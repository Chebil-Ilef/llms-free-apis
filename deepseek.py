import ollama



def main():
    """
        install ollama using pip install ollama
        pull the model using ollama pull model_name via cli
    """
    # Initialize the model
    model_name = "deepseek-r1:8b" # 4.9 GB

    # Use the model to generate text (for example)
    response = ollama.chat(model=model_name, messages=[
    {
        'role': 'user',
        'content': 'Explain the concept of recursion in programming.',
    },
    ])

    print(response['message']['content'])



if __name__ == '__main__':
    main()
