import sys, pygame, utils.util

pygame.init()

# Config settings
size = width, height = 1920, 1080

top_offset = 100
line_offset = 12
lr_margin = 50

line_color = pygame.Color('#DAA520')
text_color = pygame.Color('#FFFFFF')
bg_color = pygame.Color('#174A43')

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()

text_and_cost = utils.util.read_text_to_dict().items()
rule_size = (height-top_offset) // len(text_and_cost)
font_size = round(rule_size * .84)
simple_font = pygame.font.Font(None, font_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()

    screen.fill(bg_color)


    for index, (surface_l, surface_r) in enumerate(text_and_cost):
        # right align rect
        right_text = simple_font.render(surface_r, False, text_color)
        temp_rect = right_text.get_rect()
        temp_rect.topright = (width-lr_margin, top_offset + rule_size * index)

        screen.blit(simple_font.render(surface_l, False, text_color), (lr_margin, top_offset + rule_size * index))
        screen.blit(right_text, temp_rect)
        screen.blit(simple_font.render('_' * 255, False, line_color), (0, top_offset+line_offset + rule_size * index))

    # Render Frame
    pygame.display.flip()
    clock.tick(1)
