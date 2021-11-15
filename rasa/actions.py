# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionSchedule(Action):

     def name(self) -> Text:
         return "action_schedule"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

           print(tracker.get_slot("section"),tracker.get_slot("group"))
           if(("m2" in tracker.get_slot("section")) and ("alternant" in tracker.get_slot("group"))) : 
               res = "5223"
           elif(("m2" in tracker.get_slot("section")) and ("classique" in tracker.get_slot("group"))) : 
               res = "5222"
           text="https://edt-api.univ-avignon.fr/app.php/api/exportAgenda/tdoption/"+res
           dispatcher.utter_message(text)
	
           return []

