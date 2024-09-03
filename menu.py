import pygame, sys, sorting_algorithm, os

import traversal_algorithms
from tools import Button, Slider, DropDown

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
base_font = pygame.font.Font(None, 45)
MENU_BG = pygame.image.load(resource_path("assets/dark-gradient-background-6bly12umg2d4psr2.jpg"))
OPTIONS_BG = pygame.image.load(resource_path("assets/white-gradient-background-o0tqqpgs66oz4rfr.jpg"))
PLAY_BG = pygame.image.load(resource_path("assets/gradient-colour-background-illustration-free-vector.jpg"))
SORT_BG = pygame.image.load(resource_path("assets/dark-brown-gradient-background-dark-red-brown-background-pattern-for-website-landing-pages-blurred-template-vector.jpg"))
SEARCH_BG = pygame.image.load(resource_path("assets/papers.co-sk64-dark-green-blur-gradation-23-wallpaper.jpg"))

icon_path = resource_path('assets/icons8-search-algorithm-outline-black-16.png')  # Adjust the path to your icon file
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

def get_font(size):
    return pygame.font.Font(None, size)


def sort_menu():
    pygame.display.set_caption("Sorting Algorithms")

    while True:
        sort_mouse_pos = pygame.mouse.get_pos()

        SCREEN.blit(SORT_BG, (0, 0))

        sort_text = get_font(45).render("Choose a sorting algorithm", True, "#FFFFFF")
        sort_rect = sort_text.get_rect(center=(640, 160))
        SCREEN.blit(sort_text, sort_rect)

        sort_bubble = Button(image=pygame.image.load(resource_path("assets/Bubble.png")), pos=(150, 400), text_input="", font=get_font(75), base_color="White",
                             hovering_color="Green")

        sort_bubble.changeColor(sort_mouse_pos)
        sort_bubble.update(SCREEN)

        sort_insertion = Button(image=pygame.image.load(resource_path("assets/insertion.webp")), pos=(400, 400), text_input="", font=get_font(75),
                                base_color="White",
                                hovering_color="Green")

        sort_insertion.changeColor(sort_mouse_pos)
        sort_insertion.update(SCREEN)

        sort_quick = Button(image=pygame.image.load(resource_path("assets/quick.png")), pos=(650, 400), text_input="", font=get_font(75), base_color="White",
                            hovering_color="Green")

        sort_quick.changeColor(sort_mouse_pos)
        sort_quick.update(SCREEN)

        sort_merge = Button(image=pygame.image.load(resource_path("assets/merge.png")), pos=(900, 400), text_input="", font=get_font(75), base_color="White",
                            hovering_color="Green")

        sort_merge.changeColor(sort_mouse_pos)
        sort_merge.update(SCREEN)

        sort_selection = Button(image=pygame.image.load(resource_path("assets/selection.png")), pos=(1150, 400), text_input="", font=get_font(75),
                                base_color="White",
                                hovering_color="Green")

        sort_selection.changeColor(sort_mouse_pos)
        sort_selection.update(SCREEN)

        sort_back = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75),
                           base_color="White",
                           hovering_color="Green")

        sort_back.changeColor(sort_mouse_pos)
        sort_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sort_bubble.checkForInput(sort_mouse_pos):
                    return "Bubble"
                if sort_insertion.checkForInput(sort_mouse_pos):
                    return "Insertion"
                if sort_quick.checkForInput(sort_mouse_pos):
                    return "Quick"
                if sort_merge.checkForInput(sort_mouse_pos):
                    return "Merge"
                if sort_selection.checkForInput(sort_mouse_pos):
                    return "Selection"
                if sort_back.checkForInput(sort_mouse_pos):
                    return "play"

        pygame.display.update()


def search_menu():
    pygame.display.set_caption("Graph search algorithms")

    while True:
        sort_mouse_pos = pygame.mouse.get_pos()

        SCREEN.blit(SEARCH_BG, (0, 0))

        search_text = get_font(45).render("Choose a search algorithm", True, "#FFFFFF")
        search_rect = search_text.get_rect(center=(640, 100))
        SCREEN.blit(search_text, search_rect)

        inst_text = get_font(45).render("Space to start, and R to reset when search is done.", True, "#FFFFFF")
        inst_rect = inst_text.get_rect(center=(640, 160))
        SCREEN.blit(inst_text, inst_rect)

        search_dfs = Button(image=pygame.image.load(resource_path("assets/dfs.png")), pos=(250, 400), text_input="", font=get_font(75), base_color="Black",
                             hovering_color="Green")


        search_dfs.changeColor(sort_mouse_pos)
        search_dfs.update(SCREEN)

        search_bfs = Button(image=pygame.image.load(resource_path("assets/bfs.png")), pos=(500, 400), text_input="", font=get_font(75),
                                base_color="Black",
                                hovering_color="Green")

        search_bfs.changeColor(sort_mouse_pos)
        search_bfs.update(SCREEN)

        search_dijkstra = Button(image=pygame.image.load(resource_path("assets/dijkstra.png")), pos=(750, 400), text_input="", font=get_font(75), base_color="Black",
                            hovering_color="Green")

        search_dijkstra.changeColor(sort_mouse_pos)
        search_dijkstra.update(SCREEN)

        search_astar = Button(image=pygame.image.load(resource_path("assets/astar.png")), pos=(1000, 400), text_input="", font=get_font(75), base_color="Black",
                            hovering_color="Green")

        search_astar.changeColor(sort_mouse_pos)
        search_astar.update(SCREEN)

        search_back = Button(image=None, pos=(640, 650), text_input="BACK", font=get_font(75),
                           base_color="White",
                           hovering_color="Green")

        search_back.changeColor(sort_mouse_pos)
        search_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if search_dfs.checkForInput(sort_mouse_pos):
                    traversal_algorithms.algorithm = "DFS"
                if search_bfs.checkForInput(sort_mouse_pos):
                    traversal_algorithms.algorithm = "BFS"
                if search_dijkstra.checkForInput(sort_mouse_pos):
                    traversal_algorithms.algorithm = "DIJKSTRA"
                if search_astar.checkForInput(sort_mouse_pos):
                    traversal_algorithms.algorithm = "ASTAR"
                if search_back.checkForInput(sort_mouse_pos):
                    return "play"
                return "Traversal"

        pygame.display.update()



def play():
    pygame.display.set_caption("Play")

    while True:

        play_mouse_pos = pygame.mouse.get_pos()

        SCREEN.blit(PLAY_BG, (0, 0))

        play_text = get_font(45).render("Choose a type of algorithm", True, "#FFFFFF")
        play_rect = play_text.get_rect(center=(640, 160))
        SCREEN.blit(play_text, play_rect)

        play_sort = Button(image=pygame.image.load(resource_path("assets/sort.png")), pos=(490, 400), text_input="", font=get_font(75), base_color="White",
                           hovering_color="Green")

        play_sort.changeColor(play_mouse_pos)
        play_sort.update(SCREEN)

        play_search = Button(image=pygame.image.load(resource_path("assets/search.png")), pos=(790, 400), text_input="", font=get_font(75), base_color="White",
                             hovering_color="Green")

        play_search.changeColor(play_mouse_pos)
        play_search.update(SCREEN)

        play_back = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75),
                           base_color="White",
                           hovering_color="Green")

        play_back.changeColor(play_mouse_pos)
        play_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_sort.checkForInput(play_mouse_pos):
                    return "sort"
                if play_search.checkForInput(play_mouse_pos):
                    return "search"
                if play_back.checkForInput(play_mouse_pos):
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
    options_theme_color_sort = DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        900, 160, 140, 40,
        pygame.font.SysFont(None, 30),
        "Select Theme", ["Normal", "Dark", "Light", "Dusk", "Spring", "Summer", "Fall", "Winter"]
    )

    options_theme_color_search = DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        230, 310, 140, 40,
        pygame.font.SysFont(None, 30),
        "Select Theme", ["Normal", "Dark", "Light", "Dusk", "Spring", "Summer", "Fall", "Winter"]
    )

    current_theme_sort = sorting_algorithm.THEME
    current_theme_search = traversal_algorithms.THEME

    while True:
        options_mouse_pos = pygame.mouse.get_pos()
        SCREEN.blit(OPTIONS_BG, (0, 0))

        # title
        options_text = get_font(45).render("Options", True, "#000000")
        options_rect = options_text.get_rect(center=(640, 100))
        SCREEN.blit(options_text, options_rect)

        # FPS text
        options_fps = get_font(45).render(f"Sort Speed: {sorting_algorithm.FPS}", True, "#000000")
        options_fps_rect = options_fps.get_rect(midleft=(225, 275))
        SCREEN.blit(options_fps, options_fps_rect)

        # Get the rounded value from the slider
        slider_value = round(slider.get_value())
        num_rectangles = max(MIN, min(MAX, int((slider_value / 100) * max_rectangles)))  # Scale between 5 and max_rectangles

        # slider text
        options_nrectangles = get_font(45).render(f"Number of Rectangles: {num_rectangles}", True, "#000000")
        options_nrectangles_rect = options_nrectangles.get_rect(midleft=(225, 225))
        SCREEN.blit(options_nrectangles, options_nrectangles_rect)

        # Render slider
        slider.move_slider(options_mouse_pos)
        slider.render(SCREEN)

        # Get the rounded value from the checkpoint slider
        checkpoint_value = round(slider_checkpoint.get_value())

        # Checkpoints text
        options_checkpoints = get_font(45).render(f"Number of Checkpoints: {checkpoint_value}", True, "#000000")
        options_checkpoints_rect = options_checkpoints.get_rect(midright=(1040, 375))
        SCREEN.blit(options_checkpoints, options_checkpoints_rect)

        # Checkpoints speed text
        options_checkpoints_speed = get_font(45).render(f"Search Speed: {traversal_algorithms.FPS}", True, "#000000")
        options_checkpoints_rect_speed = options_checkpoints_speed.get_rect(midright=(1040, 425))
        SCREEN.blit(options_checkpoints_speed, options_checkpoints_rect_speed)

        # Render checkpoint slider
        slider_checkpoint.move_slider(options_mouse_pos)
        slider_checkpoint.render(SCREEN)

        # back button
        options_back = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        options_back.changeColor(options_mouse_pos)
        options_back.update(SCREEN)

        text_surface_speed = get_font(40).render(input_text_speed, True, pygame.Color('black'))
        text_width_speed, text_height_speed = text_surface_speed.get_size()
        text_x_speed = input_box_speed.right - text_width_speed - 10  # Right-align the text within the box
        text_y_speed = input_box_speed.centery - text_height_speed // 2  # Center the text vertically
        SCREEN.blit(text_surface_speed, (text_x_speed, text_y_speed))
        pygame.draw.rect(SCREEN, pygame.Color('gray'), input_box_speed, 2)

        # Render input box for checkpoints speed (Right-aligned and vertically centered)
        text_surface_checkpoint_speed = get_font(40).render(input_text_checkpoint_speed, True, pygame.Color('black'))
        text_width_checkpoint_speed, text_height_checkpoint_speed = text_surface_checkpoint_speed.get_size()
        text_x_checkpoint_speed = input_box_checkpoint_speed.right - text_width_checkpoint_speed - 10  # Right-align the text within the box
        text_y_checkpoint_speed = input_box_checkpoint_speed.centery - text_height_checkpoint_speed // 2  # Center the text vertically
        SCREEN.blit(text_surface_checkpoint_speed, (text_x_checkpoint_speed, text_y_checkpoint_speed))
        pygame.draw.rect(SCREEN, pygame.Color('gray'), input_box_checkpoint_speed, 2)

        # theme_text
        options_theme_sort = get_font(45).render(f"Sort theme: {str(current_theme_sort)}", True, "#000000")
        options_theme_sort_rect = options_theme_sort.get_rect(midleft=(225, 175))
        SCREEN.blit(options_theme_sort, options_theme_sort_rect)


        # theme_text
        options_theme_search = get_font(45).render(f"Search theme: {str(current_theme_search)}", True, "#000000")
        options_theme_search_rect = options_theme_search.get_rect(midright=(1040, 325))
        SCREEN.blit(options_theme_search, options_theme_search_rect)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
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

                slider.check_mouse_down(options_mouse_pos)
                slider_checkpoint.check_mouse_down(options_mouse_pos)

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

        theme_option_sort = options_theme_color_sort.update(event_list)
        if theme_option_sort >= 0:
            current_theme_sort = options_theme_color_sort.options[theme_option_sort]
            options_theme_color_sort.main = current_theme_sort
        options_theme_color_sort.draw(SCREEN)



        theme_option_search = options_theme_color_search.update(event_list)
        if theme_option_search >= 0:
            current_theme_search = options_theme_color_search.options[theme_option_search]
            options_theme_color_search.main = current_theme_search
        options_theme_color_search.draw(SCREEN)



        pygame.display.flip()




def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(MENU_BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Algorithm Visualizer", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 150))

        version_text = get_font(30).render("1.0.0", True, "#777a7a")
        version_rect = version_text.get_rect(center=(30, 705))

        credit_text = get_font(40).render("By: Adrian Garza", True, "#097882")
        credit_rect = credit_text.get_rect(center=(1140, 700))

        play_button = Button(

            image=pygame.image.load(resource_path("assets/new_play_button.png")),
            pos=(400, 400),
            text_input="", font=get_font(75), base_color="#808080", hovering_color="White")
        options_button = Button(
            image=pygame.image.load(resource_path("assets/options_button.png")),
            pos=(640, 400),
            text_input="", font=get_font(75), base_color="#808080", hovering_color="White")
        quit_button = Button(
            image=pygame.image.load(resource_path("assets/new_quit_button.png")),
            pos=(880, 400),
            text_input="", font=get_font(75), base_color="#808080", hovering_color="White")

        SCREEN.blit(menu_text, menu_rect)
        SCREEN.blit(version_text, version_rect)
        SCREEN.blit(credit_text, credit_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    return "play"
                if options_button.checkForInput(menu_mouse_pos):
                    return "options"
                if quit_button.checkForInput(menu_mouse_pos):
                    return "quit"

        pygame.display.update()
