import requests
import time
from datetime import datetime

name = input('Enter your name: ')
password = input('Enter your password: ')

while True:
    messages = requests.get('http://127.0.0.1:5000/history').json()['messages']
    for m in messages:
        print(datetime.fromtimestamp(m['time']).isoformat(), m['user'])
        print(m['text'])
        print()

    message = input('Enter your message: ')

    req = requests.post('http://127.0.0.1:5000/message', data={'user': name,
                                                         'password': password,
                                                         'text': message})

    # Exit if not authorized
    if not req.json()['ok']:
        print(req.json()['status'])
        break

    time.sleep(1)
