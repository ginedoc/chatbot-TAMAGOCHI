import imp
import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '374041751:AAHZKYm_SFiSDz7nZEsURqRyblxDnbTB_v0'
WEBHOOK_URL = 'https://5978efb8.ngrok.io/hook'

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
        'DIE',
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
            'source': 'state0', 
            'dest': 'state2', 
            'conditions': 'is_going_to_state2'
            },
        {
            'trigger': 'advance', 
            'source': 'state2', 
            'dest': 'state3', 
            'conditions': 'is_going_to_state3'
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
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state7',
            'conditions': 'is_going_to_state7',
            },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state8',
            'conditions': 'is_going_to_state8',
            },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state9',
            'conditions': 'is_going_to_state9',
            },
        # go back
        {     
            'trigger': 'go_back',
            'source': [
                'state1',
                'DIE',
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
                'source': 'state2',
                'dest': 'DIE',
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
    app.run()
