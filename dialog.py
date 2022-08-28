def take_300_bucks():
    print("You took 300 bucks")
    print("Теперь ты босс в качалке!")


def deny_300_bucks():
    print("You denied 300 bucks")
    print("Ты проиграл")



DIALOG_DICT = {
        "Привет!": {
            "Хочешь 300 bucks?": {
                "Да": {
                    "Ты получишь 300 bucks": take_300_bucks,
                    },
                "Нет": deny_300_bucks,
                },
            },
        }
