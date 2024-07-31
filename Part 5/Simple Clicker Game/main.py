import pygame
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        # https://www.geeksforgeeks.org/mmouse-clicks-on-sprites-in-pygame/
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
        self.visible = True
        
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()
clicks = 0
def on_click():
    global clicks
    clicks += 1

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init()


screen = pygame.display.set_mode((300,300))
sprite = ClickableSprite(pygame.Surface((100,100)), 100, 100, on_click)
group = pygame.sprite.GroupSingle(sprite)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    group.update(events)
    screen.fill((255,255,255))
    text_surface = my_font.render(str(clicks), False, (0,0,0))
    screen.blit(text_surface,(140,50))
    
    if sprite.visible:
        group.draw(screen)
    pygame.display.update()
pygame.quit()    
    