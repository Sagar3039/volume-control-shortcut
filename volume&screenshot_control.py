import keyboard
import ctypes
import time
import os
from datetime import datetime
from PIL import ImageGrab

# Send Windows volume keys
def send_volume_key(key_code):
    APPCOMMAND_VOLUME_UP = 0x0a
    APPCOMMAND_VOLUME_DOWN = 0x09

    hwnd = ctypes.windll.user32.GetForegroundWindow()
    message = 0x319
    wparam = hwnd
    lparam = (key_code << 16)
    ctypes.windll.user32.SendMessageW(hwnd, message, wparam, lparam)

# Screenshot folder
screenshot_dir = r"C:\Users\Sagar\Pictures\Screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
    image = ImageGrab.grab()
    image.save(filename)
    print(f"Screenshot saved: {filename}")

# Hotkey bindings
keyboard.add_hotkey("alt+a", lambda: send_volume_key(0x09))  # Volume Down
keyboard.add_hotkey("alt+d", lambda: send_volume_key(0x0a))  # Volume Up
keyboard.add_hotkey("alt+s", take_screenshot)                # Take Screenshot

print("Volume control and screenshot tool running... Press ESC to quit.")
keyboard.wait("esc")
