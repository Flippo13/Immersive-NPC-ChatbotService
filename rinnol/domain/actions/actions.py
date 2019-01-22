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
        return "check_reward"

    @staticmethod
    def required_slots(tracker):

        return["freedom"]

    def slot_mappings(self):

        return { "freedom": [self.from_entity(entity="freedom",
                        intent=["promise_freedom","comply_to_request"]),
                        self.from_intent(intent='affirm', value=True),
                        self.from_intent(intent="negative", value=False),
                        self.from_entity(entity="thread", intent=["force_help"])]}

    @staticmethod
    def freedom_synonyms():
        return["out","free","outside","out of here"]

    @staticmethod
    def threads_synonyms():
        return["demands", "no way", "no", "no chance"]

        
    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        """Validate requested slot else reject execution of the from action"""

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)

        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        for slot, value in slot_values.items():
            if slot == 'freedom':
                if isinstance(value,str):
                    if value.lower() not in self.freedom_synonyms():
                        dispatcher.utter_template('utter_request_rewards', tracker)

                        slot_values[slot] = None

                    elif value.lower() in self.threads_synonyms():
                        

                        slot_values[slot] = False

                    elif value.lower() in self.freedom_synonyms():
                       

                        slot_values[slot] = True


        return [SlotSet(slot, value) for slot, value in slot_values.items()]
            

    def submit(self, dispatcher, tracker, domain):
        if (tracker.get_slot("freedom")) is True:
            dispatcher.utter_template('utter_thank_you', tracker)
        else:
            dispatcher.utter_template('utter_comply', tracker)

        return[]
        

class Comply(Action):

    def name(self):
        return "action_comply"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_comply',tracker)

        return[SlotSet("freedom","No Freedom")]


class NameVeeq(Action):

    def name(self):
        return "action_nameveeq"

    def run(self, dispatcher, tracker, domain):
        
        freedomSlot = tracker.get_slot("freedom")

        if freedomSlot is not None:
            
            dispatcher.utter_template('utter_name_veeq',tracker)

            return[SlotSet("name", "Veeq")]
        
        else:
            

            dispatcher.utter_template('utter_state_rewards',tracker)
        
            return[] 

class RoleVeeq(Action):

    def name(self):
        return "action_roleveeq"

    def run(self, dispatcher, tracker, domain):

        nameSlot = tracker.get_slot("name")

        if nameSlot is not None:
            dispatcher.utter_template('utter_role_veeq',tracker)

            return[]
        
        else: 

            dispatcher.utter_template('utter_ask_who',tracker)

        return[]

class AppearanceVeeq(Action):

    def name(self):
        return "action_appearanceveeq"

    def run(self, dispatcher, tracker, domain):

        
        nameSlot = tracker.get_slot("name")

        if nameSlot is not None:
            dispatcher.utter_template('utter_appearance_veeq',tracker)

            return[]
        
        else: 

            dispatcher.utter_template('utter_ask_who',tracker)
            return[]

class HappyAnimation(Action):

    def name(self):
        return "action_happyanimation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_custom_message({'animation':'happy'})


        return[]

class AngryAnimation(Action):

    def name(self):
        return "action_angryanimation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_custom_message({'animation':'angry'})


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