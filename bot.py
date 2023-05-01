import os
import openai
from dotenv import load_dotenv
import argparse
from colorama import Fore, Style, init

RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    parser = argparse.ArgumentParser(description='Chat with a Chatbot!')

    parser.add_argument('--personality', type=str, help="Personality of the chatbot", default="friendly and helpful")

    args = parser.parse_args()

    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}."

    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            user_input = input(f"{Fore.BLUE}You:{Style.RESET_ALL} ")
            messages.append({"role": "user", "content": user_input})  # saving message context
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=300)
            messages.append(response["choices"][0]["message"].to_dict())  # saving bot response
            print(f"{Fore.RED}Bot:{Style.RESET_ALL} " + response.choices[0].message.content)
        except KeyboardInterrupt:
            print("Exiting...")
            break


if __name__ == '__main__':
    main()
