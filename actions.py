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
import json
import feedparser

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionGetLottery(Action):
    def name(self) -> Text:
        return "action_get_lottery"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
        # feed parser lay dữ liệu từ rss feed
        feed_cnt = feedparser.parse(url)
        first_node = feed_cnt['entries']
        return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
        dispatcher.utter_message(return_msg)
        return []
