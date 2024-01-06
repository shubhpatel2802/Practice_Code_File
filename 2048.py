import pygame
import random

pygame.init()

GRID_SIZE = 4
TILE_SIZE = 100
WIDTH = GRID_SIZE * TILE_SIZE
HEIGHT = GRID_SIZE * TILE_SIZE
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (205, 193, 180)
FONT_COLOR = (255, 255, 255)

def initialize_grid():
    return [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

def draw_grid(screen, grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, GRID_COLOR, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            value = grid[i][j]
            if value != 0:
                draw_tile(screen, i, j, value)

def draw_tile(screen, row, col, value):
    font = pygame.font.Font(None, 36)
    text = font.render(str(value), True, FONT_COLOR)
    text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
    pygame.draw.rect(screen, get_tile_color(value), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    screen.blit(text, text_rect)

def get_tile_color(value):
    colors = {
        0: (205, 193, 180),
        2: (238, 228, 218),
        4: (237, 224, 200),
        8: (242, 177, 121),
        16: (245, 149, 99),
        32: (246, 124, 95),
        64: (246, 94, 59),
        128: (237, 207, 114),
        256: (237, 204, 97),
        512: (237, 200, 80),
        1024: (237, 197, 63),
        2048: (237, 194, 46),
    }
    return colors.get(value, (255, 255, 255))

def merge_tiles(line):
    merged_line = [0] * GRID_SIZE
    current_index = 0

    for value in line:
        if value != 0:
            if merged_line[current_index] == 0:
                merged_line[current_index] = value
            elif merged_line[current_index] == value:
                merged_line[current_index] *= 2
                current_index += 1
            else:
                current_index += 1
                merged_line[current_index] = value

    return merged_line

def move(grid, direction):
    if direction == "left":
        for i in range(GRID_SIZE):
            grid[i] = merge_tiles(grid[i])
    elif direction == "right":
        for i in range(GRID_SIZE):
            grid[i] = merge_tiles(grid[i][::-1])[::-1]
    elif direction == "up":
        for j in range(GRID_SIZE):
            column = [grid[i][j] for i in range(GRID_SIZE)]
            column = merge_tiles(column)
            for i in range(GRID_SIZE):
                grid[i][j] = column[i]
    elif direction == "down":
        for j in range(GRID_SIZE):
            column = [grid[i][j] for i in range(GRID_SIZE)]
            column = merge_tiles(column[::-1])[::-1]
            for i in range(GRID_SIZE):
                grid[i][j] = column[i]

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 Game")

    grid = initialize_grid()

    add_new_tile(grid)
    add_new_tile(grid)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move(grid, "left")
                    add_new_tile(grid)
                elif event.key == pygame.K_RIGHT:
                    move(grid, "right")
                    add_new_tile(grid)
                elif event.key == pygame.K_UP:
                    move(grid, "up")
                    add_new_tile(grid)
                elif event.key == pygame.K_DOWN:
                    move(grid, "down")
                    add_new_tile(grid)

        screen.fill(BACKGROUND_COLOR)

        draw_grid(screen, grid)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
