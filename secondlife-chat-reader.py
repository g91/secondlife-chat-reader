# SecondLifeChatReader.py
# This script monitors and reads aloud new chat messages from a Second Life chat log file.

import time
import re
import pyttsx3

class SecondLifeChatReader:
    def __init__(self, filename):
        self.filename = filename
        self.last_line = ''
        self.engine = pyttsx3.init()
        self.timestamp_pattern = re.compile(r'^\s*\[[^\]]+\]\s*')

    def strip_timestamp(self, line):
        return self.timestamp_pattern.sub('', line).strip()

    def read_last_line(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    return lines[-1].strip()
        except Exception as e:
            print(f"Error reading Second Life chat file: {e}")
        return ''

    def check_and_read_new_message(self):
        current_last_line = self.read_last_line()
        if current_last_line and current_last_line != self.last_line:
            stripped_line = self.strip_timestamp(current_last_line)
            if stripped_line:
                if "HTTP" not in stripped_line.upper():
                    print(f"New Second Life message: {stripped_line}")
                    self.engine.say(stripped_line)
                    self.engine.runAndWait()
                else:
                    print(f"Skipped Second Life message (contains HTTP): {stripped_line}")
            self.last_line = current_last_line

def monitor_secondlife_chat(filename):
    reader = SecondLifeChatReader(filename)
    
    print(f"Monitoring Second Life chat file: {filename}")
    print("Press Ctrl+C to stop the Second Life chat reader.")
    
    try:
        while True:
            reader.check_and_read_new_message()
            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        print("\nStopping the Second Life chat monitor.")

if __name__ == "__main__":
    sl_chat_file = r"C:\Users\theru\AppData\Roaming\SecondLife\theevildomo_resident\chat.txt"
    monitor_secondlife_chat(sl_chat_file)
