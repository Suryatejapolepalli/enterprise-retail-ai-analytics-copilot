from openai import OpenAI

client = OpenAI()


def generate_business_insight(question, dataframe):

    sample_data = dataframe.head(10).to_string(index=False)

    prompt = f"""
You are a senior business analyst.

User question:
{question}

Query result sample:
{sample_data}

Generate:
1. Short executive summary
2. Key business insight
3. Important trend or observation

Keep the response concise and professional.
"""

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=prompt
    )

    return response.output_text.strip()