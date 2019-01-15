## greet
* greet
    - utter_greet
* ask_name 
    - utter_name

## ask name
* ask_name
    - utter_name

## information raih
* ask_information_raih
    - utter_information_raih

## information raihkru
* ask_information_raihkru
    - utter_information_raihkru

## information species
* ask_information_species
    - utter_information_species

## insult
* insult
    - utter_insult

## compliment
* compliment
    - utter_compliment

## role Rinnol
* ask_role_rinnol
    - utter_role_rinnol

## role Akemaz
* ask_role
    - utter_role

## play dump 1
* ask_information
    - utter_play_dump

## play dump 2
* ask_veeq_personality
    - utter_play_dump

## play dump 3
* ask_guess_info
    - utter_play_dump

## play dump 4
* promise_freedom
    - utter_play_dump

## play dump 5
* ask_info_location
    - utter_play_dump

## play dump 6
* ask_location_veeq
    - utter_play_dump

## play dump 7
* ask_appearance_veeq
    - utter_play_dump

## mood
* ask_mood
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
    - utter_giving_in
* positive
    - utter_information
* positive
    - utter_help

## happy path 3
* force_help{"name":"Veeq"}
    - utter_giving_in
* confirm
    - utter_information
* positive
    - utter_help

## happy path 4
* force_help{"name":"Veeq"}
    - utter_giving_in
* negative
    - utter_ultimatum
* positive
    - utter_help

## Generated Story 3226747728899169231
* greet
    - utter_greet
* ask_name
    - utter_name
* compliment
    - utter_compliment
* ask_info_location
    - utter_play_dump
* force_help{"name": "Veeq"}
    - slot{"name": "Veeq"}
    - utter_giving_in
* negative
    - utter_ultimatum
* confirm{"information": "information"}
    - utter_help
* goodbye

