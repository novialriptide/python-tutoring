import pygame
import random

pygame.init()

window = pygame.display.set_mode((420, 420))
font = pygame.font.SysFont("Comic Sans", 20)

game_over = False

class CountDownTimer:
    def __init__(self, ms):
        self.ms = ms + pygame.time.get_ticks()

    def get_time(self):
        return (self.ms - pygame.time.get_ticks()) / 1000

t = CountDownTimer(5000)
boxes = []
points = 0
box_size = 30

class Box:
    def __init__(self, position):
        self.position = position
        self.rect = pygame.Rect(self.position.x, self.position.y, box_size, box_size)

def spawn_box():
    global boxes
    
    pos = pygame.Vector2(random.randint(0, 420 - box_size), random.randint(0, 420 - box_size))
    boxes.append(Box(pos))

spawn_box()

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse_position = pygame.mouse.get_pos()

    if not game_over:
        timer_time = t.get_time()
        window.fill((21, 21, 21))
        window.blit(font.render(f"time left: {timer_time}", True, (69, 69, 69)), (0, 0))
        window.blit(font.render(f"points: {points}", True, (69, 69, 69)), (0, 30))
        
        if timer_time < 0:
            game_over = True
        
        for b in boxes[:]:
            pygame.draw.rect(window, (255, 255, 255), b)
            
            if b.rect.collidepoint(mouse_position):
                points += 1
                boxes.remove(b)
                for i in range(random.randint(1, 2)):
                    spawn_box()
    
    if game_over:
        window.fill((21, 21, 21))
        window.blit(font.render("haha game over", True, (69, 69, 69)), (0, 0))
        window.blit(font.render(f"points: {points}", True, (69, 69, 69)), (0, 30))
    
    pygame.display.update()