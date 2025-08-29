import pygame

def run():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Snake — skeleton")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    run()
