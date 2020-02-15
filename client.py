import requests
import time
from datetime import datetime

name = input('Enter your name: ')
password = input('Enter your password: ')

def request_messages(timestamp):
    return requests.get(
        'http://127.0.0.1:5000/history',
        params={'time': timestamp}
    ).json()['messages']

def print_messages(messages):
    for m in messages:
        print(datetime.fromtimestamp(float(m['time'])).isoformat(), m['user'])
        print(m['text'])
        print()

messages = request_messages(0)
print_messages(messages)

while True:
    last_time = datetime.now().timestamp()

    # New message
    message = input('Enter your message: ')

    req = requests.post(
        'http://127.0.0.1:5000/message',
        data={
            'user': name,
            'password': password,
            'text': message
        }
    )

    # Exit if not authorized
    if not req.json()['ok']:
        print(req.json()['status'])
        break

    # Request and print new messages
    messages = request_messages(last_time)
    print_messages(messages)

    time.sleep(1)
