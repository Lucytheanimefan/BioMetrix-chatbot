from wit import Wit

access_token = "PNUPYT4U3IP2VCZRMQN3L443Q2QO375F"

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

actions = {
    'send': send,
    'getForecast': get_forecast,
}

client = Wit(access_token=access_token, actions=actions)

def create_client(actions):
	client = Wit(access_token=access_token, actions=actions)
	return client

def get_response(message, vactions=actions):
	session_id = 'my-user-session-42'
	context0 = {}
	wit_client = create_client(actions)
	resp = wit_client.message(message)
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