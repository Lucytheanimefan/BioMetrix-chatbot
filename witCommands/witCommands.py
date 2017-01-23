from wit import Wit

access_token = "BQHY6RUVWMZ7W74INLCAXJFSSZ5Z7OY5"#"PNUPYT4U3IP2VCZRMQN3L443Q2QO375F"

def send(request, response):
    print('Sending to user...', response['text'])
def my_action(request):
    print('Received from user...', request['text'])

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def get_forecast(request): ### the error I get for this line: TypeError: get_forecast() takes 1 positional argument but 2 were given
    print("THIS IS THE REQUEST: ")
    '''
    {'text': u'what is the weather in rome', 'context': {}, 'session_id': 'my-user-session-42', 'entities': {u'intent': [{u'confidence': 0.9949754848030923, u'value': u'weather'}], u'location': [{u'suggested': True, u'confidence': 0.9963185770228331, u'type': u'value', u'value': u'rome'}]}}
    '''
    print request
    context = request['context']
    entities = request['entities']
 
    loc = first_entity_value(entities, 'location')
    if loc:
        context['forecast'] = 'sunny'
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']
 
    return context

def get_score(request):
    print("GET SCORE")
    print(request)
    context = request['context']
    entities = request['entities']
    scoreType = first_entity_value(entities, 'bio_stat')
    print("SCORE TYPE: "+scoreType)
    context['stats_score'] = 'This is a test score'
    print(context)
    return context

actions = {
    'send': send,
    'getScore': get_score,
}

client = Wit(access_token=access_token, actions=actions)

def create_client(actions):
    print("In create client")
    print(actions)
    client = Wit(access_token=access_token, actions=actions)
    print(client)
    return client

def get_response(message, vactions=actions):
    print("GE RESPONSE")
    session_id = 'my-user-session-50'
    context0 = {}
    wit_client = create_client(actions)
    resp = wit_client.message(message)
    print("wit client messaged: "+message)
    context1 = wit_client.run_actions(session_id, message, context0)
    return context1


#client.interactive()
'''
resp = client.message('what is the weather in London?')
print('Yay, got Wit.ai response: ' + str(resp))

print("-----------")
session_id = 'my-user-session-42'
context0 = {}
context1 = client.run_actions(session_id, 'what is the weather in London?', context0)

print('-----The session state is now: ' + str(context1))
'''