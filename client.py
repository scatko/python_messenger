import requests
import time
from datetime import datetime

name = input('Enter your name: ')

while True:
    messages = requests.get('http://127.0.0.1:5000/history').json()['messages']
    print(messages)
    for m in messages:
        print(m)
        print(datetime.fromtimestamp(m['time']).isoformat(), m['user'])
        print(m['text'])
        print()

    message = input('Enter your message: ')

    requests.post('http://127.0.0.1:5000/message', data={'user': name, 'text':
                                                         message})

    time.sleep(1)
