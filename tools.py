import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, minim: int, maxim: int) -> None:
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.minim = minim
        self.maxim = maxim

        
        self.initial_val = initial_val
        self.value = initial_val  

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + (self.initial_val * self.size[0]) - 5, self.slider_top_pos, 10, self.size[1])

        self.moving = False  

    def move_slider(self, mouse_pos):
        if self.moving:
            self.button_rect.centerx = min(max(mouse_pos[0], self.slider_left_pos), self.slider_right_pos)
            self.value = (self.button_rect.centerx - self.slider_left_pos) / self.size[0]

    def render(self, screen):
        pygame.draw.rect(screen, "darkgray", self.container_rect)  
        pygame.draw.rect(screen, "blue", self.button_rect)  

    def check_mouse_down(self, mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            self.moving = True  

    def check_mouse_up(self):
        self.moving = False 

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.button_rect.centerx - self.slider_left_pos
        return round((button_val / val_range) * (self.maxim - self.minim) + self.minim)



