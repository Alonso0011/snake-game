# pylint: disable=no-member
import requests
import pygame
import random

# Configuração inicial do jogo (pygame, variáveis de tela, etc.)
pygame.init()

# Configuração da tela
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Função para desenhar a cobra (já existente)
def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 20, 20))

# Função para enviar a pontuação ao backend Flask
def submit_score(name, score):
    url = 'http://127.0.0.1:5000/ranking'  # A URL do backend Flask
    data = {'name': name, 'score': score}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Pontuação enviada com sucesso!")
    else:
        print("Erro ao enviar pontuação:", response.status_code)

# Função principal do jogo
def game_loop():
    game_over = False
    snake_x = screen_width // 2
    snake_y = screen_height // 2
    snake_body = [(snake_x, snake_y)]
    direction = "RIGHT"
    score = 0  # Inicializando a pontuação

    while not game_over:
        screen.fill((255, 255, 255))  # Limpa a tela

        # Captura dos eventos de teclado (movimento da cobra)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

        # Lógica para movimentar a cobra
        if direction == "LEFT":
            snake_x -= 20
        elif direction == "RIGHT":
            snake_x += 20
        elif direction == "UP":
            snake_y -= 20
        elif direction == "DOWN":
            snake_y += 20

        snake_head = (snake_x, snake_y)
        snake_body.append(snake_head)

        # Verifica se a cobra colidiu com as paredes ou com ela mesma
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0 or snake_head in snake_body[:-1]:
            game_over = True

        # Desenha a cobra
        draw_snake(snake_body)

        # Atualiza a tela
        pygame.display.update()

        # Controla a velocidade do jogo
        pygame.time.Clock().tick(15)  # Ajuste a velocidade do jogo

    # Enviar a pontuação ao backend Flask após o jogo terminar
    submit_score("Jogador1", score)  # Substitua por um nome de jogador dinâmico, se preferir
    pygame.quit()

# Iniciar o jogo
game_loop()
