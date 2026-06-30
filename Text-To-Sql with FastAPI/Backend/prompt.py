def build_sql_prompt(question, schema):

    return f"""
        You are an expert PostgreSQL SQL Generator.

        Return ONLY SQL.

        Rules

        1. Return SQL only.
        2. No explanation.
        3. No markdown.
        4. No ```sql
        5. Use only schema below.
        6. Never create columns.
        7. Never create tables.
        8. PostgreSQL syntax only.

        Schema

        {schema}

        Question

        {question}
    """

def build_fix_prompt(question, schema, previous_sql, error):

    return f"""
        You generated this SQL

        {previous_sql}

        Database Error

        {error}

        Schema

        {schema}

        Question

        {question}

        Correct the SQL.

        Return ONLY SQL.
    """

