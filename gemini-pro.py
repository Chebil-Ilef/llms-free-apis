import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    """
    To use the Gemini API, you'll need an API key. If you don't already have one, create a key in Google AI Studio.
        https://aistudio.google.com/app/apikey
    """
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    prompt = """
    Below are some examples of short stories. Use these patterns to generate a new story.

    Example 1:
    Input: A magic backpack that grants wishes.
    Output: Once upon a time, Jake found an old backpack in his attic. When he whispered a wish into its pocket, it came true! But soon, he realized every wish had a consequence...

    Example 2:
    Input: A talking cat who solves mysteries.
    Output: In a quiet town, a detective named Lily had an unusual partner—a cat named Whiskers who could talk! Together, they uncovered hidden secrets, solving the biggest mysteries the town had ever seen.

    Now, write a new story based on the input below:
    
    Input: A magic backpack that teleports the wearer.
    Output:
    """

    # Customize LLM parameters
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.7,  # Controls randomness (0: deterministic, 1: creative)
            "top_p": 0.9,        # Nucleus sampling (higher = more diverse responses)
            "top_k": 40,         # Limits token choices (higher = more randomness)
            "max_output_tokens": 500,  # Limit response length
        }
    )

    print(response.text)

if __name__ == '__main__':
    main()
