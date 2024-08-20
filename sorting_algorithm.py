import random
import pygame

pygame.init()

WINDOW_SIZE = 720
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# variables
RECT_WIDTH = 20
clock = pygame.time.Clock()
FPS = 15

# colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GREY = (170, 170, 170)
LIGHT_BLUE = (64, 224, 208)
RED = (255, 0, 0)


class Rectangle:
    def __init__(self, color, x, height):
        self.color = color
        self.x = x
        self.width = RECT_WIDTH
        self.height = height

    def select(self):
        self.color = BLUE

    def unselect(self):
        self.color = PURPLE

    def set_smallest(self):
        self.color = LIGHT_BLUE

    def set_sorted(self):
        self.color = GREEN

    def set_largest(self):
        self.color = RED


def create_rectangles():
    num_rectangles = WINDOW_SIZE // RECT_WIDTH - 5
    rectangles = []
    heights = []

    for i in range(5, num_rectangles):
        height = random.randint(2, 50) * 10
        while height in heights:
            height = random.randint(2, 50) * 10

        heights.append(height)
        rect = Rectangle(PURPLE, i * RECT_WIDTH, height)
        rectangles.append(rect)
    return rectangles


def draw_rects(rectangles):
    WINDOW.fill(GREY)

    for rect in rectangles:
        pygame.draw.rect(WINDOW, rect.color, (rect.x, WINDOW_SIZE - rect.height, rect.width, rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x, WINDOW_SIZE), (rect.x, WINDOW_SIZE - rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x + rect.width, WINDOW_SIZE),
                         (rect.x + rect.width, WINDOW_SIZE - rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x, WINDOW_SIZE - rect.height),
                         (rect.x + rect.width, WINDOW_SIZE - rect.height))

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
    screen_width = 600  # Adjusted screen width
    # Calculate the left margin to ensure equal spacing on both sides
    margin = (screen_width - total_width) / 2

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
        rectangles[k].x = k * rectangles[k].width

        draw_rects(rectangles)
        yield  # Pause after merging each element

    for rect in rectangles[start:end]:
        rect.set_sorted()  # Mark the merged section as sorted
        draw_rects(rectangles)

def quick_sort(rectangles, low=0, high=None):
    if high is None:
        high = len(rectangles) - 1

    if low < high:
        p, pivot_index = yield from partition(rectangles, low, high)
        yield from quick_sort(rectangles, low, pivot_index - 1)
        yield from quick_sort(rectangles, pivot_index + 1, high)

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

    text = FONT.render(txt, True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_SIZE / 2, y))
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
