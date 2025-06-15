# 📸 Camera Hack Telegram Bot

> A simple yet sneaky Telegram bot that captures webcam photos periodically and sends them straight to your Telegram chat.  
> **Perfect for monitoring, remote surveillance, or just having some fun with your camera remotely!**

---

### ⚙️ Features

- Automatically captures an image from your default webcam every _X_ seconds (default 10 seconds).
- Sends the captured image to your specified Telegram chat using the Telegram Bot API.
- Runs in a separate thread so it won't block other tasks.
- Simple, lightweight, and easy to set up!

---

### 🚀 How to Use

1. **Create a Telegram bot** with [BotFather](https://t.me/BotFather) and get your API token.
2. **Get your Telegram chat ID** (can be your personal chat or a group chat).
3. Clone this repo:

    ```bash
    git clone https://github.com/ZAARA-Ziof/camera-hack-telegram-bot.git
    cd camera-hack-telegram-bot
    ```

4. Edit `camera_hack_bot.py`:

    ```python
    BOT_TOKEN = 'YOUR_BOT_TOKEN'
    CHAT_ID = 'YOUR_CHAT_ID'
    ```

5. Install dependencies:

    ```bash
    pip install opencv-python requests
    ```

6. Run the bot:

    ```bash
    python camera_hack_bot.py
    ```

---

### 🛠️ Customization

- Change the capture interval by modifying the `interval` parameter when creating the `CameraHackBot` instance.

Example:

```python
bot = CameraHackBot(BOT_TOKEN, CHAT_ID, interval=30)  # capture every 30 seconds
```

---

### ⚠️ Disclaimer

This tool is designed for educational and ethical usage only.  
Unauthorized access or monitoring of devices without permission is illegal and unethical.

Use responsibly.

---

### 🙋‍♂️ Author

**ZAARA Ziof**

Follow me on GitHub: [ZAARA-Ziof](https://github.com/zaaraZiof0)

---

### 📜 License

MIT License © 2025 ZAARA Ziof
