from src.snake.entities import next_position, spawn_food
from src.snake.settings import GRID_W, GRID_H

def test_next_position_moves_correctly():
    assert next_position((5, 5), (1, 0)) == (6, 5)
    assert next_position((0, 0), (0, 1)) == (0, 1)
    assert next_position((10, 7), (-1, 0)) == (9, 7)

def test_spawn_food_inside_grid_and_not_on_snake():
    snake = [(0, 0), (1, 0), (2, 0)]
    food = spawn_food(snake)
    assert food not in snake
    x, y = food
    assert 0 <= x < GRID_W
    assert 0 <= y < GRID_H
