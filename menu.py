import pygame, sys, sorting_algorithm
from button import Button

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/dark-gradient-background-6bly12umg2d4psr2.jpg")


def get_font(size):
    return pygame.font.Font(None, size)


def play():
    pygame.display.set_caption("Play")

    from sorting_algorithm import sorter
    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Choose a sorting algorithm", True, "#FFFFFF")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BUBBLE = Button(image=None, pos=(640, 260), text_input="BUBBLE", font=get_font(75), base_color="White",
                           hovering_color="Green")

        PLAY_BUBBLE.changeColor(PLAY_MOUSE_POS)
        PLAY_BUBBLE.update(SCREEN)

        PLAY_INSERTION = Button(image=None, pos=(640, 310), text_input="INSERTION", font=get_font(75), base_color="White",
                             hovering_color="Green")

        PLAY_INSERTION.changeColor(PLAY_MOUSE_POS)
        PLAY_INSERTION.update(SCREEN)

        PLAY_QUICK = Button(image=None, pos=(640, 360), text_input="QUICK", font=get_font(75), base_color="White",
                             hovering_color="Green")

        PLAY_QUICK.changeColor(PLAY_MOUSE_POS)
        PLAY_QUICK.update(SCREEN)

        PLAY_MERGE = Button(image=None, pos=(640, 410), text_input="MERGE", font=get_font(75), base_color="White",
                             hovering_color="Green")

        PLAY_MERGE.changeColor(PLAY_MOUSE_POS)
        PLAY_MERGE.update(SCREEN)

        PLAY_SELECTION = Button(image=None, pos=(640, 460), text_input="SELECTION", font=get_font(75), base_color="White",
                             hovering_color="Green")

        PLAY_SELECTION.changeColor(PLAY_MOUSE_POS)
        PLAY_SELECTION.update(SCREEN)

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
                if PLAY_BUBBLE.checkForInput(PLAY_MOUSE_POS):
                    return "Bubble"
                if PLAY_INSERTION.checkForInput(PLAY_MOUSE_POS):
                    return "Insertion"
                if PLAY_QUICK.checkForInput(PLAY_MOUSE_POS):
                    return "Quick"
                if PLAY_MERGE.checkForInput(PLAY_MOUSE_POS):
                    return "Merge"
                if PLAY_SELECTION.checkForInput(PLAY_MOUSE_POS):
                    return "Selection"
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    return "menu"

        pygame.display.update()


def options():
    pygame.display.set_caption("Options")
    input_box = pygame.Rect(200, 150, 140, 74)
    input_text = ""
    active = False

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is Options screen.", True, "#000000")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75), base_color="Black",
                              hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return "menu"
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        sorting_algorithm.FPS = int(input_text)
                        print(f"Number entered: {sorting_algorithm.FPS}")
                        input_text = ""
                elif event.unicode.isdigit():
                    input_text += event.unicode

        pygame.draw.rect(SCREEN, (200, 200, 200), input_box, 0)  # Filled rectangle
        pygame.draw.rect(SCREEN, (0, 0, 0), input_box, 2)  # Border of the rectangle

        # Render the input text
        text_surface = get_font(45).render(input_text, True, (0, 0, 0))
        SCREEN.blit(text_surface, (input_box.x + 10, input_box.y + 10))

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

