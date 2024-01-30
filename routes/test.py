from flask import Blueprint
from clients.ClioDbClient import ClioDbClient

test_blueprint = Blueprint("test_blueprint", __name__)


@test_blueprint.route("/test", methods=["POST"])
def test():
    print("test")
    # content_type = request.headers.get("Content-Type")
    # prompt = None
    # if content_type == "application/json" and request.json:
    #     json_payload = request.json
    #     prompt = json_payload["prompt"]
    # else:
    #     return "Content-Type not supported!"

    conn = ClioDbClient.getClioDb()
    cur = conn.cursor()  # type: ignore
    try:
        cur.execute("select * from matters limit 10;")
        results = cur.fetchall()
        conn.commit()  # type: ignore
        # Convert the response to a list of dicts
        # contact_list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in contact]
        # print('results', results)
        # results_list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in results]
        # print('results_list', results_list)
        # return results
    except BaseException:
        conn.rollback()  # type: ignore
        raise Exception("Error with DB")
    finally:
        pass

    return {"completion": str(results)}

    # return
    # return {"tool": "CONVERSATIONAL_AGENT", "completion": output}
