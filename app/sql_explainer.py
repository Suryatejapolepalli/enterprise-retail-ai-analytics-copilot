from openai import OpenAI

client = OpenAI()


def explain_sql(sql_query):

    prompt = f"""
You are a senior data analyst.

Explain the following SQL query in simple business language.

SQL Query:
{sql_query}

Keep explanation concise and professional.
"""

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=prompt
    )

    return response.output_text.strip()