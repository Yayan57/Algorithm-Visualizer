import sys, pygame


def handle_menu():
    from menu import main_menu
    return main_menu()


def handle_play():
    from menu import play
    print("play")
    return play()


def handle_options():
    from menu import options
    return options()

def handle_sort():
    from menu import sort_menu
    return sort_menu()

def handle_search():
    from menu import search_menu
    return search_menu()


def handle_sorting_algorithm(algorithm):
    from sorting_algorithm import sorter
    return sorter(algorithm)


def game_loop():

    state_handlers = {
        "menu": handle_menu,
        "play": handle_play,
        "options": handle_options,
        "sort": handle_sort,
        "search": handle_search,
        "Bubble": lambda: handle_sorting_algorithm("Bubble"),
        "Insertion": lambda: handle_sorting_algorithm("Insertion"),
        "Quick": lambda: handle_sorting_algorithm("Quick"),
        "Merge": lambda: handle_sorting_algorithm("Merge"),
        "Selection": lambda: handle_sorting_algorithm("Selection"),

    }
    run = True
    state = "menu"
    while run:

        if state in state_handlers:
            state = state_handlers[state]()
            print(f"State: {state}, continuing loop")

        elif state == "quit":
            run = False

        else:
            print(f"Unknown state: {state}, ending loop")  # Debugging
            run = False


    pygame.quit()
    sys.exit()


game_loop()

""""
TODO:
0   make options to be used in options page (FPS(speed):text box, amount of rectangles: slider, and rectangle color: color picker)
0   allow text to be inputted and saved in text box
0   center the sorting algorithms based on the width of the menu
0   make a graph visualizer
0   i forgot what this was supposed to be TODO remember what i wanted to add to program
0   make the page for graph chooser before the play 

Finished:
X   add credit to me
X   add beta on bottom left
X   add images for cards
X   change main menu to actual good title
X   fix merge algorithm
X   fix menu 1st button press
X   make all rectangles green at end of quick sort
X   change window size in sorting algorithm to window height and width to make code more readable and updateable
"""""