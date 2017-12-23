from __future__ import print_function
from botocore.vendored import requests


# --------------- Main handler ------------------

def lambda_handler(event, context):
    #print(event['context'])
    try:
        deviceId = event['context']['System']['device']['deviceId']
        print("deviceId is "+deviceId)
        apiAccessToken = event['context']['System']['apiAccessToken']
        print("apiAccessToken is "+apiAccessToken)
        apiEndpoint = event['context']['System']['apiEndpoint']
        print("apiEndpoint is "+apiEndpoint)
    except:
        deviceId = 'amzn1.ask.device.AF5F5QCLDFWRHP3VEC2LGIJHE24XUZK4V6RMGPN3BUG46L5OFPBQHBLX2LRJYWNW5EW6A6BMJYGRNV2K2TKVNBBRTFDQMI74J3M3R5Y6YC2A5D7L3AK5BTBJWLLWPUHODULN6QZZTG3SNE2FJHGZ7FQ43FDA'
        apiEndpoint = 'https://api.eu.amazonalexa.com'
        apiAccessToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjNiOWQ2MjZjLWZkYzgtNDhkNy04N2E2LWU2YTZkOTg4MjM0YyIsImV4cCI6MTUxMTcwNDUxOCwiaWF0IjoxNTExNzAwOTE4LCJuYmYiOjE1MTE3MDA5MTgsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjoiQXR6YXxJd0VCSVBDbGl0eEhYRzNMRkhRdk85dm9wcnZ3S1l4dWpZblI0TFMwSDJtUU92UWNVa3JEWlNxYjAtajdEWVdlaVl1MDhtblctTkVNaDNkN1VwclFWcGZlSE0zYWx4bnRVdThyMDdKT1FscTBNbEtSR3JTNXE3d3RPYkRrbHV4N2gwRFAzVDN6QTN6VldxdEc4NTgwSnIzZ3gxQVNka1NVTWNyVVpIRFo4Y2NqSlRoWHBLVTg2TVUxRHl6VkZIU1cwanJkTDRPVTRTblR3X0RVRERuN0tRSDVIQjdQWVJBbWlMWmdlYjNXQTJGSlg3cWdrNDZpUVlYdlRXeUJVamRqcEdSczZPZ0xkTkhncTQxbjJVaWJ5dWRWS0Vtb1VMcjNPTkxXN1pLbDJwZGFobldZT2R6UWNlb0VGOUoxY3lRcy1JQnJQX0lTU21VWk5tNjV2ek1NenhfX1VPUkhkblQwSmFxRmxsN3VlcUpvR01QQUUzQzZ5RUhybi13cmhUT3ZpbFhTdXplb3ZtNmJrTDZSUndzTkEzQ0dHRldTenAwMExRY21NNFRwcl9QRThxVm1fbTF5OE9wbjZLZlFiR0ItTndsbGJzTXdZVDFjZDkzcnNNQjVZcWdOMzgxbkJiQWxGdVNuQ3N0X3U4RGRVVmtDRklocy1qMGtOUDd6XzBnb0ZXZW11aXciLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUY1RjVRQ0xERldSSFAzVkVDMkxHSUpIRTI0WFVaSzRWNlJNR1BOM0JVRzQ2TDVPRlBCUUhCTFgyTFJKWVdOVzVFVzZBNkJNSllHUk5WMksyVEtWTkJCUlRGRFFNSTc0SjNNM1I1WTZZQzJBNUQ3TDNBSzVCVEJKV0xMV1BVSE9EVUxONlFaWlRHM1NORTJGSkhHWjdGUTQzRkRBIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUdPUFpMV0VPUFZEVVM3NVdKWE80QUhOUkhETU1KS000SERZTzVFNjVaTDdVN0haTUFFRkNJSFpVVlJESlk2QlZRWUg3VEhBSExBWjM3NVgzVFdHV0k1VVhWSU9NNUpHRzZVU1RRRU1ZWDU3MkdRM01FT05XQ1hJMklZMk5MNlpTTFQyR1FLU1k2VDVGS1ZISUtSVURGWEdMTjZIQllVR0lIWkNLQURUQ1pPSkpKSVk1NTVRWjZWMlFEM0ZBWVFHV0tPS0ozUTQyVldHQUVRIn19.hRrFKZfsuXKNjdZhlynCKHuopqWW6vr-pdmXZKzEcuiwgVhIfkUNXmOOV4n7d0yrV_fCnoIB1pq5DGwJsJEff63RAwi2PGHHCJ0l0HX0iDqTmokiRJPZnarsQf6k6RZVpbdmPJTPEXwUgGRxtzMmTE-z6sMoRCazyQ1fQaycVeogrsGFd6ytTa1GtZ7j1-dAyP46dhKsIF4DkZqMc6LnVimmyl-A5KKFndnA66u261UjNZSK6lZlmMhn0ZZBcT1EEqCyDWOBPCUvU3odP-J4tHJ8ftE4Mv3wVUmf4xQNbD97MR3Uyryoa9ApGq29SVO8WrRu6URBlKsfhBVR6L-mIQ'
        print("Skipped")
    headers = {'Authorization': 'Bearer '+apiAccessToken}
    url = apiEndpoint + '/v1/devices/'+deviceId+'/settings/address'
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return permissions_error(r)
    return say_postcode(r.json()['postalCode'])
    if 'session' in event and event['session']['application']['applicationId'] != "amzn1.ask.skill.3b9d626c-fdc8-48d7-87a6-e6a6d988234c":
        raise ValueError("Invalid Application ID")
    if event['request']['type'] == "LaunchRequest":
        return get_help()
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])


# --------------- Helpers that build all of the responses -t---------------------

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

def say_postcode(postcode):
    speech_output = 'Your postcode is '+postcode
    card_title = 'Google Maps Help'
    should_end_session = True
    return build_response(build_speechlet_response(card_title, speech_output, None, should_end_session))

def get_help():
    speech_output = 'OK'
    card_title = 'Google Maps Help'
    should_end_session = True
    return build_response(build_speechlet_response(card_title, speech_output, None, should_end_session))

def permissions_error(r):
    speech_output = 'Sorry, I do not know your address. Please check the settings in the Alexa app.'
    card_title = 'Google Maps error '+r.status_code
    should_end_session = True
    return build_response(build_speechlet_response(card_title, speech_output, None, should_end_session))

        
def do_nothing():
    return build_response({})


# --------------- Events ------------------

def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    print("on_intent, session: ")
    print(session)
    # Dispatch to your skill's intent handlers
    if intent_name == "GetDirections":
        return get_directions(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help()
    elif intent_name == "AMAZON.CancelIntent":
        return do_nothing()
    elif intent_name == "AMAZON.StopIntent":
        return do_nothing()
    else:
        raise ValueError("Invalid intent")



