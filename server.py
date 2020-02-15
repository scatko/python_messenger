from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

users = {
    'Bielarusik': 'vasiliok',
    'Labusik': 'nugerai',
}

messages = [
    {
        'user': 'Bielarusik',
        'time': 1581725654.08043,
        'text': 'pryvit',
    },
    {
        'user': 'Labusik',
        'time': 1581725697.963234,
        'text': 'labas',
    },
]

@app.route('/')
def hello():
    return 'pryvit flask!!'

@app.route('/status')
def status():
    return {
        'status': True,
        'time': datetime.now().isoformat(),
        'users_count': len(users),
        'sent_messages': len(messages),
    }

@app.route('/history')
def history():
    return { 'messages': messages }

@app.route('/message', methods=['POST'])
def message():
    message = {
        'user': request.form['user'],
        'text': request.form['text'],
        'time': datetime.now().timestamp(),
    }
    messages.append(message)
    return {
        'ok': True,
    }

app.run()
