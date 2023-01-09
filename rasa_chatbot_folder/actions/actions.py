# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from revChatGPT import __main__
import asyncio

bot = __main__.configure()

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_chatgpt"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            mesage = tracker.latest_message["text"]

            ans = bot.get_responce_to_rasa(mesage)
            ans_aft = await ans 
            dispatcher.utter_message(text=ans_aft)
            return []