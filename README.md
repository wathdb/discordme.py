
# 🎉 DiscordMe 🐍  

**Une bibliothèque Python puissante et sécurisée pour interagir avec l'API Discord en toute simplicité, tout en évitant les bannissements et restrictions de compte.**  

---

## 🚀 **Fonctionnalités clés**  
✅ **Connexion sécurisée** avec vos identifiants Discord pour récupérer votre token automatiquement.  
✅ Envoyez des **messages privés**, des **messages dans des salons**, ou encore des **réactions aux messages**.  
✅ Modifiez rapidement votre **statut personnalisé**, votre **bio**, ou même supprimez votre statut actuel.  
✅ **Sécurité intégrée** : minimisez les risques de bannissement grâce à des appels conformes aux bonnes pratiques de l'API Discord.  
✅ Rapide, léger, et conçu pour une intégration facile dans vos projets.  

---

## ✨ **Pourquoi choisir DiscordMe ?**  

Contrairement à d'autres bibliothèques similaires :  
- 🎯 **Sûreté** : Nos appels à l'API Discord sont optimisés pour réduire les risques de bannissement et maintenir votre compte actif.  
- ⚡ **Performance** : Aucune surcharge, juste ce dont vous avez besoin pour interagir avec l'API Discord efficacement.  
- 🔒 **Respect des pratiques de Discord** : Nous mettons un point d'honneur à suivre les règles et limitations de l'API Discord.

---

## 📦 **Installation**  

Installez DiscordMe directement via **pip** :  
```bash
pip install discordme.py
```

---

## 📄 **Exemples d'utilisation**  

### 🔐 **Se connecter avec vos identifiants Discord**  
```python
from discordme import get_token

email = "email@exemple.com"
password = "votre_mot_de_passe"
token = get_token(email, password)

print(f"Votre token : {token}")
```

### ✉️ **Envoyer un message dans un salon ou en MP**  
```python
from discordme import send_message

token = "votre_token"
channel_id = "123456789012345678"  # ID du salon ou de l'utilisateur (MP)
message = "Salut tout le monde ! 🚀"

status_code = send_message(token, channel_id, message)
if status_code == 200:
    print("Message envoyé avec succès ! 🎉")
else:
    print("Échec de l'envoi du message. 😢")
```

### 😍 **Ajouter une réaction à un message**  
```python
from discordme import add_reaction

reaction = "❤️"  # Emoji à ajouter
channel_id = "123456789012345678"  # ID du salon
message_id = "987654321098765432"  # ID du message
token = "votre_token"

status_code = add_reaction(reaction, channel_id, message_id, token)
if status_code == 204:
    print("Réaction ajoutée avec succès ! 🎉")
else:
    print("Impossible d'ajouter la réaction. 😢")
```

### ✏️ **Changer votre statut personnalisé**  
```python
from discordme import change_status

token = "votre_token"
text = "Disponible pour coder 🐍"
emoji = "💻"

change_status(token, text, emoji)
print("Statut personnalisé mis à jour ! 🎯")
```

### 📝 **Modifier votre bio Discord**  
```python
from discordme import change_bio

token = "votre_token"
new_bio = "Développeur passionné de Python et Discord API 🚀"

change_bio(token, new_bio)
print("Bio mise à jour avec succès ! ✅")
```

---

## 🛡️ **Sécurité et conformité**  
💡 **Important** : Discord interdit certaines pratiques pouvant entraîner le bannissement de votre compte.  
Avec **DiscordMe**, nous :  
- Gérons les requêtes de manière **conforme aux limitations de Discord** (rate limiting).  
- Minimisons les risques liés à l'utilisation des tokens Discord grâce à une implémentation optimisée.  
- Encourageons l'utilisation de méthodes respectant les [Conditions d'utilisation de Discord](https://discord.com/terms).  

---

## 🛠️ **Contribuer**  

Les contributions sont les bienvenues ! 🎉  
1. Clonez le repo :  
   ```bash
   git clone https://github.com/votre-utilisateur/DiscordMe.git
   ```  
2. Installez les dépendances de développement :  
   ```bash
   pip install -r requirements-dev.txt
   ```  
3. Proposez vos modifications via une pull request.  

---

## 📬 **Contact & Support**  
💬 Vous avez des questions ou des suggestions ? Contactez-moi directement sur Discord : **wathd_**.  

---

## 🌟 **Donnez une étoile ⭐**  
Si ce projet vous plaît, pensez à lui donner une étoile sur GitHub pour le soutenir ! 😊  

---

**Créé avec ❤️ par [wathD]**
```
