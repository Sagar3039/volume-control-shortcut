import keyboard
import ctypes
import time

# Windows key code constants
VK_VOLUME_UP = 0xAF
VK_VOLUME_DOWN = 0xAE
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002

# Volume key press simulation
def press_key(key_code):
    ctypes.windll.user32.keybd_event(key_code, 0, KEYEVENTF_EXTENDEDKEY, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0)

# Hotkey bindings
keyboard.add_hotkey("alt+a", lambda: press_key(VK_VOLUME_DOWN))
keyboard.add_hotkey("alt+d", lambda: press_key(VK_VOLUME_UP))

print("System volume control active! Press ESC to quit.")
keyboard.wait("esc")
