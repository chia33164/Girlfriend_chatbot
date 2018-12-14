import os
from bottle import Bottle, request, abort, static_file

from fsm import TocMachine

app = Bottle()

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']

machine = TocMachine(
    states=[
        'user',
        'birthday',
        'happy',
        'cry',
        'month',
        'angry'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'birthday',
            'conditions': 'is_going_to_birthday'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'angry',
            'conditions': 'is_going_to_angry'
        },
        {
            'trigger': 'go_back',
            'source': [
                'birthday',
                'angry'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@app.route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)

@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
