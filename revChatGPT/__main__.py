import json
from os.path import exists
from os import getenv

from revChatGPT.ChatGPT import Chatbot


def get_input(prompt):
    # prompt for input
    lines = []
    print(prompt, end="")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Join the lines, separated by newlines, and print the result
    user_input = "\n".join(lines)
    # print(user_input)
    return user_input


def configure():
    config_files = ["config.json"]
    xdg_config_home = getenv("XDG_CONFIG_HOME")
    if xdg_config_home:
        config_files.append(f"{xdg_config_home}/revChatGPT/config.json")
    user_home = getenv("HOME")
    if user_home:
        print(f"{user_home}")
        config_files.append(f"{user_home}/.config/revChatGPT/config.json")

    config_file = next((f for f in config_files if exists(f)), None)
    if config_file:
        with open(config_file, encoding="utf-8") as f:
            config = json.load(f)
    else:
        print("No config file found.")
        raise Exception("No config file found.")

    class_to_rasa = chatGPTClass(config)
    return class_to_rasa


class chatGPTClass:
    def __init__(self, config):
        print("Logging in...")
        self.chatbot = Chatbot(config)

    async def get_responce_to_rasa(self, input_message="Hello"):
        print("Start of get_responce_to_rasa")
        prompt = input_message

        try:
            print("Chatbot: ")
            message = self.chatbot.ask(
                prompt,
                conversation_id=self.chatbot.config.get("conversation"),
                parent_id=self.chatbot.config.get("parent_id"),
            )
            return message["message"]
        except Exception as exc:
            print("Something went wrong!")
            print(exc)