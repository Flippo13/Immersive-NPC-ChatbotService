## greet
* greet
    - action_happyanimation
    - utter_greet
* ask_name 
    - action_happyanimation
    - utter_name

## ask name
* ask_name
    - action_happyanimation
    - utter_name

## information raih
* ask_information_raih
    - action_happyanimation
    - utter_information_raih

## information raihkru
* ask_information_raihkru
    - action_happyanimation
    - utter_information_raihkru

## information species
* ask_information_species
    - action_happyanimation
    - utter_information_species

## insult
* insult
    - action_angryanimation
    - utter_insult

## compliment
* compliment
    - action_happyanimation
    - utter_compliment

## role Rinnol
* ask_role_rinnol
    - action_happyanimation
    - utter_role_rinnol

## role Akemaz
* ask_role
    - action_happyanimation
    - utter_role

## play dump 1
* ask_information
    - action_happyanimation
    - utter_play_dump

## play dump 2
* ask_veeq_personality
    - action_happyanimation
    - utter_play_dump

## play dump 3
* ask_guess_info
    - action_happyanimation
    - utter_play_dump

## play dump 4
* promise_freedom
    - action_happyanimation
    - utter_play_dump

## play dump 5
* ask_info_location
    - action_happyanimation
    - utter_play_dump

## play dump 6
* ask_location_veeq
    - action_happyanimation
    - utter_play_dump

## play dump 7
* ask_appearance_veeq
    - action_happyanimation
    - utter_play_dump

## mood
* ask_mood
    - action_happyanimation
    - utter_mood

## happy path 1
* force_help{"name":"Veeq"} 
    - utter_giving_in
* ask_information
    - utter_information
* positive
    - utter_help

## happy path 2
* force_help{"name":"Veeq"}
    - action_angryanimation
    - utter_giving_in
* positive
    - utter_information
* positive
    - action_happyanimation
    - utter_help

## happy path 3
* force_help{"name":"Veeq"}
    - utter_giving_in
* confirm
    - utter_information
* positive
    - action_happyanimation
    - utter_help

## happy path 4
* force_help{"name":"Veeq"}
    - utter_giving_in
* negative
    - utter_ultimatum
* positive
    - action_happyanimation
    - utter_help

## Generated Story 3226747728899169231
* greet
    - action_happyanimation
    - utter_greet
* ask_name
    - action_happyanimation
    - utter_name
* compliment
    - action_happyanimation
    - utter_compliment
* ask_info_location
    - action_happyanimation
    - utter_play_dump
* force_help{"name": "Veeq"}
    - slot{"name": "Veeq"}
    - utter_giving_in
* negative
    - utter_ultimatum
* confirm{"information": "information"}
    - utter_help
* goodbye

