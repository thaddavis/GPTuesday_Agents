from time import sleep
from flask import Blueprint, make_response, jsonify

test_streaming_blueprint = Blueprint("test_streaming_blueprint", __name__)


@test_streaming_blueprint.route("/test_streaming", methods=["GET"])
def test_streaming():
    def generate():
        for x in range(3):
            print(x)
            print("sleeping")
            sleep(2)
            yield f"{x}"

    return generate(), {"Content-Type": "text/plain"}
