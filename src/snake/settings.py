# src/snake/settings.py

# Grid/célula
CELL = 20
GRID_W, GRID_H = 32, 24  # 32*20=640, 24*20=480

# Tela (derivada do grid)
SCREEN_W, SCREEN_H = GRID_W * CELL, GRID_H * CELL

# FPS base do jogo
FPS = 12

# Cores (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED   = (220, 40, 40)
GRAY  = (230, 230, 230)

# Flags futuras (placeholders para próximas etapas)
SHOW_GRID = True
