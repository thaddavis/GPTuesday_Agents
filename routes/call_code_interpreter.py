from flask import Blueprint
from time import sleep
from openai import OpenAI

call_code_interpreter_blueprint = Blueprint("call_code_interpreter", __name__)


@call_code_interpreter_blueprint.route("/call_code_interpreter", methods=["POST"])
def call_code_interpreter():
    client = OpenAI()

    # Upload a file with an "assistants" purpose
    file = client.files.create(
        file=open("scratch/billing.csv", "rb"), purpose="assistants"
    )

    assistant = client.beta.assistants.create(
        instructions="You are a paralegal. When asked a question related to legal practice matters, you may write code, execute code, generate files, and generate diagrams to clearly explain answers to team members.",
        model="gpt-4-1106-preview",
        tools=[{"type": "code_interpreter"}],
        file_ids=[file.id],
    )

    thread = client.beta.threads.create(
        # metadata={"assistant": assistant.id},
        # messages=[
        #     {
        #         "role": "user",
        #         "content": "Build a bar chart showing the total billed hours of my team",
        #         "file_ids": [file.id],
        #     }
        # ],
    )

    client.beta.threads.messages.create(
        thread_id=thread.id,
        content="Build a bar chart showing the total billed hours of my team",
        role="user",
    )

    print("thread", thread)

    run = client.beta.threads.runs.create(
        thread_id=thread.id, assistant_id=assistant.id
    )

    retrieved_run = client.beta.threads.runs.retrieve(
        thread_id=thread.id, run_id=run.id
    )

    print("retrieved_run", retrieved_run)

    # Polling mechanism to see if runStatus is completed
    # This should be made more robust.
    while retrieved_run.status != "completed":
        sleep(2)
        retrieved_run = client.beta.threads.runs.retrieve(
            run_id=run.id, thread_id=thread.id
        )
        print("- - -")
        print("retrieved_run", retrieved_run)

    messages = client.beta.threads.messages.list(thread.id)
    print("- - -")
    # pprint.pprint(messages)

    file_id = None
    for message in messages.data:
        print("-_-_-")
        print(type(message.content[0]))
        print(
            str(type(message.content[0]))
            == "<class 'openai.types.beta.threads.message_content_image_file.MessageContentImageFile'>"
        )
        if (
            str(type(message.content[0]))
            == "<class 'openai.types.beta.threads.message_content_image_file.MessageContentImageFile'>"
        ):
            print("!-!")
            print(message.content[0].image_file.file_id)  # type: ignore
            file_id = message.content[0].image_file.file_id  # type: ignore
            break

        # for message_content in message:
        #     print("-!-!-")
        #     print(message_content)
        #     print(type(message_content))
    # if messages.data[0].content[0].type == "image_file":
    #     file_id = messages.data[0].content[0].image_file.file_id

    if file_id:
        api_response = client.files.with_raw_response.content(file_id=file_id)

        if api_response.status_code == 200:
            content = api_response.content
            with open("image.png", "wb") as f:
                f.write(content)
            print("File downloaded successfully.")

    return {
        "tool": "CODE_INTERPRETER",
        "completion": "",
    }
