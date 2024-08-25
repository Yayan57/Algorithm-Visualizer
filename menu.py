import pygame, sys, sorting_algorithm
from tools import Button, Slider, DropDown

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
base_font = pygame.font.Font(None, 45)
BG = pygame.image.load("assets/dark-gradient-background-6bly12umg2d4psr2.jpg")


def get_font(size):
    return pygame.font.Font(None, size)


def sort_menu():
    pygame.display.set_caption("Sorting Algorithms")

    while True:
        SORT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        SORT_TEXT = get_font(45).render("Choose a sorting algorithm", True, "#FFFFFF")
        SORT_RECT = SORT_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(SORT_TEXT, SORT_RECT)

        SORT_BUBBLE = Button(image=None, pos=(640, 260), text_input="BUBBLE", font=get_font(75), base_color="White",
                             hovering_color="Green")

        SORT_BUBBLE.changeColor(SORT_MOUSE_POS)
        SORT_BUBBLE.update(SCREEN)

        SORT_INSERTION = Button(image=None, pos=(640, 310), text_input="INSERTION", font=get_font(75),
                                base_color="White",
                                hovering_color="Green")

        SORT_INSERTION.changeColor(SORT_MOUSE_POS)
        SORT_INSERTION.update(SCREEN)

        SORT_QUICK = Button(image=None, pos=(640, 360), text_input="QUICK", font=get_font(75), base_color="White",
                            hovering_color="Green")

        SORT_QUICK.changeColor(SORT_MOUSE_POS)
        SORT_QUICK.update(SCREEN)

        SORT_MERGE = Button(image=None, pos=(640, 410), text_input="MERGE", font=get_font(75), base_color="White",
                            hovering_color="Green")

        SORT_MERGE.changeColor(SORT_MOUSE_POS)
        SORT_MERGE.update(SCREEN)

        SORT_SELECTION = Button(image=None, pos=(640, 460), text_input="SELECTION", font=get_font(75),
                                base_color="White",
                                hovering_color="Green")

        SORT_SELECTION.changeColor(SORT_MOUSE_POS)
        SORT_SELECTION.update(SCREEN)

        SORT_BACK = Button(image=None, pos=(640, 560), text_input="BACK", font=get_font(75),
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
                    return "menu"

        pygame.display.update()


def search_menu():
    pygame.display.set_caption("Graph searching algorithms")


def play():
    pygame.display.set_caption("Play")

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Choose a type of algorithm", True, "#FFFFFF")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_SORT = Button(image=None, pos=(640, 260), text_input="Sorting", font=get_font(75), base_color="White",
                           hovering_color="Green")

        PLAY_SORT.changeColor(PLAY_MOUSE_POS)
        PLAY_SORT.update(SCREEN)

        PLAY_SEARCH = Button(image=None, pos=(640, 310), text_input="Search", font=get_font(75), base_color="White",
                             hovering_color="Green")

        PLAY_SEARCH.changeColor(PLAY_MOUSE_POS)
        PLAY_SEARCH.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 560), text_input="BACK", font=get_font(75),
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

    input_box = pygame.Rect(900, 160, 140, 40)
    input_text = ""
    active = False

    MIN = 5
    MAX = 55
    max_rectangles = (sorting_algorithm.WINDOW_WIDTH // sorting_algorithm.RECT_WIDTH) - 5

    slider = Slider((970, 225), (140, 30), .5, 0, 100)

    COLOR_INACTIVE = (100, 80, 255)
    COLOR_ACTIVE = (100, 200, 255)
    COLOR_LIST_INACTIVE = (255, 100, 100)
    COLOR_LIST_ACTIVE = (255, 150, 150)

    # dropdown box

    OPTIONS_THEME_COLOR = DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        900, 250, 140, 50,
        pygame.font.SysFont(None, 30),
        "Select Theme", ["Normal", "Dark", "Light", "Dusk", "Spring", "Summer", "Fall", "Winter"])

    current_theme = sorting_algorithm.THEME



    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        #title
        OPTIONS_TEXT = get_font(45).render("This is Options screen.", True, "#000000")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #FPS text
        OPTIONS_FPS = get_font(45).render(f"Speed: {sorting_algorithm.FPS}", True, "#000000")
        OPTIONS_FPS_RECT = OPTIONS_TEXT.get_rect(center=(400, 175))
        SCREEN.blit(OPTIONS_FPS, OPTIONS_FPS_RECT)

        # Get the rounded value from the slider
        slider_value = round(slider.get_value())
        num_rectangles = max(MIN,
                             min(MAX, int((slider_value / 100) * max_rectangles)))  # Scale between 5 and max_rectangles
        #slider text
        OPTIONS_NRECTANGLES = get_font(45).render(f"Number of Rectangles: {num_rectangles}", True, "#000000")
        OPTIONS_NRECTANGLES_RECT = OPTIONS_TEXT.get_rect(center=(400, 225))
        SCREEN.blit(OPTIONS_NRECTANGLES, OPTIONS_NRECTANGLES_RECT)

        # Render slider
        slider.move_slider(OPTIONS_MOUSE_POS)
        slider.render(SCREEN)



        #back button
        OPTIONS_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75), base_color="Black",
                              hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        text_surface = get_font(40).render(input_text, True, pygame.Color('black'))
        text_rect = text_surface.get_rect()

        if text_rect.width > input_box.width - 7:
            text_rect.right = input_box.right - 5
        else:
            text_rect.right = input_box.right - 5
        text_rect.centery = input_box.centery

        clip_rect = pygame.Rect(input_box.left + 5, input_box.top, input_box.width - 7, input_box.height)

        pygame.draw.rect(SCREEN, pygame.Color('gray'), input_box, 2)
        SCREEN.set_clip(clip_rect)
        SCREEN.blit(text_surface, text_rect)
        SCREEN.set_clip(None)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    sorting_algorithm.num_rectangles = num_rectangles
                    sorting_algorithm.THEME = current_theme
                    return "menu"
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                slider.check_mouse_down(OPTIONS_MOUSE_POS)

            if event.type == pygame.MOUSEBUTTONUP:
                slider.check_mouse_up()

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text.isdigit() and len(input_text) < 8:
                        sorting_algorithm.FPS = int(input_text)
                        input_text = ""
                elif event.unicode.isdigit():
                    if len(input_text) < 7:
                        input_text += event.unicode
        theme_option = OPTIONS_THEME_COLOR.update(event_list)
        if theme_option >= 0:
            current_theme = OPTIONS_THEME_COLOR.options[theme_option]
            OPTIONS_THEME_COLOR.main = current_theme
        OPTIONS_THEME_COLOR.draw(SCREEN)

        # theme_text
        OPTIONS_THEME = get_font(45).render(f"Sort theme: {str(current_theme)}", True, "#000000")
        OPTIONS_THEME_RECT = OPTIONS_TEXT.get_rect(center=(400, 275))
        SCREEN.blit(OPTIONS_THEME, OPTIONS_THEME_RECT)

        pygame.display.flip()


def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Algorithm Visualizer", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))

        VERSION_TEXT = get_font(30).render("Beta", True, "#777a7a")
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
