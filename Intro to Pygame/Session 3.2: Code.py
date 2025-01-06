import pygame


pygame.init()

screen = pygame.display.set_mode((1024,576))
pygame.display.set_caption('This is a cool screen')
clock = pygame.time.Clock()

background = pygame.image.load("/Users/shivamsahu/Downloads/bgtutorial.png")
ground = pygame.image.load("/Users/shivamsahu/Downloads/groundtutorial.png")
font = pygame.font.Font(None,18)
text = font.render('Hello',False,'Red')
screen.fill('grey')
player = pygame.image.load("/Users/shivamsahu/Kabir Session 4/graphics/dragon.png")

player_pos_x = 50

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    player_pos_x += 4

    if player_pos_x > 1100: player_pos_x = -100
    screen.blit(background,(0,0))
    screen.blit(text,(100,100))
    screen.blit(player,(player_pos_x,50))
    



    pygame.display.update()
    #clock.tick(60)
