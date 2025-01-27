import requests

TOKEN = ''  # Токен твоего бота
CHAT_ID = ''  # chat_id твоей группы
message = 'Надеемся'  # Текст сообщения

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
params = {
    'chat_id': CHAT_ID,
    'text': message
}

response = requests.get(url, params=params)
print(response.json())  # Печатает ответ от Telegram API
