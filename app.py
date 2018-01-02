import imp
import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine



API_TOKEN = '374041751:AAHZKYm_SFiSDz7nZEsURqRyblxDnbTB_v0'
WEBHOOK_URL = 'https://86cd79a0.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
#        'new',
#        'intro',
#        'option',
#        'optionA',
#        'optionB',
#        'optionC',

        # A

#        'bendong',
#        'fastfood',
#        'steak',
#        'bread',
#        'noodle',
#        'snack','
        'state0',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10',
        'state11',
        'state12',
        'state13',
        'state15',
        'state16',
    ],
    transitions=[
        # intro
        {
            'trigger': 'advance', 
            'source': 'state0', 
            'dest': 'state1', 
            'conditions': 'is_going_to_state1'
            },
        {
            'trigger': 'advance', 
            'source': [
                'state0',
                'state3',
                'state12'
                ],
            'dest': 'state2', 
            'conditions': 'is_going_to_state2'
            },
        # A
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state4',
            'conditions': 'is_going_to_state4',
            },
        {
            'trigger': 'advance', 
            'source': [
                'state4', 
                'state5',
                'state6',
                'state7',
                'state8',
                'state9',
                ],
            'dest': 'state10',
            'conditions': 'is_going_to_state10',
            },
        {
            'trigger': 'advance', 
            'source': [
                'state2',
                'state4', 
                'state5',
                'state6',
                'state7',
                'state8',
                'state9',
                ],
            'dest': 'state3',
            'conditions': 'is_going_to_state3',
            },
        # B
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state5',
            'conditions': 'is_going_to_state5',
            },
        # C
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state6',
            'conditions': 'is_going_to_state6',
            },
        # D
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state7',
            'conditions': 'is_going_to_state7',
            },
        # E
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state8',
            'conditions': 'is_going_to_state8',
            },
        # F
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state9',
            'conditions': 'is_going_to_state9',
            },
        # DIE
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state11',
            'conditions': 'is_going_to_state11',
                },
	{
	    'trigger': 'advance',
	    'source': 'state11',
	    'dest': 'state0',
	    'conditions': 'is_going_to_state0',
		},
        # option B
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
                },
        {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state13',
            'conditions': 'is_going_to_state13',
                },
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state15',
            'conditions': 'is_going_to_state15',
                },
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state16',
            'conditions': 'is_going_to_state16',
                },
        # go back
        {     
            'trigger': 'go_back',
            'source': [
                'state1',
                ],
            'dest': 'state0'
            },
        {
            'trigger': 'go_back',
            'source': 'state10',
            'dest': 'state2',
            },
        {
            'trigger': 'go_back',
            'source': [
                'state15',
                'state16',
                ],
            'dest': 'state12'
                },
    ],
    initial = 'state0',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')



if __name__ == "__main__":
    _set_webhook()
    app.run(debug=True)
