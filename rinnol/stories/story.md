##happy path
* ask_mole
    - utter_state_rewards
    - check_reward
    - form{"name":"action_checkreward"}
    - form{"name":null}
* ask_help
    - utter_positive

## greet
* greet
    - utter_greet


## ask info
* ask_info
    - utter_info

## ask info location
* ask_info_location
    - utter_info_location

## ask name
* ask_name
    - utter_name

## ask backstory
* ask_backstory
    - utter_backstory
* elaborate
    - utter_negative

## promise freedom

* promise_freedom
    - utter_thank_you
* ask_mole
    - action_nameveeq
* ask_role_veeq
    - action_roleveeq
* ask_appearance_veeq
    - action_appearanceveeq

## promise freedom

* promise_freedom
    - utter_thank_you
* ask_mole
    - action_nameveeq
* ask_appearance_veeq
    - action_appearanceveeq
* ask_role_veeq
    - action_roleveeq

## ask role
* ask_role_veeq
    - action_roleveeq


## ask appearance
* ask_appearance_veeq
    - action_appearanceveeq

## Generated Story 5544121430277218876
* ask_mole
    - utter_state_rewards
    - check_reward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* form: promise_freedom{"freedom": "out"}
    - form: action_checkreward
    - slot{"freedom": "out"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 7392903516996215448
* ask_mole
    - utter_state_rewards
    - check_reward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* force_help
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_comply

## Generated Story -8615622466873028937
* ask_mole
    - utter_state_rewards
    - check_reward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* force_help
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_comply

## Generated Story -3575530110341386893
* ask_appearance_veeq
    - action_appearanceveeq
* ask_mole
    - utter_state_rewards
    - check_reward
    - form{"name": "check_reward"}
    - slot{"requested_slot": "freedom"}
* form: promise_freedom{"freedom": "out"}
    - form: check_reward
    - slot{"freedom": true}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_mole
    - action_nameveeq
    - slot{"name": "Veeq"}
* ask_appearance_veeq
    - action_appearanceveeq
* ask_role_veeq{"job": "job"}
    - action_roleveeq
* goodbye
    - utter_goodbye

## Generated Story 5544121430277218876
* ask_help
    - utter_state_rewards
    - check_reward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* form: promise_freedom{"freedom": "out"}
    - form: action_checkreward
    - slot{"freedom": "out"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 7392903516996215448
* ask_help
    - utter_state_rewards
    - check_reward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* force_help
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_comply

## Generated Story -8615622466873028937
* ask_help
    - utter_state_rewards
    - check_reward
    - form{"name": "action_checkreward"}
    - slot{"requested_slot": "freedom"}
* force_help
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_comply

## Generated Story -3575530110341386893
* ask_appearance_veeq
    - action_appearanceveeq
* ask_help
    - utter_state_rewards
    - check_reward
    - form{"name": "check_reward"}
    - slot{"requested_slot": "freedom"}
* form: promise_freedom{"freedom": "out"}
    - form: check_reward
    - slot{"freedom": true}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_mole
    - action_nameveeq
    - slot{"name": "Veeq"}
* ask_appearance_veeq
    - action_appearanceveeq
* ask_role_veeq{"job": "job"}
    - action_roleveeq
* goodbye
    - utter_goodbye

