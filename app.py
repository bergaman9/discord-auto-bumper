import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "authorization": os.getenv("AUTH"),
}

turkoyto_payload = {"type": 2,"application_id":"302050872383242240","guild_id":"505520771603496971", "session_id": os.getenv("SESSION_ID"),"channel_id": "1030939187496632381", "data": {"version": "1051151064008769576", "id": "947088344167366698", "name": "bump","type": 1}}

while True:
    requests.post("https://discord.com/api/v9/interactions", headers=headers, json=turkoyto_payload)
    print("Türk Oyuncu Topluluğu öne çıkarıldı.")
    time.sleep(7200)
