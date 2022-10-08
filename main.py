import sys, pygame, utils.util

pygame.init()

size = width, height = 1920, 1080
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
simple_font = pygame.font.Font(None, 50);
# title = pygame.image.load("Title Logo.png")
# titlerect = title.get_rect()

text_surfaces_L = list()
text_surfaces_R = list()
line = simple_font.render('_'*190, False, 'Gray')
for key, value in utils.util.read_text_to_dict().items():
    text_surfaces_L.append(simple_font.render(key, False, 'White'))
    text_surfaces_R.append(simple_font.render(value, False, 'White'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
    

    # DO ACTIONS
    screen.fill((0,0,0))

    for index, surface in enumerate(text_surfaces_L):
        screen.blit(surface, (200, 300+60*index))
        screen.blit(line, (0, 312+60*index))

    for index, surface in enumerate(text_surfaces_R):
        screen.blit(surface, (1520, 300+60*index))
    # screen.blit(title, titlerect)

    # Render Frame
    pygame.display.flip()
    clock.tick(60)