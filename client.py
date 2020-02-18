import requests
from time import sleep
from datetime import datetime

last_message_time = 0

while True:
    # Request and print new messages
    response = requests.get(
        'http://127.0.0.1:5000/history',
        params={'time': last_message_time}
    )

    messages = response.json()['messages']
    for m in messages:
        print(datetime.fromtimestamp(float(m['time'])).isoformat(), m['user'])
        print(m['text'])
        print()
        last_message_time = m['time']

    sleep(1)
