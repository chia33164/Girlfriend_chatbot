from bottle import route, run, request, abort, static_file
import os
from fsm import TocMachine


VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")
machine = TocMachine(
    states=[
        'user',
        'choose',
        'birthday',
        'angry',
        'sad',
        'month',
        'boring',
        'happy',
        'bad'
    ],
    transitions=[
        {'trigger': 'advance', 'source': 'user'    , 'dest': 'choose'  , 'conditions': 'is_going_to_choose'},
        {'trigger': 'advance', 'source': 'choose'  , 'dest': 'birthday', 'conditions': 'is_going_to_birthday'},
        {'trigger': 'advance', 'source': 'choose'  , 'dest': 'angry'   , 'conditions': 'is_going_to_angry'},
        {'trigger': 'advance', 'source': 'choose'  , 'dest': 'month'   , 'conditions': 'is_going_to_month'},
        {'trigger': 'advance', 'source': 'birthday', 'dest': 'happy'   , 'conditions': 'is_going_to_happy'},
        {'trigger': 'advance', 'source': 'birthday', 'dest': 'bad'     , 'conditions': 'is_going_to_bad'},
        {'trigger': 'advance', 'source': 'month'   , 'dest': 'happy'   , 'conditions': 'is_going_to_happy'},
        {'trigger': 'advance', 'source': 'month'   , 'dest': 'bad'     , 'conditions': 'is_going_to_bad'},
        {'trigger': 'advance', 'source': 'angry'   , 'dest': 'happy'   , 'conditions': 'is_going_to_happy'},
        {'trigger': 'advance', 'source': 'angry'   , 'dest': 'bad'     , 'conditions': 'is_going_to_bad'},
        {
            'trigger': 'go_back', 
            'source': [
                'user',
                'choose',
                'birthday',
                'angry',
                'sad',
                'month',
                'boring',
                'happy',
                'bad'
            ],      
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
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
    # print('REQUEST BODY: ')
    # print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        print(event)
        machine.advance(event)
    return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=6000, debug=True, reloader=True)
