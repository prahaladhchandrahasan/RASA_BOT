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


## what is corona
* corona_intro
  - utter_corona_intro

## how does corona spread
* corona_spread
  - utter_corona_spread
## corona food spread
* corona_food_spread
  - utter_corona_food_spread

## corona warm weather
* warm_weather
  - utter_warm_weather
## corona high risk
* high_risk
   - utter_high_risk



## corona symptoms
* corona_symptoms
  - utter_corona_symptoms

## helpline number
* helpline_numbers
  - utter_helpline_numbers



## corona statewise
* corona_state
  - action_corona_tracker


