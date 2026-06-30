import re
def extract_sql(text):

    text = text.strip()

    text = re.sub(r"```sql", "", text, flags=re.IGNORECASE)
    text = text.replace("```", "")

    return text.strip()


def is_valid_sql(sql):

    sql = sql.lower()

    keywords = (
        "select",
        "with",
    )

    return sql.startswith(keywords)