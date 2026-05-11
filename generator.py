from groq import Groq
import os
from dotenv import load_dotenv  
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def generate_response(context, question):

    prompt = f"""
    You are an environmental scientific assistant.

    Use ONLY the provided context to answer.

    Provide:
    1. A clear scientific explanation
    2. Key environmental mechanisms
    3. Important scientific observations

    If information is missing, say:
    "Information not available in retrieved context."

    CONTEXT:
    {context}

    QUESTION:
    {question}

    ANSWER:
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content