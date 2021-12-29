import pygame, time, random



pygame.font.init()
fonte=pygame.font.Font("freesansbold.ttf", 20)         
nave = pygame.image.load("nave.png")
nave_inimiga = pygame.image.load("naveini.png")
planeta = pygame.image.load("planeta.png")

screen = pygame.display.set_mode((980, 700))
pygame.display.set_caption("Guardian(fraco)")
pygame.display.set_icon(nave)
running = True

WHITE = (255,255,255)
YELLOW = (255,255,0)
YELLOW_ =(238,173,45)
BLACK = (0,0,0)
GREEN = (0,128,0)

# Bullet
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x+25, y-10]


    def update(self):
        self.rect.y -= 0.5
        if self.rect.bottom <= 65:
            self.kill()

#criar class para novos bixos da nave       

bullet_group = pygame.sprite.Group()


x_ini, y_ini = random.randint(100,700), random.randint(50,100)
v_enemy = 0.17
x_NAVE, y = 465, 450
score_v = 0
x_pla ,y_plan, x1_plan,x2_plan = 940, 570, 1300, 1660
textx_Sco, texty_Sco = 445, 680
x_speed , y_speed = 890,5
def speed(x,y):
    speed = fonte.render(str(speedi),True,GREEN)
    screen.blit(speed,(x,y))
def score(x,y): # score
    score = fonte.render("Score: " + str(score_v),True,BLACK)
    screen.blit(score,(x,y))
def enemy(x,y): # nave inimiga
    screen.blit(nave_inimiga,(x,y))
def planet(x,y): # planeta
    screen.blit(planeta,(x,y))


velocidade = 0.75 # velocidade # CRIAR 5 NIVEIS DE VELOCIDADE(colocar speed)
velocidade_planeta = 0.25
while running:
    screen.blit(nave,(x_NAVE,y))
    for event in pygame.event.get():
        time1x = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and velocidade < 1.54:
                velocidade += 0.20
            if event.key == pygame.K_s and velocidade > 0.75:
                velocidade -= 0.20
            if event.key == pygame.K_SPACE:
                x_centro = x_NAVE
                bullet = Bullets(x_centro,450)
                bullet_group.add(bullet)
                
    teclas = pygame.key.get_pressed()
    if True: #teclas
        if teclas[pygame.K_a]:
            x_NAVE -= velocidade
        if teclas[pygame.K_d]: 
            x_NAVE += velocidade 
        if x_NAVE >= 930:
            x_NAVE = 930
        if x_NAVE <= 0:
            x_NAVE = 0   
        if teclas[pygame.K_1]: # resetar velocidade
            velocidade = 0.75
    if True: #linhas
       # pygame.draw.line(screen,WHITE, [0,626],[980,626],150)
        pygame.draw.line(screen, YELLOW, [0, 550], [980, 550], 5)
        pygame.draw.line(screen, YELLOW_, [0, 690], [980, 690], 30)
    if True: #planetas
        if x_pla < -125:
            x_pla = 940
        if x1_plan < -125:
            x1_plan = 940
        if x2_plan < -125:
            x2_plan = 940
    if True: #enemy movimento       
        v_enemy *= 1.0001
        if v_enemy >= 0.45:
            a = random.randint(1,3)
            if a > 1:
                v_enemy = 0.25
            else:
                v_enemy = 0.14
        if x_ini <= 0:
           v_enemy = -v_enemy
        if x_ini >= 780:
           v_enemy = -v_enemy
        x_ini -= v_enemy 
    if True: #speed
        if velocidade == 0.75:
            speedi = "Speed: 1"
        if velocidade == 0.95 :
            speedi = "Speed: 2"
        if velocidade == 1.15:
            speedi = "Speed: 3"
        if round(velocidade,2) == 1.35:
            speedi = "Speed: 4"
        if round(velocidade,2) == 1.55:
            speedi = "Speed: 5"
    bullet_group.update()
    #bullet movement
    bullet_group.draw(screen)

    x_pla -= velocidade_planeta
    x1_plan -= velocidade_planeta
    x2_plan -= velocidade_planeta
    #velocidade_planeta *= 1.000005
    speed(x_speed,y_speed)
    planet(x_pla,y_plan)
    planet(x1_plan,y_plan)
    planet(x2_plan,y_plan)
    enemy(x_ini,y_ini)                                                                             
    score(textx_Sco,texty_Sco)          
    pygame.display.update()                          
    screen.fill(BLACK)
    
