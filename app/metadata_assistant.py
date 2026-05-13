from openai import OpenAI
from metadata_context import BUSINESS_METADATA

client = OpenAI()


def generate_metadata_answer(question):

    prompt = f"""
You are an enterprise retail data warehouse assistant.

Business metadata:
{BUSINESS_METADATA}

Answer the user's metadata question professionally.

Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=prompt
    )

    return response.output_text.strip()