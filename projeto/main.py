import pygame, time
pygame.font.init()
fonte=pygame.font.Font("freesansbold.ttf", 20)         
nave = pygame.image.load("nave.png")
screen = pygame.display.set_mode((980, 700))
pygame.display.set_caption("Guardian(fraco)")
running = True
WHITE = (255,255,255)
YELLOW = (255,255,0)
YELLOW_ =(238,173,45)
x = 465
y = 450
score_v = 0
textx_Sco = 445
texty_Sco = 680
def score(x,y): # score
    score = fonte.render("Score: " + str(score_v),True,(0,0,0))
    screen.blit(score,(x,y))
   
velocidade = 1 # velocidade
while running:
    pygame.time.delay(3)
    screen.blit(nave,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    teclas = pygame.key.get_pressed()
    if True: #teclas
        if teclas[pygame.K_a]:
            x -= velocidade
        if teclas[pygame.K_d]:
            x += velocidade 
        if teclas[pygame.K_UP]:
            velocidade += 0.05
        if teclas[pygame.K_DOWN]:
            velocidade -= 0.05
        if teclas[pygame.K_1]:
            velocidade = 1
    if True: #linhas
       # pygame.draw.line(screen,WHITE, [0,626],[980,626],150)
        pygame.draw.line(screen, YELLOW, [0, 550], [980, 550], 5)
        pygame.draw.line(screen, YELLOW_, [0, 690], [980, 690], 30)

    
                                                                                    
    score(textx_Sco,texty_Sco)          
    pygame.display.update()                          
    screen.fill((0,0,0))
    

