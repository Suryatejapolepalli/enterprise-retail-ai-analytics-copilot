from openai import OpenAI
from rag_metadata import search_metadata

client = OpenAI()


def generate_metadata_answer(question):

    metadata_context = search_metadata(question)

    prompt = f"""
You are an enterprise metadata assistant.

Metadata Context:
{metadata_context}

User Question:
{question}

Provide a professional business explanation.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text.strip()