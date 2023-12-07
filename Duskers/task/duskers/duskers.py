from enum import StrEnum, auto

TITLE = """\
+===========================================================================================+
  ######*   ##*  ##*  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*  ##*  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ######*    #####*   ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*         ##*     ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ##*         ##*     ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                                (Survival ASCII Strategy Game)
+===========================================================================================+\
"""

HUB = """\
__________(LOG)__________________________________________________(LOG)__________
+==============================================================================+
         $()$()$      |      $()$()$     |      $()$()$
        $$.....$$     |     $$.....$$    |     $$.....$$
         $$$$$$$      |      $$$$$$$     |      $$$$$$$
        $$$...$$$     |     $$$...$$$    |     $$$...$$$
        $~$$$$$~$     |     $~$$$$$~$    |     $~$$$$$~$
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+\
"""

MENU = """\
                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|\
"""

COMMAND = "Your command:\n"
NAME = "Enter your name:\n"

INVALID_INPUT = "Invalid input\n"
COMING_SOON = "Coming SOON! Thanks for playing!"


class GameState(StrEnum):
    initializing = auto()
    quitting = auto()

    title_screen = auto()
    main_menu = auto()
    play = auto()
    high_scores = auto()
    help = auto()


class Game:
    def __init__(self):
        self.state = GameState.initializing

    def set_state(self, new_state):
        self.state = new_state

    def start_game(self):
        self.state = GameState.main_menu
        self.loop()

    def loop(self):
        while self.state != GameState.quitting:
            if self.state == GameState.main_menu:
                self.main_menu()
            elif self.state == GameState.play:
                raise NotImplementedError()
            elif self.state == GameState.high_scores:
                self.high_scores()
            elif self.state == GameState.help:
                self.help()
        self.quit()

    def quit(self):
        print("Thanks for playing, bye!")

    def main_menu(self):
        print(TITLE)
        print("[Play]", "[High] Scores", "[Help]", "[Exit]", sep="\n", end="\n\n")

        while True:
            command = _get_input(COMMAND)

            if command == "play":
                self.state = GameState.play
            elif command == "high":
                self.state = GameState.high_scores
            elif command == "help":
                self.state = GameState.help
            elif command == "exit":
                self.state = GameState.quitting
            else:
                print(INVALID_INPUT)
                continue

            break

    def high_scores(self):
        print("No scores to display.", "    [Back]", end="\n\n")

        command = _get_input(COMMAND)

        while True:
            if command == "back":
                self.state = GameState.main_menu
                break
            else:
                print(INVALID_INPUT)
                command = _get_input(COMMAND)

    def help(self):
        print(COMING_SOON, end="\n\n")
        self.state = GameState.quitting


def _get_input(prompt, lowercase=True):
    command = input(prompt)
    if lowercase:
        command = command.lower()
    print()
    return command


def play():
    name = _get_input(NAME, False)

    print(f"Greetings, commander {name}!")
    print(
        "Are you ready to begin?",
        "    [Yes] [No] Return to Main [Menu]",
        sep="\n",
        end="\n\n",
    )
    while True:
        command = _get_input(COMMAND)

        if command == "yes":
            while True:
                print(HUB, end="\n\n")
                command = _get_input(COMMAND)

                if command == "ex":
                    print(COMING_SOON, end="\n\n")
                    return True
                elif command == "save":
                    print(COMING_SOON, end="\n\n")
                    return True
                elif command == "up":
                    print(COMING_SOON, end="\n\n")
                    return True
                elif command == "m":
                    print(MENU, sep="\n\n")

                    command = _get_input(COMMAND)

                    if command == "back":
                        pass
                    elif command == "main":
                        return False
                    elif command == "save":
                        print(COMING_SOON, end="\n\n")
                        return True
                    elif command == "exit":
                        print(COMING_SOON, end="\n\n")
                        return True

        elif command == "no":
            print("How about now.")
        elif command == "menu":
            return False
        else:
            print(INVALID_INPUT)


def main_menu():
    while True:
        print(TITLE)
        print("[Play]", "[High] Scores", "[Help]", "[Exit]", sep="\n", end="\n\n")

        while True:
            command = _get_input(COMMAND)

            if command == "play":
                exit_game = play()
                if exit_game:
                    return
                else:
                    break
            elif command == "high":
                print("No scores to display.", "    [Back]", end="\n\n")

                command = _get_input(COMMAND)

                while command != "back":
                    print(INVALID_INPUT)
                    command = _get_input(COMMAND)

                break

            elif command == "help":
                print(COMING_SOON, end="\n\n")
                return
            elif command == "exit":
                print("Thanks for playing, bye!")
                return
            else:
                print(INVALID_INPUT)


def main():
    Game().start_game()


if __name__ == "__main__":
    main()
