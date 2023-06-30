import logging

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from actions.openai_api import request_gpt

logger = logging.getLogger(__name__)

logger.info(f"Rasa Action Server started.")

class ActionSensitivTopic(Action):

    def name(self) -> Text:
        return "action_sensitiv_topic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logger.info("action_sensitiv_topic")

        user_message = tracker.latest_message.get('text')
        
        gpt_response = request_gpt(user_message)
        if gpt_response == "yes":
            return [SlotSet("sensitive_topic_flag", True)]
        else:
            return [SlotSet("sensitive_topic_flag", False)]
        