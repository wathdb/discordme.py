import requests
from .utils import encode_to_url_format

def add_reaction(reaction, channel_id, message_id, token):
    for i in range(10):
        emoji = encode_to_url_format(reaction)
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/%40me'
        headers = {"authorization": token}
        response = requests.put(url, headers=headers)
        return response.status_code

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
    # Définir l'en-tête d'autorisation avec le token Discord
    headers = {
        'authorization': f'{token}',  # Token Discord
        'content-type': 'application/json',
    }

    # Créer le payload pour la requête PATCH avec les paramètres `text` et `emoji`
    data = {
        "custom_status": {
            "text": text,  # Le texte du statut
            "emoji_name": emoji  # L'emoji à afficher
        }
    }
    # Effectuer la requête PATCH
    response = requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=data)

def remove_status(token):
    url = "https://discord.com/api/v9/users/@me/settings-proto/1"
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }

    # Données de la requête
    data = {
        "settings": "WgoKCAoGb25saW5l"
    }
    # Envoie de la requête PATCH
    response = requests.patch(url, json=data, headers=headers)

def change_bio(token, new_bio):
    url = "https://discord.com/api/v9/users/%40me/profile"
    headers = {
         "Authorization": f"{token}",
         "Content-Type": "application/json"
    }

    # Données de la requête
    data = {
        "bio": new_bio
    }
# Envoie de la requête PATCH
    response = requests.patch(url, json=data, headers=headers)

def send_message(token, channel_id, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {"authorization": token}
    data = {"content": message}
    response = requests.post(url, json=data, headers=headers)
    return response.status_code
