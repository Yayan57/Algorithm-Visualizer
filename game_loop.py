import sys, pygame


def handle_menu():
    from menu import main_menu
    return main_menu()


def handle_play():
    from menu import play
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

def handle_traversal():
    from traversal_algorithms import run
    return run()


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
        "Traversal": handle_traversal,
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


Finished:
X   add credit to me
X   add beta on bottom left
X   add images for cards
X   change main menu to actual good title
X   fix merge algorithm
X   fix menu 1st button press
X   make all rectangles sorted at end of quick sort
X   change window size in sorting algorithm to window height and width to make code more readable and updateable
X   make the page for graph chooser before the play 
X   allow text to be inputted and saved in text box
X   center the sorting algorithms based on the width of the menu
X   figure out why lowering the max height of the rectangles breaks the program (ans: was running out of unique heights)
X   make options to be used in options page (FPS(speed):text box, amount of rectangles: slider, and rectangle color: drop down boxes )
X   make a traversal visualizer
X   split traversal algorithms to own pages
X   fix generate random maze function
X   get rid of draw own maze feature
X   create themes for search
X   add buttons for the sort algorithms so it isnt just words
X   add buttons for the search algorithms so it isnt just words
X   make play page look better
X   make options page look better
X   make sort graphs page look better
"""""