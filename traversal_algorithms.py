import pygame
import random


class GUI():
    FPS = 60
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    def __init__(self, coords):
        self.grid_width = 32
        self.grid_height = 18
        self.box_height = self.WINDOW_HEIGHT / self.grid_height
        self.box_width = self.WINDOW_WIDTH / self.grid_width
        self.coords = coords
        self.placing_walls = False
        self.removing_walls = False
        self.animation_speed = 10

        self.coords.maze = [[0 for x in range(self.grid_width)] for y in range(self.grid_height)]

        pygame.init()
        self.win = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pathfinding Algorithms")

    def main(self, running=False):
        self.clock.tick(self.FPS)
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
        run_keys = {"q", "w", "e", "r"}
        checkpoint_keys = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                key = chr(event.key)
                if not running:
                    if key in run_keys:
                        self.run_algorithm(key)
                    elif key == "x":
                        self.coords.remove_all()
                    elif key == "z":
                        self.coords.remove_last()
                    elif key in checkpoint_keys:
                        self.place_check_point(key)
                    elif (key == "+" or key == "=") and self.animation_speed > 0:
                        if self.animation_speed <= 2:
                            self.animation_speed = 1
                        else:
                            self.animation_speed = int(self.animation_speed * .5)

                    elif key == "-":
                        self.animation_speed = int(self.animation_speed * 2) + 1

                    elif key == " ":
                        self.coords.generate_random_maze(gui)

                    elif key == "i":
                        self.coords.generate_random_checkpoints(gui)

                else:
                    print(key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not running:
                    if event.button == 1:
                        self.placing_walls = True
                    elif event.button == 3:
                        self.removing_walls = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.placing_walls = False
                elif event.button == 3:
                    self.removing_walls = False

    def redraw(self):
        self.win.fill((255, 255, 255))
        self.draw_points()
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.grid_width - 1):
            pygame.draw.rect(self.win, (0, 0, 0), (((i + 1) * self.box_width) - 2, 0, 4, self.WINDOW_HEIGHT))
        for i in range(self.grid_height -1):
            pygame.draw.rect(self.win, (0, 0, 0), (0, ((i + 1) * self.box_height) - 2, self.WINDOW_WIDTH, 4))

    def draw_points(self):
        for node in self.coords.open_list:
            self.draw_box(node.position, (0, 255, 0))
        for node in self.coords.closed_list:
            self.draw_box(node.position, (0, 0, 255))
        for wall in self.coords.final_path:
            self.draw_box(wall, (255, 0, 255))
        for wall in self.coords.walls:
            self.draw_box(wall, (0, 0, 0))
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
        center = ((boxX * self.box_width + (self.box_width / 2)), (boxY * self.box_width + (self.box_width / 2)))
        return center

    def draw_box(self, box, color):
        boxX, boxY = box
        pygame.draw.rect(self.win, color,
                         (boxX * self.box_width, boxY * self.box_width, self.box_width, self.box_width))

    def get_box_coords(self):
        boxX = int((self.mouse_x + 2) / self.box_width)
        boxY = int((self.mouse_y + 2) / self.box_width)
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
        self.placing_walls == False
        self.removing_walls == False
        self.coords.remove_last()

        if len(self.coords.check_points) > 1:

            self.coords.create_maze(gui)
            check_points = self.coords.check_points[:]
            check_points = [point for point in check_points if point != "None"]

            for i, point in enumerate(check_points):
                if i != len(check_points) - 1:

                    start = point
                    end = check_points[i + 1]

                    new_path = pathfind(self.coords.maze, start, end, self, self.coords, key)
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
        self.check_points = []
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
        largest = 0
        for wall in self.walls:
            if wall[0] > largest: largest = wall[0]
            if wall[1] > largest: largest = wall[1]
        for point in self.check_points:
            if point[0] > largest: largest = point[0]
            if point[1] > largest: largest = point[1]
        return largest + 1

    def create_maze(self, gui):

        largest_distance = self.largest_distance()
        grid_size = ((gui.grid_height * gui.grid_width) // 2)
        if grid_size > largest_distance:
            largest = grid_size
        else:
            largest = largest_distance

        self.maze = [[0 for x in range(largest)] for y in range(largest)]
        for wall in self.walls:
            try:
                wall_x, wall_y = wall
                self.maze[wall_x][wall_y] = 1
            except:
                pass

    def generate_random_checkpoints(self, gui):
        self.check_points = []
        for i in range(gui.grid_height * gui.grid_width):
            if random.random() < 2 / 576:
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
                if wall not in self.walls:
                    self.walls.append(wall)

def pathfind(maze, start, end, gui, coords, key):

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

            if key == "q": #dfs
                current_node = open_list[-1]
                current_index = len(open_list) - 1

            elif key == "w": #bfs
                current_node = open_list[0]
                current_index = 0

            elif key == "r": #a*
                current_node = open_list[0]
                current_index = 0
                for index, item in enumerate(open_list):
                    if item.f < current_node.f:
                        current_node = item
                        current_index = index

            elif key == "e":  #dijkstra
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

                if key == "e":
                    child.g = current_node.g + 1

                elif key == "r":
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


gui = GUI(Coordinates())
while True:
    gui.main()

    """
NOTES:
X   grid to be 18 x 32
0   random maze to be made every time
0   random checkpoints to be made everytime
0   keys to stop and start
0   menu to determine the algorithm used not keys
0   option for how many checkpoints wanted
    """