import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def main():
    """
    GPT-4 Turbo, Whisper, DALL·E using GitHub Token.
    Go to settings, developer settings, personal access tokens, generate a new token.

    """
    client= OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv('GITHUB_TOKEN')
    )

    # batch processing to avoid early hit of rate limit
    queries = [
        "What is AI?",
        "Explain Quantum Computing.",
        "How does deep learning work?"
    ]

    combined_prompt = "\n\n".join([f"{i+1}. {q}" for i, q in enumerate(queries)]) + "\n\nRespond to each point separately."

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": combined_prompt}
        ],
        max_tokens=1000
    )

    print(response.choices[0].message.content)  # Prints all answers in one response, 1 API call instead of 3


if __name__ == '__main__':
    
    main()



