from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import json

from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


logger = logging.getLogger(__name__)


class CheckReward(FormAction): 

    def name(self):
        return "action_check_reward"


    @staticmethod
    def required_slots(tracker):

        return["money_reward", "freedom"]

    def slot_mappings(self):

        return { "money_reward": self.from_entity(entity="money_reward",
                                                  intent=["check_reward" , "promise_money", "comply_to_request"]),
                "freedom": self.from_entity(entity="freedom",
                                            intent=["check_reward", "promise_freedom","comply_to_request"])}
    
    
    @staticmethod
    def money_reward_synonyms():
        #type: () -> List[Text]
        """A small database for words for money_reward"""
        return["cash","doe", "money"]

    @staticmethod
    def freedom_synonyms():
        return["out","free","outside","out of here"]

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        """Validate requested slot else reject execution of the from action"""

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,tracker,domain))
            
            if not slot_values:

                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        for slot, value in slot_values.items():
            if slot == 'money_reward':
                if value.lower() not in self.money_reward_synonyms():
                    dispatcher.utter_template('utter_ask_money_reward', tracker)

                    slot_values[slot] = None
                    
            if slot == 'freedom':
                if value.lower() not in self.freedom_synonyms():
                    dispatcher.utter_template('utter_ask_freedom', tracker)

                    slot_values[slot] = None
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
            

    def submit(self, dispatcher, tracker, domain):

        dispatcher.utter_template('utter_submit', tracker)
        return[]
        
        
class IrritatedAnimation(Action):

    def name(self):
        return "action_irritatedanimation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_custom_message({'animation':'irritated'})


        return[]

class HappyAnimation(Action):

    def name(self):
        return "action_happyanimation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_custom_message({'animation':'happy'})


        return[]

class AngryAnimation(Action):

    def name(self):
        return "action_happyanimation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_custom_message({'animation':'happy'})


        return[]


class SuprisedAnimation(Action):

    def name(self):
        return "action_suprisedanimation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_custom_message({'animation':'suprised'})


        return[]

class ConfusedAnimation(Action):
    
    def name(self):
        return "action_confusedanimation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_custom_message({'animation':'confused'})


        return[]

class SetKeyword(Action):

    def name(self):
        return "action_setkeyword"

    def run(self, dispatcher, tracker, domain):
        keyword = tracker.get_slot("keyword")
        dispatcher.send_custom_message({"Keyword_Found":keyword})
        
        return []