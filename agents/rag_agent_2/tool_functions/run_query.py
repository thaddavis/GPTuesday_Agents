from clients.ClioDbClient import ClioDbClient
import json
from datetime import date, datetime


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def run_query(query: str) -> str:
    print("Enter RunQuery tool...")
    conn = ClioDbClient.getClioDb()
    cur = conn.cursor()  # type: ignore
    try:
        cur.execute(query)
        results = cur.fetchall()
        conn.commit()  # type: ignore
        # Convert the response to a list of dicts
        # contact_list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in contact]
        # print("results", results)
        # column_names = [desc[0] for desc in cur.description]
        # print(column_names)
        # results_list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in results]
        # print('results_list', results_list)
        return json.dumps(results, default=json_serial)
        # return str(results)
    except BaseException as e:
        conn.rollback()  # type: ignore
        print("Exception", e)
        return f"ERROR when running the query {query}"
    finally:
        pass
