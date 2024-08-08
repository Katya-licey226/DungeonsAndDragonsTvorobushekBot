import requests
import json

url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
token = 'None' # Надо получить токен в get_token.py
payload = json.dumps({
  "model": "GigaChat",
  "messages": [
    {
      "role": "system",
      "content": "Ты ведущий игры Подземелье и Драконы"
    },
    {
      "role": "user",
      "content": "Составь вступление к этой игре"
    }
  ],
  "n": 1,
  "stream": False,
  "update_interval": 0
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': f'Bearer {token}'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)