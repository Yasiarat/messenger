import requests
import time


host = 'http://127.0.0.1:1060'
url = '/send_messages'
login_url = '/login'

username = input('Введи своё имя:  ')
password = input('Введи своё имя:  ')
response = requests.post(
    host + login_url,
    json={'username': username, 'password': password}
)
while not response.json()['ok']:
    print('Неверный логин или пароль')
    print()
    username = input('Введи своё имя:  ')
    password = input('Введи своё имя:  ')
    response = requests.post(
        host + login_url,
        json={'username': username, 'password': password}
    )

print('Доступ разрешен.Welcome!')

while True:
    text = input('Введи текст сообщения:  ')

    response = requests.post(
        host + url,
        json = {'username':username, 'text':text}
    )
    print(response)
