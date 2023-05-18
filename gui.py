import PySimpleGUI as sg


def create_gui():
    layout = [
        [sg.Text("Select Algorithm Type:")],
        [sg.Radio("Minimax", "algorithm", default=True, key="-MINIMAX-")],
        [sg.Radio("Alpha-Beta", "algorithm", key="-ALPHA_BETA-")],
        [sg.Text("Select Difficulty Level:")],
        [sg.Radio("Easy", "difficulty", default=True, key="-EASY-")],
        [sg.Radio("Medium", "difficulty", key="-MEDIUM-")],
        [sg.Radio("Hard", "difficulty", key="-HARD-")],
        [sg.Button("Start Game", key="-START-")],
    ]

    window = sg.Window("Connect Four Game", layout, finalize=True)
    return window


def get_selected_options(values):
    algorithm_type = "Minimax" if values["-MINIMAX-"] else "Alpha-Beta"
    difficulty_level = "Easy" if values["-EASY-"] else "Medium" if values["-MEDIUM-"] else "Hard"
    return algorithm_type, difficulty_level


def run():
    window = create_gui()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "-START-":
            algorithm_type, difficulty_level = get_selected_options(values)
            # Use the selected options to start the game with the chosen algorithm and difficulty
            if (algorithm_type == "Minimax"):
                if (difficulty_level == "Easy"):
                    window.close()

                    return 0, 1
                elif (difficulty_level == "Medium"):
                    window.close()

                    return 0, 2

                else:
                    window.close()

                    return 0, 5

            else:
                if (difficulty_level == "Easy"):
                    window.close()

                    return 1, 1

                elif (difficulty_level == "Medium"):
                    window.close()

                    return 1, 2
                else:
                    window.close()

                    return 1, 5
