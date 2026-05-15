from openai import OpenAI
from prompts import SYSTEM_PROMPT
from business_glossary import BUSINESS_GLOSSARY

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

Business Glossary:
{BUSINESS_GLOSSARY}

Conversation History:
{history_text}

Current User Question:
{question}

Instructions:

1. Follow Business Glossary strictly
2. Use warehouse values exactly
3. Use LOWER() for string filters
4. Return ONLY Athena SQL
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