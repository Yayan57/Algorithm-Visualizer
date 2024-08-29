import pygame, sys, sorting_algorithm

import traversal_algorithms
from tools import Button, Slider, DropDown
from traversal_algorithms import algorithm

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
base_font = pygame.font.Font(None, 45)
MENU_BG = pygame.image.load("assets/dark-gradient-background-6bly12umg2d4psr2.jpg")
OPTIONS_BG = pygame.image.load("assets/white-gradient-background-o0tqqpgs66oz4rfr.jpg")
PLAY_BG = pygame.image.load("assets/gradient-colour-background-illustration-free-vector.jpg")
SORT_BG = pygame.image.load("assets/dark-brown-gradient-background-dark-red-brown-background-pattern-for-website-landing-pages-blurred-template-vector.jpg")
SEARCH_BG = pygame.image.load("assets/papers.co-sk64-dark-green-blur-gradation-23-wallpaper.jpg")


def get_font(size):
    return pygame.font.Font(None, size)


def sort_menu():
    pygame.display.set_caption("Sorting Algorithms")

    while True:
        SORT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(SORT_BG, (0, 0))

        SORT_TEXT = get_font(45).render("Choose a sorting algorithm", True, "#FFFFFF")
        SORT_RECT = SORT_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(SORT_TEXT, SORT_RECT)

        SORT_BUBBLE = Button(image=pygame.image.load("assets/Bubble.png"), pos=(150, 400), text_input="", font=get_font(75), base_color="White",
                             hovering_color="Green")

        SORT_BUBBLE.changeColor(SORT_MOUSE_POS)
        SORT_BUBBLE.update(SCREEN)

        SORT_INSERTION = Button(image=pygame.image.load("assets/insertion.webp"), pos=(400, 400), text_input="", font=get_font(75),
                                base_color="White",
                                hovering_color="Green")

        SORT_INSERTION.changeColor(SORT_MOUSE_POS)
        SORT_INSERTION.update(SCREEN)

        SORT_QUICK = Button(image=pygame.image.load("assets/quick.png"), pos=(650, 400), text_input="", font=get_font(75), base_color="White",
                            hovering_color="Green")

        SORT_QUICK.changeColor(SORT_MOUSE_POS)
        SORT_QUICK.update(SCREEN)

        SORT_MERGE = Button(image=pygame.image.load("assets/merge.png"), pos=(900, 400), text_input="", font=get_font(75), base_color="White",
                            hovering_color="Green")

        SORT_MERGE.changeColor(SORT_MOUSE_POS)
        SORT_MERGE.update(SCREEN)

        SORT_SELECTION = Button(image=pygame.image.load("assets/selection.png"), pos=(1150, 400), text_input="", font=get_font(75),
                                base_color="White",
                                hovering_color="Green")

        SORT_SELECTION.changeColor(SORT_MOUSE_POS)
        SORT_SELECTION.update(SCREEN)

        SORT_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75),
                           base_color="White",
                           hovering_color="Green")

        SORT_BACK.changeColor(SORT_MOUSE_POS)
        SORT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SORT_BUBBLE.checkForInput(SORT_MOUSE_POS):
                    return "Bubble"
                if SORT_INSERTION.checkForInput(SORT_MOUSE_POS):
                    return "Insertion"
                if SORT_QUICK.checkForInput(SORT_MOUSE_POS):
                    return "Quick"
                if SORT_MERGE.checkForInput(SORT_MOUSE_POS):
                    return "Merge"
                if SORT_SELECTION.checkForInput(SORT_MOUSE_POS):
                    return "Selection"
                if SORT_BACK.checkForInput(SORT_MOUSE_POS):
                    return "play"

        pygame.display.update()


def search_menu():
    pygame.display.set_caption("Graph search algorithms")

    while True:
        SORT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(SEARCH_BG, (0, 0))

        SEARCH_TEXT = get_font(45).render("Choose a search algorithm", True, "#FFFFFF")
        SEARCH_RECT = SEARCH_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(SEARCH_TEXT, SEARCH_RECT)

        INST_TEXT = get_font(45).render("Space to start, and R to reset when search is done.", True, "#FFFFFF")
        INST_RECT = INST_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(INST_TEXT, INST_RECT)

        SEARCH_DFS = Button(image=pygame.image.load("assets/dfs.png"), pos=(250, 400), text_input="", font=get_font(75), base_color="Black",
                             hovering_color="Green")


        SEARCH_DFS.changeColor(SORT_MOUSE_POS)
        SEARCH_DFS.update(SCREEN)

        SEARCH_BFS = Button(image=pygame.image.load("assets/bfs.png"), pos=(500, 400), text_input="", font=get_font(75),
                                base_color="Black",
                                hovering_color="Green")

        SEARCH_BFS.changeColor(SORT_MOUSE_POS)
        SEARCH_BFS.update(SCREEN)

        SEARCH_DIJKSTRA = Button(image=pygame.image.load("assets/dijkstra.png"), pos=(750, 400), text_input="", font=get_font(75), base_color="Black",
                            hovering_color="Green")

        SEARCH_DIJKSTRA.changeColor(SORT_MOUSE_POS)
        SEARCH_DIJKSTRA.update(SCREEN)

        SEARCH_ASTAR = Button(image=pygame.image.load("assets/astar.png"), pos=(1000, 400), text_input="", font=get_font(75), base_color="Black",
                            hovering_color="Green")

        SEARCH_ASTAR.changeColor(SORT_MOUSE_POS)
        SEARCH_ASTAR.update(SCREEN)

        SEARCH_BACK = Button(image=None, pos=(640, 650), text_input="BACK", font=get_font(75),
                           base_color="White",
                           hovering_color="Green")

        SEARCH_BACK.changeColor(SORT_MOUSE_POS)
        SEARCH_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SEARCH_DFS.checkForInput(SORT_MOUSE_POS):
                    traversal_algorithms.algorithm = "DFS"
                if SEARCH_BFS.checkForInput(SORT_MOUSE_POS):
                    traversal_algorithms.algorithm = "BFS"
                if SEARCH_DIJKSTRA.checkForInput(SORT_MOUSE_POS):
                    traversal_algorithms.algorithm = "DIJKSTRA"
                if SEARCH_ASTAR.checkForInput(SORT_MOUSE_POS):
                    traversal_algorithms.algorithm = "ASTAR"
                if SEARCH_BACK.checkForInput(SORT_MOUSE_POS):
                    return "play"
                return "Traversal"

        pygame.display.update()



def play():
    pygame.display.set_caption("Play")

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(PLAY_BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Choose a type of algorithm", True, "#FFFFFF")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_SORT = Button(image=pygame.image.load("assets/sort.png"), pos=(490, 400), text_input="", font=get_font(75), base_color="White",
                           hovering_color="Green")

        PLAY_SORT.changeColor(PLAY_MOUSE_POS)
        PLAY_SORT.update(SCREEN)

        PLAY_SEARCH = Button(image=pygame.image.load("assets/search.png"), pos=(790, 400), text_input="", font=get_font(75), base_color="White",
                             hovering_color="Green")

        PLAY_SEARCH.changeColor(PLAY_MOUSE_POS)
        PLAY_SEARCH.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75),
                           base_color="White",
                           hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_SORT.checkForInput(PLAY_MOUSE_POS):
                    return "sort"
                if PLAY_SEARCH.checkForInput(PLAY_MOUSE_POS):
                    return "search"
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    return "menu"

        pygame.display.update()


def options():
    # variables
    pygame.display.set_caption("Options")

    input_box_speed = pygame.Rect(900, 250, 140, 40)
    input_text_speed = ""
    active_speed = False

    input_box_checkpoint_speed = pygame.Rect(230, 400, 140, 40)
    input_text_checkpoint_speed = ""
    active_checkpoint_speed = False

    MIN = 5
    MAX = 55
    max_rectangles = (sorting_algorithm.WINDOW_WIDTH // sorting_algorithm.RECT_WIDTH) - 5

    slider = Slider((970, 225), (140, 30), .5, 0, 100)

    # Slider for checkpoints (ranges from 1 to 9)
    slider_checkpoint = Slider((300, 375), (140, 30), 1, 2, 9)

    COLOR_INACTIVE = (100, 80, 255)
    COLOR_ACTIVE = (100, 200, 255)
    COLOR_LIST_INACTIVE = (255, 100, 100)
    COLOR_LIST_ACTIVE = (255, 150, 150)

    # dropdown box
    OPTIONS_THEME_COLOR_SORT = DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        900, 160, 140, 40,
        pygame.font.SysFont(None, 30),
        "Select Theme", ["Normal", "Dark", "Light", "Dusk", "Spring", "Summer", "Fall", "Winter"]
    )

    OPTIONS_THEME_COLOR_SEARCH = DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        230, 310, 140, 40,
        pygame.font.SysFont(None, 30),
        "Select Theme", ["Normal", "Dark", "Light", "Dusk", "Spring", "Summer", "Fall", "Winter"]
    )

    current_theme_sort = sorting_algorithm.THEME
    current_theme_search = traversal_algorithms.THEME

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(OPTIONS_BG, (0, 0))

        # title
        OPTIONS_TEXT = get_font(45).render("Options", True, "#000000")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # FPS text
        OPTIONS_FPS = get_font(45).render(f"Sort Speed: {sorting_algorithm.FPS}", True, "#000000")
        OPTIONS_FPS_RECT = OPTIONS_FPS.get_rect(center=(330, 275))
        SCREEN.blit(OPTIONS_FPS, OPTIONS_FPS_RECT)

        # Get the rounded value from the slider
        slider_value = round(slider.get_value())
        num_rectangles = max(MIN, min(MAX, int((slider_value / 100) * max_rectangles)))  # Scale between 5 and max_rectangles

        # slider text
        OPTIONS_NRECTANGLES = get_font(45).render(f"Number of Rectangles: {num_rectangles}", True, "#000000")
        OPTIONS_NRECTANGLES_RECT = OPTIONS_NRECTANGLES.get_rect(center=(415, 225))
        SCREEN.blit(OPTIONS_NRECTANGLES, OPTIONS_NRECTANGLES_RECT)

        # Render slider
        slider.move_slider(OPTIONS_MOUSE_POS)
        slider.render(SCREEN)

        # Get the rounded value from the checkpoint slider
        checkpoint_value = round(slider_checkpoint.get_value())

        # Checkpoints text
        OPTIONS_CHECKPOINTS = get_font(45).render(f"Number of Checkpoints: {checkpoint_value}", True, "#000000")
        OPTIONS_CHECKPOINTS_RECT = OPTIONS_CHECKPOINTS.get_rect(center=(850, 375))
        SCREEN.blit(OPTIONS_CHECKPOINTS, OPTIONS_CHECKPOINTS_RECT)

        # Checkpoints speed text
        OPTIONS_CHECKPOINTS_SPEED = get_font(45).render(f"Search Speed: {traversal_algorithms.FPS}", True, "#000000")
        OPTIONS_CHECKPOINTS_RECT_SPEED = OPTIONS_CHECKPOINTS_SPEED.get_rect(center=(910, 425))
        SCREEN.blit(OPTIONS_CHECKPOINTS_SPEED, OPTIONS_CHECKPOINTS_RECT_SPEED)

        # Render checkpoint slider
        slider_checkpoint.move_slider(OPTIONS_MOUSE_POS)
        slider_checkpoint.render(SCREEN)

        # back button
        OPTIONS_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Render input box for speed
        text_surface_speed = get_font(40).render(input_text_speed, True, pygame.Color('black'))
        SCREEN.blit(text_surface_speed, input_box_speed.topleft)
        pygame.draw.rect(SCREEN, pygame.Color('gray'), input_box_speed, 2)

        # Render input box for checkpoints speed
        text_surface_checkpoint_speed = get_font(40).render(input_text_checkpoint_speed, True, pygame.Color('black'))
        SCREEN.blit(text_surface_checkpoint_speed, input_box_checkpoint_speed.topleft)
        pygame.draw.rect(SCREEN, pygame.Color('gray'), input_box_checkpoint_speed, 2)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    sorting_algorithm.num_rectangles = num_rectangles
                    sorting_algorithm.THEME = current_theme_sort
                    traversal_algorithms.THEME = current_theme_search
                    traversal_algorithms.num_of_checkpoints = checkpoint_value
                    return "menu"
                if input_box_speed.collidepoint(event.pos):
                    active_speed = True
                    active_checkpoint_speed = False
                elif input_box_checkpoint_speed.collidepoint(event.pos):
                    active_checkpoint_speed = True
                    active_speed = False
                else:
                    active_speed = False
                    active_checkpoint_speed = False

                slider.check_mouse_down(OPTIONS_MOUSE_POS)
                slider_checkpoint.check_mouse_down(OPTIONS_MOUSE_POS)

            if event.type == pygame.MOUSEBUTTONUP:
                slider.check_mouse_up()
                slider_checkpoint.check_mouse_up()

            if event.type == pygame.KEYDOWN:
                if active_speed:
                    if event.key == pygame.K_BACKSPACE:
                        input_text_speed = input_text_speed[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_text_speed.isdigit() and len(input_text_speed) < 8:
                            sorting_algorithm.FPS = int(input_text_speed)
                            input_text_speed = ""
                    elif event.unicode.isdigit():
                        if len(input_text_speed) < 7:
                            input_text_speed += event.unicode

                if active_checkpoint_speed:
                    if event.key == pygame.K_BACKSPACE:
                        input_text_checkpoint_speed = input_text_checkpoint_speed[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_text_checkpoint_speed.isdigit() and len(input_text_checkpoint_speed) < 8:
                            traversal_algorithms.FPS = int(input_text_checkpoint_speed)
                            input_text_checkpoint_speed = ""
                    elif event.unicode.isdigit():
                        if len(input_text_checkpoint_speed) < 7:
                            input_text_checkpoint_speed += event.unicode

        theme_option_sort = OPTIONS_THEME_COLOR_SORT.update(event_list)
        if theme_option_sort >= 0:
            current_theme_sort = OPTIONS_THEME_COLOR_SORT.options[theme_option_sort]
            OPTIONS_THEME_COLOR_SORT.main = current_theme_sort
        OPTIONS_THEME_COLOR_SORT.draw(SCREEN)

        # theme_text
        OPTIONS_THEME_SORT = get_font(45).render(f"Sort theme: {str(current_theme_sort)}", True, "#000000")
        OPTIONS_THEME_SORT_RECT = OPTIONS_THEME_SORT.get_rect(center=(365, 175))
        SCREEN.blit(OPTIONS_THEME_SORT, OPTIONS_THEME_SORT_RECT)

        theme_option_search = OPTIONS_THEME_COLOR_SEARCH.update(event_list)
        if theme_option_search >= 0:
            current_theme_search = OPTIONS_THEME_COLOR_SEARCH.options[theme_option_search]
            OPTIONS_THEME_COLOR_SEARCH.main = current_theme_search
        OPTIONS_THEME_COLOR_SEARCH.draw(SCREEN)

        # theme_text
        OPTIONS_THEME_SEARCH = get_font(45).render(f"Search theme: {str(current_theme_search)}", True, "#000000")
        OPTIONS_THEME_SEARCH_RECT = OPTIONS_THEME_SEARCH.get_rect(center=(880, 325))
        SCREEN.blit(OPTIONS_THEME_SEARCH, OPTIONS_THEME_SEARCH_RECT)

        pygame.display.flip()




def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(MENU_BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Algorithm Visualizer", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))

        VERSION_TEXT = get_font(30).render("1.0.0", True, "#777a7a")
        VERSION_RECT = VERSION_TEXT.get_rect(center=(30, 705))

        CREDIT_TEXT = get_font(40).render("By: Adrian Garza", True, "#097882")
        CREDIT_RECT = CREDIT_TEXT.get_rect(center=(1140, 700))

        PLAY_BUTTON = Button(

            image=pygame.image.load("assets/new_play_button.png"),
            pos=(400, 400),
            text_input="", font=get_font(75), base_color="#808080", hovering_color="White")
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("assets/options_button.png"),
            pos=(640, 400),
            text_input="", font=get_font(75), base_color="#808080", hovering_color="White")
        QUIT_BUTTON = Button(
            image=pygame.image.load("assets/new_quit_button.png"),
            pos=(880, 400),
            text_input="", font=get_font(75), base_color="#808080", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(VERSION_TEXT, VERSION_RECT)
        SCREEN.blit(CREDIT_TEXT, CREDIT_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "play"
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "options"
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "quit"

        pygame.display.update()
