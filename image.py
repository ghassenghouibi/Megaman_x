import pygame

pygame.init()


ecran =pygame.display.set_mode((600,600))
acceuil=pygame.image.load('./images/Intro.png')
Take=pygame.image.load('./images/fond3.png')
Fond=pygame.image.load('./images/Fond.png')
Kill=pygame.image.load('./images/fond2.png')
perso=pygame.image.load('./images/1.png').convert()
perso.set_colorkey((255,255,255))
perso1=pygame.image.load('./images/2.png').convert()
mur = pygame.image.load('./images/mur.png')
Fire=pygame.image.load('./images/fire.png').convert()
Fire.set_colorkey((255,255,255))
Enemie=pygame.image.load('./images/enemie.png').convert()
Enemie.set_colorkey((255,255,255))
tank=pygame.image.load('./images/tank.png').convert()
tank.set_colorkey((255,255,255))
plane=pygame.image.load('./images/plane1.png').convert()
plane.set_colorkey((255,255,255))
enemie=pygame.image.load('./images/enemies.png').convert()
enemie.set_colorkey((255,255,255))
killing=pygame.image.load('./images/lol.png')
balle=pygame.image.load('./images/bullet.png').convert()
balle.set_colorkey((255,255,255))
balle1=pygame.image.load('./images/bulet.png').convert()
balle1.set_colorkey((255,255,255))
acceuil=pygame.image.load('./images/Intro.png')
option=pygame.image.load('./images/insctructions.png')
son = pygame.mixer.Sound("./son/son.ogg")
jump=pygame.mixer.Sound("./son/jump.wav")
cartouche=pygame.mixer.Sound("./son/death.wav")
tannk=pygame.mixer.Sound("./son/tank.wav")