## happy path
* ask_info_location
 - utter_info_location
* ask_mole
 - action_checkreward
 - form{"name":"check_reward"}
 - form{"name":null}
 - utter_state_rewards
* ask_mole
 - action_nameveeq

## happy path
* ask_info_location
 - utter_info_location
* ask_mole
 - action_checkreward
 - form{"name":"check_reward"}
* force_help
 - utter_comply
* ask_mole
 - action_nameveeq

## happy path
* ask_info_location
 - utter_info_location
* ask_mole
 - action_checkreward
 - form{"name":"check_reward"}
* force_help+ask_mole
 - action_nameveeq
 
## happy path
* ask_mole
 - action_checkreward
 - form{"name":"check_reward"}
 - form{"name":null}
 - utter_state_rewards
* ask_mole
 - action_nameveeq

## happy path
* ask_mole
 - action_checkreward
 - form{"name":"check_reward"}
* force_help+ask_mole
 - action_nameveeq

## happy path
* ask_mole
 - action_checkreward
 - form{"name":"check_reward"}
* force_help
 - utter_comply
* ask_mole
 - action_nameveeq

## Generated Story 2731415989214055349
* ask_info_location
    - utter_info_location
* ask_mole
    - action_checkreward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
    - utter_state_rewards
    - action_listen
* form: promise_freedom{"freedom": "out"}
    - action_checkreward
    - slot{"freedom": "out"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_thank_you
* ask_mole
    - action_nameveeq
    - slot{"name": "Veeq"}
* ask_appearance_veeq{"name":"Veeq"}
    - utter_appearance_veeq
* ask_role_veeq{"name":"Veeq"}
    - utter_role_veeq
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story -2145418971661494439
* greet
    - utter_greet
* ask_mood
    - utter_mood
* ask_motive
    - utter_motive
* ask_help
    - utter_request_reward
    - action_checkreward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* form: promise_freedom{"freedom": "out"}
    - form: action_checkreward
    - slot{"freedom": "out"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_thank_you
* ask_mole
    - action_nameveeq
    - slot{"name": "Veeq"}
* ask_appearance_veeq{"name":"Veeq"}
    - utter_appearance_veeq
* ask_role_veeq{"name":"Veeq"}
    - utter_role_veeq
* goodbye
    - utter_goodbye
    - action_restart


## greet
* greet
    - utter_greet

## goodbye
* goodbye
    - utter_goodbye

## chitchat
* ask_mood
    - utter_mood
* ask_motive
    - utter_motive
* ask_backstory
    - utter_backstory

## chitchat
* ask_motive
    - utter_motive
* ask_backstory
    - utter_backstory

## backstory
* ask_backstory
    - utter_backstory
    

## Generated Story 1879470576897561842
* ask_mole
    - utter_request_reward
* force_help
    - utter_comply
* ask_mole
    - action_nameveeq
    - slot{"name": "Veeq"}
* ask_appearance_veeq
    - utter_appearance_veeq
* ask_role_veeq
    - utter_role_veeq
* goodbye
    - utter_goodbye

## Generated Story 6575840438572499487
* ask_mole
    - utter_request_reward
    - action_checkreward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* form: promise_freedom{"freedom": "out"}
    - form: action_checkreward
    - slot{"freedom": "out"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_checkreward
    - form{"name": "action_checkreward"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_thank_you
* ask_mole
    - action_nameveeq
    - slot{"name": "Veeq"}
* ask_role_veeq
    - utter_role_veeq
* ask_appearance_veeq
    - utter_appearance_veeq
* goodbye
    - utter_goodbye

