# src/snake/entities.py
from typing import List, Tuple, Set
from .settings import GRID_W, GRID_H

Cell = Tuple[int, int]       # (x, y) em células
Direction = Tuple[int, int]  # (dx, dy)

def next_position(head: Cell, direction: Direction) -> Cell:
    """
    Calcula a próxima posição da cabeça.
    Não aplica wrap nem validações de borda/colisão (isso é papel do loop).
    """
    return head[0] + direction[0], head[1] + direction[1]

def spawn_food(snake: List[Cell]) -> Cell:
    """
    Gera comida em uma célula livre do grid.
    """
    import random
    occupied: Set[Cell] = set(snake)
    free_cells = [(x, y) for x in range(GRID_W) for y in range(GRID_H) if (x, y) not in occupied]
    # fallback: se não houver célula livre (grid cheio), retorna a própria cabeça
    return random.choice(free_cells) if free_cells else snake[-1]
