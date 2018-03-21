from __future__ import print_function
from botocore.vendored import requests
import googlemaps
from os import environ
from datetime import datetime

# --------------- Main handler ------------------

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return get_help()
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event)

def on_intent(event):
    intent = event['request']['intent']
    intent_name = event['request']['intent']['name']
    print("on_intent, session: ")
    print(event['session'])
    # Dispatch to your skill's intent handlers
    if intent_name == "GetDirectionsTo":
        return get_directions(event)
    elif intent_name == "GetDirectionsFromTo":
        return get_directions(event)
    elif intent_name == "GetCommuteToWork":
        return get_commute_to_work(event)
    elif intent_name == "GetCommuteFromWork":
        return get_commute_from_work(event)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help()
    elif intent_name == "AMAZON.CancelIntent":
        return do_nothing()
    elif intent_name == "AMAZON.StopIntent":
        return do_nothing()
    else:
        raise ValueError("Invalid intent")

def get_directions(event):
    destination = event['request']['intent']['slots']['tocity']['value']
    if 'fromcity' in event['request']['intent']['slots']:
        start_address = start_postcode = event['request']['intent']['slots']['fromcity']['value']
    else:
        start_address, start_postcode = get_my_address(event)
        if not start_address:
            return permissions_error()
    print('start: '+start_address+'; destination: '+destination)
    return get_duration(start_postcode, destination, start_address)
    
def get_commute_to_work(event):
    start_address, start_postcode = get_my_address(event)
    if not start_address:
        return permissions_error()
    destination = get_work_address()
    print('start: '+start_address+'; destination: '+destination)
    return get_duration(start_postcode, destination, start_address)
    
def get_commute_from_work(event):
    home_address, destination = get_my_address(event)
    if not home_address:
        return permissions_error()
    start_address = start_postcode = get_work_address()
    print('start: '+start_address+'; destination: '+destination)
    return get_duration(start_postcode, destination, start_address)

def get_my_address(event):
    try:
        deviceId = event['context']['System']['device']['deviceId']
        print("deviceId is "+deviceId)
        apiAccessToken = event['context']['System']['apiAccessToken']
        print("apiAccessToken is "+apiAccessToken)
        apiEndpoint = event['context']['System']['apiEndpoint']
        print("apiEndpoint is "+apiEndpoint)
        headers = {'Authorization': 'Bearer '+apiAccessToken}
        url = apiEndpoint + '/v1/devices/'+deviceId+'/settings/address'
        r = requests.get(url, headers=headers)
        print(r.json())
        return r.json()['addressLine1'], r.json()['postalCode']
    except:
        try:
            return environ['HOME'], environ['HOME']
        except:
            return False, False

def get_work_address():
    return environ['WORK']

def get_duration(start_postcode, end, start_address):
    gmaps = googlemaps.Client(key=environ['API_KEY'])
    try:
        directions_result = gmaps.directions(start_postcode, end, departure_time=datetime.now())
    except:
        directions_result = []
    if len(directions_result) == 0:
        try:
            directions_result = gmaps.directions(start_postcode+', '+environ['COUNTRY'], end+', '+environ['COUNTRY'], departure_time=datetime.now())
        except:
            directions_result = []
        if len(directions_result) == 0:   
            return ask_for_repeat(end)
    leg = directions_result[0]['legs'][0]
    duration=leg['duration_in_traffic']['text']
    summary = directions_result[0]['summary']
    to_say="Right now, it takes "+duration+" to get from "+start_address+" to "+end+", via "+summary
    return say_duration(to_say)

def ask_for_repeat(end):
    speech_output = "I'm sorry, I couldn't find "+end+", could you be more specific?"
    card_title = 'Google Maps Help'
    should_end_session = False
    return build_response(build_speechlet_response(card_title, speech_output, None, should_end_session))

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_short_speechlet_response(output, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'shouldEndSession': should_end_session
    }

def build_response(speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': {},
        'response': speechlet_response
    }

# --------------- Functions that control the skill's behavior ------------------

def say_duration(duration):
    speech_output = duration
    card_title = 'Google Maps'
    should_end_session = True
    return build_response(build_speechlet_response(card_title, speech_output, None, should_end_session))

def get_help():
    speech_output = 'Welcome to Google Maps'
    card_title = 'Google Maps'
    should_end_session = False
    return build_response(build_speechlet_response(card_title, speech_output, None, should_end_session))

def permissions_error():
    speech_output = 'Sorry, I do not know your address. Please check the settings in the Alexa app.'
    card_title = 'Google Maps error'
    should_end_session = True
    return build_response(build_speechlet_response(card_title, speech_output, None, should_end_session))

def do_nothing():
    return build_response({})