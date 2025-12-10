import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликни по шарику!")#настройки окна

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)#цвета


ball_x = 400
ball_y = 300
ball_radius = 50#параметры шарика


score = 0
font = pygame.font.SysFont(None, 48)#счёт


running = True #главный цикл
while running:
    for event in pygame.event.get():#обработка событий
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN: #клик мышкой
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            distance = ((mouse_x - ball_x) ** 2 + (mouse_y - ball_y) ** 2) ** 0.5#проверка, попали ли по шарику
            
            if distance <= ball_radius:
                score += 1
                ball_x = random.randint(ball_radius, WIDTH - ball_radius)#перемещаем шарик в случайное место
                ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
    
    screen.fill(WHITE)  #белый фон
    
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius) #шарик
    
    score_text = font.render(f"Счёт: {score}", True, BLUE)#отображает счет
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()

pygame.quit()
