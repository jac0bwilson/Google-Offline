from twilio.twiml.messaging_response import MessagingResponse

def getRequest(request):
    request_json = request.get_json()
    request_args = request.args

    if request_json and 'Body' in request_json:
        body = request_json['Body']
    elif request_args and 'Body' in request_args:
        body = request_args['Body']
    else:
        body = 'Default'
    
    return reply(body)

def reply(text):
    resp = MessagingResponse()

    if "hello" in text.lower() or "hi" in text.lower():
        resp.message("Hello there!")
    else:
        resp.message("Boring default response")

    return str(resp)

