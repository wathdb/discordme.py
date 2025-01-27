import requests
import json
from json import loads
from time import sleep
from json import dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import discordme
import requests
from .utils import encode_to_url_format

def add_reaction(reaction, channel_id, message_id, token):
    for i in range(10):
        emoji = encode_to_url_format(reaction)
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/%40me'
        headers = {"authorization": token}
        response = requests.put(url, headers=headers)
        print(response.text)

def send_mp(message, user_channel_id, token):
    url = f'https://discord.com/api/v9/channels/{user_channel_id}/messages'
    headers = {"authorization": token}
    data = {"content": message}
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

def get_token(email, password):
    url = 'https://discord.com/api/v9/auth/login'
    data = {"login": email, "password": password, "undelete": False}
    response = requests.post(url, json=data)
    return response.json().get("token")

def change_status(token, text, emoji):
    headers = {
        'authorization': f'{token}',  # Token Discord
        'content-type': 'application/json',
    }
    data = {
        "custom_status": {
            "text": text,
            "emoji_name": emoji
        }
    }
    response = requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=data)

def remove_status(token):
    url = "https://discord.com/api/v9/users/@me/settings-proto/1"
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    data = {
        "settings": "WgoKCAoGb25saW5l"
    }
    response = requests.patch(url, json=data, headers=headers)

def change_bio(token, new_bio):
    url = "https://discord.com/api/v9/users/%40me/profile"
    headers = {
         "Authorization": f"{token}",
         "Content-Type": "application/json"
    }
    data = {
        "bio": new_bio
    }
    response = requests.patch(url, json=data, headers=headers)

def send_message(token, channel_id, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {"authorization": token}
    data = {"content": message}
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

def reply_mp(message, user_channel_id, message_id, token):
    url = f'https://discord.com/api/v9/channels/{user_channel_id}/messages'
    headers = {"authorization": token}
    data = {
        "content": message,
        "message_reference": {
            "channel_id": user_channel_id,
            "message_id": message_id
        }
    }
    response = requests.post(url, json=data, headers=headers)

def create_channel(name, guild_id, category_id, token):
    url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
    headers = {"authorization": token}
    data = {
        "name": name,
        "parent_id": category_id
    }
    response = requests.post(url, json=data, headers=headers)

def get_server_channels(server_id, token):
    url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
    headers = {"authorization": token}
    response = requests.get(url, headers=headers)
    channels = response.json()
    channels_info = {f"channel{i+1}": channel["id"] for i, channel in enumerate(channels)}
    return channels_info

def get_channel_messages(channel_id, token):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50'
    headers = {"authorization": token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        messages = response.json()
        formatted_messages = {
            f"message{i+1}": {
                "channel_id": channel_id,
                "message_id": message.get("id"),
                "content": message.get("content")
            }
            for i, message in enumerate(messages)
        }
        return formatted_messages
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return {}

def get_friends(token):
    url = f'https://discord.com/api/v9/users/@me/relationships'
    headers = {"authorization": token}
    response = requests.get(url, headers=headers)
    friends_data = json.loads(response.text)
    friends = [friend["id"] for friend in friends_data]
    print(friends)

def block_user(user_id, token):
    url = f'https://discord.com/api/v9/users/@me/relationships/{user_id}'
    headers = {"authorization": token}
    data = {
        "type": "2",
    }
    response = requests.put(url, json=data, headers=headers)

def unblock_user(user_id, token):
    url = f'https://discord.com/api/v9/users/@me/relationships/{user_id}'
    headers = {"authorization": token}
    response = requests.delete(url, headers=headers)

def typing(user_channel_id, token):
    url = f'https://discord.com/api/v9/channels/{user_channel_id}/typing'
    headers = {"authorization": token}
    response = requests.post(url, headers=headers)

def change_name(new_name, token):
    url = f'https://discord.com/api/v9/users/@me'
    headers = {"authorization": token}
    data = {"global_name": new_name}
    response = requests.patch(url, json=data, headers=headers)
    print(response.text)

def join_server(invite, token):
    url = f'https://discord.com/api/v9/invites/{invite}'
    headers = {"authorization": token}
    response = requests.post(url, headers=headers)
    print(response.text)
