import pygame
import random

#variables
algorithm = "BFS"
num_of_checkpoints = 2
FPS = 60
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
THEME = "Normal"

# colors
THEME_COLORS = {
    "Normal": {
        "SEEN": (0, 0, 255),
        "ADJACENT": (0, 255, 0),
        "CORRECT": (255, 0, 255),
        "WALL": (0,0,0),
        "BACKGROUND": (255, 255, 255)
    },
    "Dark": {
        "SEEN": (30, 30, 30),      # Dark gray
        "ADJACENT": (50, 50, 50),  # Lighter gray
        "CORRECT": (255, 69, 0),   # Orange-Red
        "WALL": (0, 0, 0),      # Dark Indigo
        "BACKGROUND": (30, 0, 140)    # Black
    },
    "Light": {
        "SEEN": (173, 216, 230),   # Light Blue
        "ADJACENT": (144, 238, 144),# Light Green
        "CORRECT": (255, 182, 193),# Light Pink
        "WALL": (211, 211, 211),   # Light Gray
        "BACKGROUND": (255, 255, 255) # White
    },
    "Dusk": {
        "SEEN": (72, 61, 139),     # Dark Slate Blue
        "ADJACENT": (255, 140, 0), # Dark Orange
        "CORRECT": (75, 0, 130),   # Indigo
        "WALL": (139, 69, 19),     # Saddle Brown
        "BACKGROUND": (70, 130, 180) # Steel Blue
    },
    "Spring": {
        "SEEN": (60, 179, 113),    # Medium Sea Green
        "ADJACENT": (255, 182, 193),# Light Pink
        "CORRECT": (255, 255, 0),  # Yellow
        "WALL": (34, 139, 34),     # Forest Green
        "BACKGROUND": (240, 255, 240) # Honeydew
    },
    "Summer": {
        "SEEN": (255, 215, 0),     # Gold
        "ADJACENT": (240, 128, 128),# Light Coral
        "CORRECT": (135, 206, 250),# Light Sky Blue
        "WALL": (34, 139, 34),     # Forest Green
        "BACKGROUND": (255, 250, 205) # Lemon Chiffon
    },
    "Fall": {
        "SEEN": (205, 92, 92),     # Indian Red
        "ADJACENT": (244, 164, 96),# Sandy Brown
        "CORRECT": (255, 69, 0),   # Orange-Red
        "WALL": (139, 69, 19),     # Saddle Brown
        "BACKGROUND": (255, 228, 181) # Moccasin
    },
    "Winter": {
        "SEEN": (176, 224, 230),   # Powder Blue
        "ADJACENT": (70, 130, 180),# Steel Blue
        "CORRECT": (255, 250, 250),# Snow
        "WALL": (25, 25, 112),     # Midnight Blue
        "BACKGROUND": (245, 245, 245) # White Smoke
    }
}


def apply_theme(theme_name):
    global SEEN_COLOR, ADJACENT_COLOR, CORRECT_COLOR, WALL_COLOR, BACKGROUND_COLOR

    theme_colors = THEME_COLORS.get(theme_name, THEME_COLORS['Normal'])

    SEEN_COLOR = theme_colors['SEEN']
    ADJACENT_COLOR = theme_colors['ADJACENT']
    CORRECT_COLOR = theme_colors['CORRECT']
    WALL_COLOR = theme_colors['WALL']
    BACKGROUND_COLOR = theme_colors['BACKGROUND']


# Define the theme colors globally but don't assign them until apply_theme is called
SEEN_COLOR = ADJACENT_COLOR = CORRECT_COLOR = WALL_COLOR = BACKGROUND_COLOR = None

# Apply the default theme at the beginning
apply_theme(THEME)

class GUI():

    def __init__(self, coords):
        self.grid_width = 32
        self.grid_height = 18
        self.box_height = WINDOW_HEIGHT / self.grid_height
        self.box_width = WINDOW_WIDTH / self.grid_width
        self.coords = coords
        self.placing_walls = False
        self.removing_walls = False
        self.animation_speed = 10

        self.coords.maze = [[0 for x in range(self.grid_width)] for y in range(self.grid_height)]

        pygame.init()
        self.win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(F"Pathfinding Algorithms: {algorithm}")

    def main(self, running=False):
        self.clock.tick(FPS)
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        if not running:
            if self.placing_walls:
                self.place_wall()
            elif self.removing_walls:
                self.remove()

        self.event_handle(running)
        self.redraw()
        pygame.display.update()


    def event_handle(self, running):
        run_algos = {"DFS", "BFS", "DIJKSTRA", "ASTAR"}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                key = chr(event.key)
                if not running:
                    if key == "x":
                        self.coords.remove_all()
                    elif key == "z":
                        self.coords.remove_last()
                    elif (key == "+" or key == "=") and self.animation_speed > 0:
                        if self.animation_speed <= 2:
                            self.animation_speed = 1
                        else:
                            self.animation_speed = int(self.animation_speed * .5)

                    elif key == "-":
                        self.animation_speed = int(self.animation_speed * 2) + 1

                    elif key == " ":
                        self.coords.generate_random_checkpoints(self)
                        self.coords.generate_random_maze(self)
                        if algorithm in run_algos:
                            self.run_algorithm(algorithm)
                else:
                    print(key)


    def redraw(self):
        self.win.fill(BACKGROUND_COLOR)
        self.draw_points()
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.grid_width - 1):
            pygame.draw.rect(self.win, WALL_COLOR, (((i + 1) * self.box_width) - 2, 0, 4, WINDOW_HEIGHT))
        for i in range(self.grid_height - 1):
            pygame.draw.rect(self.win, WALL_COLOR, (0, ((i + 1) * self.box_height) - 2, WINDOW_WIDTH, 4))

    def draw_points(self):
        for node in self.coords.open_list:
            self.draw_box(node.position, ADJACENT_COLOR)
        for node in self.coords.closed_list:
            self.draw_box(node.position, SEEN_COLOR)
        for wall in self.coords.final_path:
            self.draw_box(wall, CORRECT_COLOR)
        for wall in self.coords.walls:
            self.draw_box(wall, WALL_COLOR)
        for i, point in enumerate(self.coords.check_points):
            if point != "None":
                self.draw_box(point, (255, 30, 30))
                self.display_text(str(i + 1), (255, 255, 255), self.box_center(point), int(self.box_width))
        if self.coords.start is not None:
            self.draw_box(self.coords.start, (255, 0, 0))
            self.display_text("S", (255, 255, 255), self.box_center(self.coords.start), int(self.box_width))
        if self.coords.end is not None:
            self.draw_box(self.coords.end, (255, 0, 0))
            self.display_text("E", (255, 255, 255), self.box_center(self.coords.start), int(self.box_width))

    def box_center(self, box):
        boxX, boxY = box
        center = ((boxX * self.box_width + (self.box_width / 2)), (boxY * self.box_height + (self.box_height / 2)))
        return center

    def draw_box(self, box, color):
        boxX, boxY = box
        pygame.draw.rect(self.win, color,
                         (boxX * self.box_width, boxY * self.box_height, self.box_width, self.box_height))

    def get_box_coords(self):
        boxX = int((self.mouse_x + 2) / self.box_width)
        boxY = int((self.mouse_y + 2) / self.box_height)
        return (boxX, boxY)

    def place_check_point(self, index):
        coords = self.get_box_coords()
        if (coords != self.coords.start and coords != self.coords.end
                and coords not in self.coords.walls and coords
                not in self.coords.check_points):

            while len(self.coords.check_points) <= int(index) - 1:
                self.coords.check_points.append("None")
            self.coords.check_points[int(index) - 1] = coords

    def place_wall(self):
        coords = self.get_box_coords()
        if (coords != self.coords.start and coords != self.coords.end
                and coords not in self.coords.walls and coords
                not in self.coords.check_points):
            self.coords.walls.append(coords)

    def remove(self):
        coords = self.get_box_coords()
        if coords in self.coords.walls:
            self.coords.walls.remove(coords)
        elif coords in self.coords.check_points:
            self.coords.check_points.remove(coords)
        elif coords == self.coords.start:
            self.coords.start = None
        elif coords == self.coords.end:
            self.coords.end = None

    def run_algorithm(self, key):
        self.coords.remove_last()

        if len(self.coords.check_points) > 1:

            self.coords.create_maze(self)
            check_points = self.coords.check_points[:]
            check_points = [point for point in check_points if point != "None"]

            for i, point in enumerate(check_points):
                if i != len(check_points) - 1:

                    start = point
                    end = check_points[i + 1]

                    new_path = pathfind(self.coords.maze, start, end, self, self.coords, key, algorithm)
                    if new_path == None:
                        new_path = []

                    self.coords.final_path.extend(new_path)

    def display_text(self, txt, color, center, size):
        font = pygame.font.Font(None, size)
        text_surf = font.render(txt, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = (center)
        self.win.blit(text_surf, text_rect)


class Coordinates():

    def __init__(self):
        self.remove_all()

    def remove_all(self):
        self.start = None
        self.end = None
        self.walls = []
        self.maze = []
        self.open_list = []
        self.closed_list = []
        self.final_path = []
        self.check_points = []

    def remove_last(self):
        self.maze = []
        self.open_list = []
        self.closed_list = []
        self.final_path = []

    def largest_distance(self):
        largest_x = 0
        largest_y = 0

        for wall in self.walls:
            if wall[0] > largest_x:
                largest_x = wall[0]
            if wall[1] > largest_y:
                largest_y = wall[1]

        for point in self.check_points:
            if point[0] > largest_x:
                largest_x = point[0]
            if point[1] > largest_y:
                largest_y = point[1]

        return largest_x + 1, largest_y + 1

    def create_maze(self, gui):
        largest_x, largest_y = self.largest_distance()

        maze_width = max(gui.grid_width, largest_x)
        maze_height = max(gui.grid_height, largest_y)
        self.maze = [[0 for x in range(maze_height)] for y in range(maze_width)]

        for wall in self.walls:
            try:
                wall_x, wall_y = wall
                if 0 <= wall_x < maze_width and 0 <= wall_y < maze_height:
                    self.maze[wall_x][wall_y] = 1
            except IndexError:
                pass

    def generate_random_checkpoints(self, gui):
        self.check_points = []
        while len(self.check_points) < num_of_checkpoints or len(self.check_points) > num_of_checkpoints + 1:
            for i in range(gui.grid_height * gui.grid_width):
                if random.random() < 1 / 576:
                    checkpoint = (random.randint(0, gui.grid_width - 1),
                                  random.randint(0, gui.grid_height - 1))
                    if checkpoint not in self.check_points:
                        self.check_points.append(checkpoint)

    def generate_random_maze(self, gui):
        self.walls = []
        for i in range(gui.grid_height * gui.grid_width):
            if random.random() > .6:
                wall = (random.randint(0, gui.grid_width - 1),
                        random.randint(0, gui.grid_height - 1))
                if wall not in self.walls and wall not in self.check_points:
                    self.walls.append(wall)


def pathfind(maze, start, end, gui, coords, key, algorithm):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    count = 0

    while len(open_list) > 0:

        if count >= gui.animation_speed:
            count = 0

            if algorithm == "DFS":
                current_node = open_list[-1]
                current_index = len(open_list) - 1

            elif algorithm == "BFS":
                current_node = open_list[0]
                current_index = 0

            elif algorithm == "ASTAR":
                current_node = open_list[0]
                current_index = 0
                for index, item in enumerate(open_list):
                    if item.f < current_node.f:
                        current_node = item
                        current_index = index

            elif algorithm == "DIJKSTRA":
                current_node = open_list[0]
                current_index = 0
                for index, item in enumerate(open_list):
                    if item.g < current_node.g:
                        current_node = item
                        current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                coords.open_list = open_list
                coords.closed_list = closed_list
                return path

            for new_pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:

                node_pos = (current_node.position[0] + new_pos[0],
                            current_node.position[1] + new_pos[1])

                if (node_pos[0] > (len(maze) - 1) or node_pos[0] < 0
                        or node_pos[1] > (len(maze[len(maze) - 1]) - 1)
                        or node_pos[1] < 0):
                    continue

                if maze[node_pos[0]][node_pos[1]] != 0:
                    continue

                if Node(current_node, node_pos) in closed_list:
                    continue

                child = Node(current_node, node_pos)

                passList = [False for closed_child in closed_list if child == closed_child]
                if False in passList:
                    continue

                if algorithm == "DIJKSTRA":
                    child.g = current_node.g + 1

                elif algorithm == "ASTAR":
                    child.g = current_node.g + 1
                    child.h = (((abs(child.position[0] - end_node.position[0]) ** 2) +
                                (abs(child.position[1] - end_node.position[1]) ** 2)) ** .6)
                    child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g >= open_node.g:
                        break

                else:
                    open_list.append(child)

        else:
            coords.open_list = open_list
            coords.closed_list = closed_list
            gui.main(True)

        count += 1


class Node():
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position




def run():
    gui = GUI(Coordinates())
    while True:
        gui.main()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "menu"

"""
NOTES:

0   add themes

X   option for how many checkpoints wanted
X   grid to be 18 x 32
X   test.py works but traversal algorithms doesnt look into that
X   random maze to be made every time
X   random checkpoints to be made everytime
X   menu to determine the algorithm used not keys
"""
