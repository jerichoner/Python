# Демонстрация создания простой игры на Python с использованием Pygame
# Этот пример будет создавать базовую сетку и позволит игроку менять местами элементы

import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение параметров игры
screen_width, screen_height = 800, 600
grid_size = 8
cell_size = 50
margin = 4

# Цвета
background_color = (255, 255, 255)
cell_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Настройка экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Мир Кристаллов - Прототип")

# Функция для отрисовки сетки
def draw_grid():
    for row in range(grid_size):
        for col in range(grid_size):
            color = cell_colors[grid[row][col]]
            pygame.draw.rect(screen, color, [(margin + cell_size) * col + margin,
                                             (margin + cell_size) * row + margin,
                                             cell_size, cell_size])

# Генерация случайной сетки
def generate_grid():
    return [[random.randint(0, len(cell_colors) - 1) for _ in range(grid_size)] for _ in range(grid_size)]

# Основной цикл игры
def game_loop():
    grid = generate_grid()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_color)
        draw_grid()
        pygame.display.flip()

    pygame.quit()

# Запуск игры
game_loop()
