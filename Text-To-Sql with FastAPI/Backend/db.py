import psycopg2
from psycopg2.extras import RealDictCursor



DATABASE_URL = "postgresql://postgres:123456@host.docker.internal:5432/aidemo"

def get_connection():
    return psycopg2.connect(DATABASE_URL)


def load_schema():
    query = """
    SELECT
        table_name,
        column_name,
        data_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
    ORDER BY table_name, ordinal_position;
    """

    schema = {}

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)

            for row in cur.fetchall():
                table = row["table_name"]

                if table not in schema:
                    schema[table] = []

                schema[table].append(
                    f"{row['column_name']} ({row['data_type']})"
                )

    output = []

    for table, columns in schema.items():
        output.append(f"Table: {table}")

        for column in columns:
            output.append(f"    - {column}")

        output.append("")

    return "\n".join(output)


def execute_sql(sql):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(sql)

            return cur.fetchall()