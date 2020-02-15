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
    data = request.form
    user = data['user']
    password = data['password']
    text = data['text']

    # Simple authentication
    if user in users:
        if password != users[user]:
            return {
                'ok': False,
                'status': 'access denied',
            }
    else:
        users[user] = password

    # Save message if authenticated
    message = {
        'user': user,
        'text': text,
        'time': datetime.now().timestamp(),
    }
    messages.append(message)
    return {
        'ok': True,
    }

app.run()
