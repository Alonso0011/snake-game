# src/snake/game.py
# pylint: disable=no-member
import pygame
from typing import List, Tuple

from .settings import (
    SCREEN_W, SCREEN_H, FPS, CELL,
    WHITE, BLACK, GREEN, RED, GRAY, SHOW_GRID,
)
from .entities import next_position, spawn_food

Cell = Tuple[int, int]
Direction = Tuple[int, int]


def _draw_grid(surface: pygame.Surface) -> None:
    if not SHOW_GRID:
        return
    for x in range(0, SCREEN_W, CELL):
        pygame.draw.line(surface, GRAY, (x, 0), (x, SCREEN_H), 1)
    for y in range(0, SCREEN_H, CELL):
        pygame.draw.line(surface, GRAY, (0, y), (SCREEN_W, y), 1)


def _draw_cell(surface: pygame.Surface, cell: Cell, color) -> None:
    rect = pygame.Rect(cell[0] * CELL, cell[1] * CELL, CELL, CELL)
    pygame.draw.rect(surface, color, rect)


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Snake — MVP")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    # estado inicial
    cols, rows = SCREEN_W // CELL, SCREEN_H // CELL
    start = (cols // 2, rows // 2)
    snake: List[Cell] = [start]
    direction: Direction = (1, 0)  # direita
    grow = 0
    score = 0
    game_over = False

    food = spawn_food(snake)

    running = True
    while running:
        # ========== eventos ==========
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # controles (impede reversão imediata)
                if event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    direction = (0, 1)
                if game_over and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    # restart rápido
                    snake = [start]
                    direction = (1, 0)
                    grow = 0
                    score = 0
                    game_over = False
                    food = spawn_food(snake)

        if not game_over:
            # ========== regras ==========
            head = snake[-1]
            new_head = next_position(head, direction)

            cols, rows = SCREEN_W // CELL, SCREEN_H // CELL
            x, y = new_head
            # colisão parede
            if x < 0 or x >= cols or y < 0 or y >= rows:
                game_over = True
            # colisão corpo
            elif new_head in snake:
                game_over = True
            else:
                snake.append(new_head)
                # come?
                if new_head == food:
                    score += 10
                    grow += 1
                    food = spawn_food(snake)
                else:
                    if grow > 0:
                        grow -= 1
                    else:
                        snake.pop(0)

        # ========== render ==========
        screen.fill(WHITE)
        _draw_grid(screen)

        # comida
        _draw_cell(screen, food, RED)
        # cobra
        for i, seg in enumerate(snake):
            color = GREEN if i < len(snake) - 1 else (0, 255, 0)  # cabeça em verde mais vivo
            _draw_cell(screen, seg, color)

        # HUD
        score_surf = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surf, (10, 8))
        if game_over:
            over = font.render("GAME OVER — Enter/Espaço: Reiniciar | Esc: Sair", True, BLACK)
            screen.blit(over, over.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
