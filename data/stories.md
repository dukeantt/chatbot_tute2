## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## ask function
* ask_func_list
    - utter_showfunclist
    
## greet with name
* greet
    - utter_greet
* give_name
    - utter_greet_with_detail
* ask_name
    - utter_ask_name
    
## approve
* affirm
    - utter_agree
    
## show_lottery_result
* greet
    - utter_greet
* ask_lottery
    - action_get_lottery
* affirm
    - utter_agree

## ask lottery simple
* ask_lottery
    - action_get_lottery
