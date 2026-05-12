from openai import OpenAI
from prompts import SYSTEM_PROMPT

client = OpenAI()


def generate_sql(question: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

User question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    sql = response.output_text.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql