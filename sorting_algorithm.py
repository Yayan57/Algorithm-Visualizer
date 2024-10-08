import random
import pygame

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# variables
RECT_WIDTH = 20
clock = pygame.time.Clock()
FPS = 15
num_rectangles = (WINDOW_WIDTH // RECT_WIDTH) -5
THEME = "Normal"

# colors
THEME_COLORS = {
    "Normal": {
        "SET_SORTED": (0, 255, 0),
        "SELECT": (0, 0, 255),
        "LINE": (0, 0, 0),
        "UNSELECT": (128, 0, 128),
        "BACKGROUND": (170, 170, 170),
        "SET_SMALLEST": (64, 224, 208),
        "SET_LARGEST": (255, 0, 0),
        "TEXT": (0, 0, 0)
    },
    "Dark": {
        "SET_SORTED": (255, 255, 255),
        "SELECT": (0, 128, 0),
        "LINE": (0, 0, 0),
        "UNSELECT": (105, 105, 105),
        "BACKGROUND": (0, 0, 0),
        "SET_SMALLEST": (139, 0, 0),
        "SET_LARGEST": (255, 69, 0),
        "TEXT": (255, 255, 255)
    },
    "Light": {
        "SET_SORTED": (173, 216, 230),
        "SELECT": (255, 182, 193),
        "LINE": (192, 192, 192),
        "UNSELECT": (211, 211, 211),
        "BACKGROUND": (255, 255, 255),
        "SET_SMALLEST": (144, 238, 144),
        "SET_LARGEST": (255, 160, 122),
        "TEXT": (0, 0, 0)
    },
    "Dusk": {
        "SET_SORTED": (72, 61, 139),
        "SELECT": (75, 0, 130),
        "LINE": (47, 79, 79),
        "UNSELECT": (123, 104, 238),
        "BACKGROUND": (25, 25, 112),
        "SET_SMALLEST": (138, 43, 226),
        "SET_LARGEST": (255, 140, 0),
        "TEXT": (255, 255, 255)
    },
    "Spring": {
        "SET_SORTED": (245, 173, 148),
        "SELECT": (245, 91, 139),
        "LINE": (34, 139, 34),
        "UNSELECT": (98, 245, 230),
        "BACKGROUND": (180, 249, 165),
        "SET_SMALLEST": (255, 182, 193),
        "SET_LARGEST": (240, 128, 128),
        "TEXT": (34, 139, 34)
    },
    "Summer": {
        "SET_SORTED": (245, 91, 139),
        "SELECT": (243, 135, 47),
        "LINE": (0, 0, 0),
        "UNSELECT": (39, 180, 110),
        "BACKGROUND": (21, 178, 211),
        "SET_SMALLEST": (64, 224, 208),
        "SET_LARGEST": (255, 0, 0),
        "TEXT": (255, 215, 0)
    },
    "Fall": {
        "SET_SORTED": (210, 105, 30),
        "SELECT": (178, 34, 34),
        "LINE": (139, 69, 19),
        "UNSELECT": (165, 42, 42),
        "BACKGROUND": (222, 184, 135),
        "SET_SMALLEST": (244, 164, 96),
        "SET_LARGEST": (255, 140, 0),
        "TEXT": (139, 69, 19)
    },
    "Winter": {
        "SET_SORTED": (255, 250, 250),
        "SELECT": (135, 206, 250),
        "LINE": (176, 224, 230),
        "UNSELECT": (70, 130, 180),
        "BACKGROUND": (240, 248, 255),
        "SET_SMALLEST": (176, 224, 230),
        "SET_LARGEST": (0, 191, 255),
        "TEXT": (70, 130, 180)
    }
}

def apply_theme(theme_name):
    global SET_SORTED, SELECT, LINE, UNSELECT, BACKGROUND, SET_SMALLEST, SET_LARGEST, TEXT

    theme_colors = THEME_COLORS.get(theme_name, THEME_COLORS['Normal'])

    SET_SORTED = theme_colors['SET_SORTED']
    SELECT = theme_colors['SELECT']
    LINE = theme_colors['LINE']
    UNSELECT = theme_colors['UNSELECT']
    BACKGROUND = theme_colors['BACKGROUND']
    SET_SMALLEST = theme_colors['SET_SMALLEST']
    SET_LARGEST = theme_colors['SET_LARGEST']
    TEXT = theme_colors["TEXT"]

# Define the theme colors globally but don't assign them until apply_theme is called
SET_SORTED = SELECT = LINE = UNSELECT = BACKGROUND = SET_SMALLEST = SET_LARGEST = None

# Apply the default theme at the beginning
apply_theme(THEME)

# Your Rectangle class and other functions can follow after this.
class Rectangle:
    def __init__(self, color, x, height):
        self.color = color
        self.x = x
        self.width = RECT_WIDTH
        self.height = height

    def select(self):
        self.color = SELECT

    def unselect(self):
        self.color = UNSELECT

    def set_smallest(self):
        self.color = SET_SMALLEST

    def set_sorted(self):
        self.color = SET_SORTED

    def set_largest(self):
        self.color = SET_LARGEST

    @staticmethod
    def background():
        return BACKGROUND

def create_rectangles():
    rectangles = []
    heights = []

    total_width = num_rectangles * RECT_WIDTH
    start_x = (WINDOW_WIDTH - total_width) // 2
    apply_theme(THEME)

    for i in range(num_rectangles):
        height = random.randint(1, 60) * 10
        while height in heights:
            height = random.randint(1, 60) * 10

        heights.append(height)
        rect = Rectangle(UNSELECT, start_x + i * RECT_WIDTH, height)
        rectangles.append(rect)

    return rectangles

def draw_rects(rectangles):
    WINDOW.fill(Rectangle.background())

    for rect in rectangles:
        clamped_height = min(rect.height, WINDOW_HEIGHT)
        pygame.draw.rect(WINDOW, rect.color, (rect.x, WINDOW_HEIGHT - clamped_height, rect.width, clamped_height))
        pygame.draw.line(WINDOW, LINE, (rect.x, WINDOW_HEIGHT), (rect.x, WINDOW_HEIGHT - rect.height))
        pygame.draw.line(WINDOW, LINE, (rect.x + rect.width, WINDOW_HEIGHT),
                         (rect.x + rect.width, WINDOW_HEIGHT - rect.height))
        pygame.draw.line(WINDOW, LINE, (rect.x, WINDOW_HEIGHT - rect.height),
                         (rect.x + rect.width, WINDOW_HEIGHT - rect.height))


def bubble_sort(rectangles):
    num_rectangles = len(rectangles)

    for i in range(num_rectangles):
        for j in range(0, num_rectangles-i-1):
            rectangles[j].select()
            rectangles[j+1].select()
            draw_rects(rectangles)

            if rectangles[j].height > rectangles[j + 1].height:
                rectangles[j].x, rectangles[j+1].x = rectangles[j+1].x, rectangles[j].x
                rectangles[j], rectangles[j+1] = rectangles[j+1], rectangles[j]

                draw_rects(rectangles)

            rectangles[j].unselect()
            rectangles[j+1].unselect()

            yield

        rectangles[num_rectangles - 1 - i].set_sorted()
        draw_rects(rectangles)

def insertion_sort(rectangles):
    num_rectangles = len(rectangles)
    total_width = sum(rect.width for rect in rectangles)
    # Calculate the left margin to ensure equal spacing on both sides
    margin = (WINDOW_WIDTH - total_width) / 2

    for i in range(1, num_rectangles):
        key_rect = rectangles[i]
        key_rect.select()

        j = i - 1
        while j >= 0 and rectangles[j].height > key_rect.height:
            # Move the rectangle at j to position j+1
            rectangles[j + 1] = rectangles[j]
            rectangles[j + 1].x = margin + sum(rect.width for rect in rectangles[:j + 1])  # Adjust x position

            rectangles[j].select()
            draw_rects(rectangles)
            rectangles[j].unselect()
            j -= 1

            yield  # Pause after each shift for visualization

        # Place the key rectangle in its correct position
        rectangles[j + 1] = key_rect
        rectangles[j + 1].x = margin + sum(rect.width for rect in rectangles[:j + 1])  # Adjust x position

        key_rect.unselect()
        key_rect.set_sorted()
        draw_rects(rectangles)

        yield  # Pause after placing the key element

    # Mark all elements as sorted at the end
    for rect in rectangles:
        rect.set_sorted()
        draw_rects(rectangles)

def merge_sort(rectangles, start=0, end=None):
    if end is None:
        end = len(rectangles)

    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(rectangles, start, mid)
        yield from merge_sort(rectangles, mid, end)
        yield from merge(rectangles, start, mid, end)

def merge(rectangles, start, mid, end):

    original_postions = [rectangles[i].x for i in range(start, end)]
    left = rectangles[start:mid]
    right = rectangles[mid:end]

    i = j = 0
    for k in range(start, end):
        if i < len(left) and (j >= len(right) or left[i].height <= right[j].height):
            rectangles[k] = left[i]
            i += 1
        else:
            rectangles[k] = right[j]
            j += 1

        # Update x positions
        rectangles[k].x = original_postions[k - start]

        draw_rects(rectangles)
        yield  # Pause after merging each element

    for rect in rectangles[start:end]:
        rect.set_sorted()  # Mark the merged section as sorted
        draw_rects(rectangles)

def quick_sort(rectangles, low=0, high=None):
    global sort_complete
    if high is None:
        high = len(rectangles) - 1

    if low < high:
        p, pivot_index = yield from partition(rectangles, low, high)
        yield from quick_sort(rectangles, low, pivot_index - 1)
        yield from quick_sort(rectangles, pivot_index + 1, high)

    # Sorting is complete
    if low == 0 and high == len(rectangles) - 1:
        sort_complete = True
        for i in range(low, high+1):
            rectangles[i].set_sorted()
        draw_rects(rectangles)


def partition(rectangles, low, high):
    pivot = rectangles[high]
    pivot.select()
    i = low - 1

    for j in range(low, high):
        rectangles[j].select()
        draw_rects(rectangles)

        if rectangles[j].height < pivot.height:
            i += 1
            rectangles[i], rectangles[j] = rectangles[j], rectangles[i]
            rectangles[i].x, rectangles[j].x = rectangles[j].x, rectangles[i].x
            draw_rects(rectangles)

        rectangles[j].unselect()
        yield  # Pause after each comparison

    rectangles[i + 1], rectangles[high] = rectangles[high], rectangles[i + 1]
    rectangles[i + 1].x, rectangles[high].x = rectangles[high].x, rectangles[i + 1].x

    pivot.unselect()
    rectangles[i + 1].set_sorted()
    draw_rects(rectangles)

    yield  # Pause after partitioning
    return i + 1, i + 1



def selection_sort(rectangles):
    num_rectangles = len(rectangles)

    for i in range(num_rectangles):
        min_index = i
        rectangles[i].set_smallest()

        for j in range(i + 1, num_rectangles):
            rectangles[j].select()
            draw_rects(rectangles)

            if rectangles[j].height < rectangles[min_index].height:
                rectangles[min_index].unselect()
                min_index = j

            rectangles[min_index].set_smallest()
            draw_rects(rectangles)
            rectangles[j].unselect()

            yield

        rectangles[i].x, rectangles[min_index].x = rectangles[min_index].x, rectangles[i].x
        rectangles[i], rectangles[min_index] = rectangles[min_index], rectangles[i]

        rectangles[min_index].unselect()
        rectangles[i].set_sorted()

        draw_rects(rectangles)


def display_text(txt, y, size):
    FONT = pygame.font.SysFont('Futura', size)

    text = FONT.render(txt, True, TEXT)
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, y))
    WINDOW.blit(text, text_rect)


def sorter(algorithm):
    from menu import main_menu
    pygame.display.set_caption('Sorting Algorithm Visualization')
    rectangles = create_rectangles()
    draw_rects(rectangles)
    if algorithm == "Bubble":
        sorting_generator = bubble_sort(rectangles)
    if algorithm == "Insertion":
        sorting_generator = insertion_sort(rectangles)
    if algorithm == "Merge":
        sorting_generator = merge_sort(rectangles)
    if algorithm == "Quick":
        sorting_generator = quick_sort(rectangles)
    if algorithm == "Selection":
        sorting_generator = selection_sort(rectangles)


    sorting = False
    while True:
        clock.tick(FPS)
        if sorting:
            try:
                next(sorting_generator)
            except StopIteration:
                sorting = False
        else:
            draw_rects(rectangles)

        display_text(algorithm + " sort Visualization: ", 30, 40)
        display_text("Press SPACE to start or stop sorting", 70, 30)
        display_text("Q to quit or R to reset", 100, 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sorting = not sorting
                if event.key == pygame.K_q:
                    return "quit"
                if event.key == pygame.K_r:
                    return "menu"

        pygame.display.update()

    return "menu"
