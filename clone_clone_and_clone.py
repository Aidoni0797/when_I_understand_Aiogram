import os
import requests
from dotenv import load_dotenv

# Загрузить токен из файла .env
load_dotenv()
token = os.getenv("GITHUB_TOKEN")
username = "..."

# Проверка наличия токена
if not token:
    raise ValueError("Токен GitHub не найден. Убедитесь, что он добавлен в .env файл.")

# Получаем список репозиториев пользователя
repos_url = f"https://api.github.com/users/{username}/repos"
headers = {'Authorization': f'token {token}'}
response = requests.get(repos_url, headers=headers)

if response.status_code != 200:
    raise Exception(f"Ошибка при получении репозиториев: {response.status_code} - {response.json()}")

repos = response.json()

# Для каждого репозитория получаем статистику
for repo in repos:
    repo_name = repo['name']
    traffic_url = f"https://api.github.com/repos/{username}/{repo_name}/traffic/clones"
    traffic_response = requests.get(traffic_url, headers=headers)

    if traffic_response.status_code != 200:
        print(f"Ошибка при получении статистики для {repo_name}: {traffic_response.status_code}")
        continue

    traffic_data = traffic_response.json()

    # Проверяем, есть ли данные по клонированиям
    if 'clones' in traffic_data:
        last_clone = traffic_data['clones'][-1] if traffic_data['clones'] else None
        if last_clone:
            print(f"Repo: {repo_name} was cloned on {last_clone['timestamp']}")
        else:
            print(f"Repo: {repo_name} has no cloning data.")
    else:
        print(f"Repo: {repo_name} - no traffic data available.")
