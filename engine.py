QUIT_SYMBOLS = ["q", "Q", "quit", "exit"]



def menu(menu_dict: dict):
    choice = None
    while choice not in QUIT_SYMBOLS:
        for i, item in enumerate(menu_dict):
            print(f"{i + 1}. {item}")

        choice = input(f"Enter your choice, or {QUIT_SYMBOLS[0]} to quit: ")

        mapped_choices = {str(i + 1): key for i, key in enumerate(menu_dict)}

        print(chr(27) + "[2J")
        if choice not in mapped_choices:
            print("Invalid choice")
            continue

        key = mapped_choices[choice]
        if callable(menu_dict[key]):
            menu_dict[key]()
        else:
            menu(menu_dict[key])

