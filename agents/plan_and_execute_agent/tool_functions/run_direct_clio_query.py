from clients.ClioDbClient import ClioDbClient
from psycopg2 import sql


def run_direct_clio_query(results: dict):
    print("Enter RunDirectClioQuery tool...")
    # conn = ClioDbClient.getClioDb()
    # cur = conn.cursor()  # type: ignore
    try:
        # cur.execute(query)
        # results = cur.fetchall()
        # conn.commit()  # type: ignore
        # # Convert the response to a list of dicts
        # # contact_list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in contact]
        # # print('results', results)
        # # results_list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in results]
        # # print('results_list', results_list)
        return results
    except BaseException:
        print("Error in RunDirectClioQuery tool...")
        conn.rollback()  # type: ignore
        return f"ERROR when running the RunDirectClioQuery tool"
    finally:
        pass
