# Этот код рабочий но фиг знает какая магия там происходит и когда же пойму айограм
import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7216240691:AAGQus0Z0NqcbLy5USkpAFDkm3R5V1cTD68'
offset = -2
timeout = 10
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')