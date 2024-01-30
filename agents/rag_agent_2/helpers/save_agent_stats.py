from datetime import datetime
from clients.ClioDbClient import ClioDbClient
import uuid
import json


def save_agent_stats(tic: float, toc: float, dt: datetime, final_steps: list[object]):
    conn = ClioDbClient.getClioDb()
    with conn.cursor() as cursor:  # type: ignore
        try:
            cursor.execute(
                """
            INSERT INTO agent_timing_stats (
                call_id,
                agent_version,
                timing,
                created_at,
                agent_log
            ) VALUES (%s, %s, %s, %s, %s)
            """,
                (
                    str(uuid.uuid4()),  # call_id
                    "rag-agent-2",  # tool
                    toc - tic,  # timing
                    dt,  # created_at
                    json.dumps(final_steps, indent=4),  # agent_log
                ),
            )
            conn.commit()  # type: ignore
        except BaseException as e:
            conn.rollback()  # type: ignore
            print(e)
        finally:
            pass
