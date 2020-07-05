# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
#


class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



         response = requests.get("https://api.covid19india.org/data.json").json()
         entities = tracker.latest_message['entities']
         state = None
         for e in entities:
         	if e['entity'] == "state":
         		state = e['value']


         message = "Please enter correct state name"
         if state == "india" or state == "India":
         	state = "Total"
         for data in response["statewise"]:
         	if data["state"] == state.title():
         		print(data)
         		message = "Active :" +data["active"] + "  Confirmed :" +data["confirmed"] + "  Deaths :" +data["deaths"] + "  Recovered :" +data["recovered"] + "  Last updated at :" +data["lastupdatedtime"]


         dispatcher.utter_message(message)
         return []
    	 

        