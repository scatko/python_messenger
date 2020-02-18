import requests

name = input('Enter your name: ')
password = input('Enter your password: ')

while True:
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
