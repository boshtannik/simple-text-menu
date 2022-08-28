from typing import Union
import os


# global settings variables to be changed in the menu
display_on: bool = True
brightness: float = 0.5  # must be limited form 0 to 1
volume: int = 25  # must be limited form 0 to 100
is_sound_on: bool = True
is_stereo: bool = True


QUIT_SYMBOLS = ["q", "Q", "quit", "exit"]


def brightness_up():
    global brightness
    brightness += 0.1
    if brightness > 1:
        brightness = 1
    print("Brightness is now {}".format(brightness))

def brightness_down():
    global brightness
    brightness -= 0.1
    if brightness < 0:
        brightness = 0
    print("Brightness is now {}".format(brightness))

def volume_up():
    global volume
    volume += 1
    if volume > 100:
        volume = 100
    print("Volume is now {}".format(volume))

def volume_down():
    global volume
    volume -= 1
    if volume < 0:
        volume = 0
    print("Volume is now {}".format(volume))

def toggle_sound():
    global is_sound_on
    is_sound_on = not is_sound_on
    print("Sound is now {}".format("on" if is_sound_on else "off"))

def toggle_stereo():
    global is_stereo
    is_stereo = not is_stereo
    print("Stereo is now {}".format("on" if is_stereo else "off"))

def toggle_display():
    global display_on
    display_on = not display_on
    print("Display is now {}".format("on" if display_on else "off"))


def add_quit_button():
    global QUIT_SYMBOLS
    import string
    answer = input("Do you want to add quit button to the list? (y/n) ")
    if answer.lower() in ("y", "yes"):
        new_quit_symbol = input("Enter quit symbol: ")
        if new_quit_symbol in string.ascii_letters:
            QUIT_SYMBOLS.append(new_quit_symbol)
            print(f"Symbol {new_quit_symbol} added to the list")
        else:
            print("Invalid symbol")


def remove_quit_button():
    global QUIT_SYMBOLS
    import string
    answer = input("Do you want to remove quit button from the list? (y/n) ")
    if answer.lower() in ("y", "yes"):
        new_quit_symbol = input("Enter quit symbol: ")
        if new_quit_symbol in QUIT_SYMBOLS:
            QUIT_SYMBOLS.remove(new_quit_symbol)
            print(f"Symbol {new_quit_symbol} removed from the list")
        else:
            print(f"Error! Symbol {new_quit_symbol} is not QUIT symbol")


def load_game_message():
    print("Loading game...")
    import time
    time.sleep(1)
    print("Game loaded")


def save_game_message():
    print("Saving game...")
    import time
    time.sleep(1)
    print("Game saved")


def new_game_message():
    print("New game...")
    import time
    time.sleep(1)
    print("Game started")



MAIN_MENU_DICT = {
        "Main menu": {
            "Game": {
                "New": new_game_message,
                "Load": load_game_message,
                "Save": save_game_message,
                },
            "Options": {
                "Display": {
                    "Toggle": toggle_display,
                    "Brightness up": brightness_up,
                    "Brightness down": brightness_down,
                    },
                "Sound": {
                    "Toggle": toggle_sound,
                    "Volume up": volume_up,
                    "Volume down": volume_down,
                    "Stereo": toggle_stereo,
                    },
                "Controls": {
                    "Key mappings": {
                        "Add quit button": add_quit_button,
                        "Remove quit button": remove_quit_button},
                    },
                },
            },
        }



def menu(menu_dict: dict):
    choice = None
    while choice not in QUIT_SYMBOLS:
        for i, item in enumerate(menu_dict):
            print(f"{i + 1}. {item}")

        choice = input(f"Enter your choice, or {QUIT_SYMBOLS[0]} to quit: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        mapped_choices = {str(i + 1): key for i, key in enumerate(menu_dict)}

        if choice not in mapped_choices:
            print("Invalid choice")
            continue

        key = mapped_choices[choice]
        if callable(menu_dict[key]):
            menu_dict[key]()
        else:
            menu(menu_dict[key])


if __name__ == "__main__":
    menu(MAIN_MENU_DICT)
