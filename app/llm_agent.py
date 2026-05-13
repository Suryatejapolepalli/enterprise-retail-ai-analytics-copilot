from openai import OpenAI
from prompts import SYSTEM_PROMPT

client = OpenAI()


def generate_sql(question: str, history=None) -> str:

    history_text = ""

    if history:
        for item in history[-3:]:
            history_text += f"""
Previous Question:
{item['question']}

Previous SQL:
{item['sql']}
"""

    prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{history_text}

Current User Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    sql = response.output_text.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()

    if "QUALIFY" in sql.upper():
        raise ValueError(
        "Invalid SQL generated: QUALIFY is not supported by Athena. Please retry the question." )
    return sql