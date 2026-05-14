from openai import OpenAI

client = OpenAI()


def repair_sql(
    original_sql,
    athena_error
):

    prompt = f"""
You are a senior AWS Athena SQL expert.

The following Athena SQL query failed.

Original SQL:
{original_sql}

Athena Error:
{athena_error}

Fix the SQL query so it works correctly in Amazon Athena.

IMPORTANT:
- Return ONLY corrected SQL
- Do not explain
- Athena-compatible syntax only
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    fixed_sql = response.output_text.strip()

    fixed_sql = (
        fixed_sql
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    return fixed_sql