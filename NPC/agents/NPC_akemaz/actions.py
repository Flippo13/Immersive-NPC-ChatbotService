from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import json

from rasa_core_sdk import Action
from rasa_core_sdk.events import FollowupAction


logger = logging.getLogger(__name__)



class ActionEmotionalResponse(Action):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
    def name(self):
        return "action_emotional_response"

    def run(self, dispatcher, tracker, domain):
        
        with open('D:/Saxion/_Year_3/Minor_Skilled/Immersive-NPC/Assets/Data/EmoFile.json') as json_data:
            d = json.load(json_data)
        
        if d['happiness'] > 0.7:
            return [FollowupAction('utter_happy_greet')]
        if d['happiness'] < 0.5 and d['happiness'] > 0.3:
            return [FollowupAction('utter_unhappy_greet')]
        if d['happiness'] < 0.3 :
            return [FollowupAction('utter_angry_greet')]
        if d['happiness'] < 0.7 and d['happiness'] > 0.5:
            return [FollowupAction('utter_neutral_greet')]
        

class CustomActionTest(Action):
    
    def name(self):
        return "custum_action_test"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message("So, this works I guess")

        return []
       
        
        

