import json

from db import load_schema, execute_sql
from prompt import build_fix_prompt, build_sql_prompt
from llm import call_llm
from utils import extract_sql, is_valid_sql



MAX_GENERATE_RETRY = 3
MAX_EXECUTION_RETRY = 3



def generate_sql(question, schema):

    prompt = build_sql_prompt(question, schema)

    for attempt in range(MAX_GENERATE_RETRY):

        print(f"Generate Attempt {attempt+1}")

        response = call_llm(prompt)

        sql = extract_sql(response)

        if is_valid_sql(sql):
            return sql

        prompt += """

            Remember:

            Return ONLY SQL.
        """

    raise Exception("Unable to generate SQL.")


def execute_with_retry(question, schema, sql):

    for attempt in range(MAX_EXECUTION_RETRY):
        try:
            print(f"Execution Attempt {attempt+1}")

            return execute_sql(sql)

        except Exception as e:

            print(e)

            prompt = build_fix_prompt(
                question,
                schema,
                sql,
                str(e),
            )

            sql = extract_sql(call_llm(prompt))

    raise Exception("Unable to execute SQL after retries.")


def generate_final_answer(question, sql, result):

    prompt = f"""
        You are a helpful data analyst.

        User Question:
        {question}

        Generated SQL:
        {sql}

        SQL Result:
        {json.dumps(result, indent=2, default=str)}

        Instructions:
        1. Answer only using the SQL result.
        2. Do not mention SQL.
        3. If the result is empty, say that no matching records were found.
        4. Keep the answer concise.
    """

    return call_llm(prompt)

def text_to_sql(question):

    schema = load_schema()

    sql = generate_sql(question, schema)

    print("\nGenerated SQL\n")
    print(sql)

    result = execute_with_retry(
        question,
        schema,
        sql,
    )
    answer = generate_final_answer(
        question=question,
        sql=sql,
        result=result,
    )

    return {
        "question": question,
        "sql": sql,
        "result": result,
        "answer": answer
    }