from twilio.twiml.messaging_response import MessagingResponse

def getRequest(request):
    request_json = request.get_json()
    request_args = request.args

    if request_json and 'body' in request_json:
        body = request_json['body']
    elif request_args and 'body' in request_args:
        body = request_args['body']
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

