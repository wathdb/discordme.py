# 🎉 DiscordMe 🐍  

**A powerful and secure Python library to interact effortlessly with the Discord API while avoiding account bans and restrictions.**  

---

## 🚀 **Key Features**  
✅ **Secure connection** with your Discord credentials to automatically retrieve your token.  
✅ Send **private messages**, **channel messages**, or even **reactions to messages**.  
✅ Quickly update your **custom status**, **bio**, or even remove your current status.  
✅ **Integrated security**: minimize ban risks with calls optimized for Discord's best practices.  
✅ Fast, lightweight, and designed for seamless integration into your projects.  

---

## ✨ **Why Choose DiscordMe?**  

Unlike similar libraries:  
- 🎯 **Safety**: Our Discord API calls are optimized to reduce ban risks and keep your account active.  
- ⚡ **Performance**: No unnecessary overhead, just what you need to interact efficiently with the Discord API.  
- 🔒 **Respect for Discord's guidelines**: We prioritize adhering to Discord API rules and limitations.  

---

## 📦 **Installation**  

Install DiscordMe directly via **pip**:  
```bash
pip install discordme.py
```

---

## 📄 **Usage Examples**  

### 🔐 **Log in with your Discord credentials**  
```python
from discordme import get_token

email = "email@example.com"
password = "your_password"
token = get_token(email, password)

print(f"Your token: {token}")
```

### ✉️ **Send a message in a channel or DM**  
```python
from discordme import send_message

token = "your_token"
channel_id = "123456789012345678"  # Channel or user ID (DM)
message = "Hello everyone! 🚀"

status_code = send_message(token, channel_id, message)
if status_code == 200:
    print("Message sent successfully! 🎉")
else:
    print("Failed to send the message. 😢")
```

### 😍 **Add a reaction to a message**  
```python
from discordme import add_reaction

reaction = "❤️"  # Emoji to add
channel_id = "123456789012345678"  # Channel ID
message_id = "987654321098765432"  # Message ID
token = "your_token"

status_code = add_reaction(reaction, channel_id, message_id, token)
if status_code == 204:
    print("Reaction added successfully! 🎉")
else:
    print("Unable to add the reaction. 😢")
```

### ✏️ **Change your custom status**  
```python
from discordme import change_status

token = "your_token"
text = "Available for coding 🐍"
emoji = "💻"

change_status(token, text, emoji)
print("Custom status updated! 🎯")
```

### 📝 **Update your Discord bio**  
```python
from discordme import change_bio

token = "your_token"
new_bio = "Passionate Python and Discord API developer 🚀"

change_bio(token, new_bio)
print("Bio successfully updated! ✅")
```

---

## 🛡️ **Security and Compliance**  
💡 **Important**: Discord prohibits certain practices that can lead to account bans.  
With **DiscordMe**, we:  
- Handle requests **in compliance with Discord's rate-limiting rules**.  
- Minimize risks associated with Discord token usage through optimized implementation.  
- Encourage methods that respect Discord's [Terms of Service](https://discord.com/terms).  

---

## 🛠️ **Contribute**  

Contributions are welcome! 🎉  
1. Clone the repo:  
   ```bash
   git clone https://github.com/wathdb/discordme.py.git
   ```  
2. Install the development dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Submit your changes via a pull request.  

---

## 📬 **Contact & Support**  
💬 Have questions or suggestions? Contact me directly on Discord: **wathd_**.  

---

## 🌟 **Give a Star ⭐**  
If you like this project, consider giving it a star on GitHub to support it! 😊  

---

**Created with ❤️ by [wathD]**
