from telethon.sync import TelegramClient
import json
# Вставь свои данные
api_id = "..."
api_hash = "..."
group_username = "..."

# Подключаемся
with TelegramClient("session_name", api_id, api_hash) as client:
    participants = client.get_participants(group_username)
    participants_data = []
    # Выводим список участников
    for user in participants:
        participants_data.append({
            "user_id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
        })
    with open('participants.json', 'w', encoding='utf-8') as f:
        json.dump(participants_data, f, ensure_ascii=False, indent=4)
