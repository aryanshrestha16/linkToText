from openai import OpenAI
from termcolor import colored

client = OpenAI()

def generate_summary(transcript: str) -> str:
        print(colored('Generating Summary... \n', 'green'))
        user_input = "generate me a detailed summary of this video. If this video is related to computer science give me a code example otherwise dont say anything about code." + transcript
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages =  [
            {"role": "user", "content": user_input}
        ]
        )

        reply_content = completion.choices[0].message.content
        print(colored(reply_content, 'green'))
