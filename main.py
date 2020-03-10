import pygame
from image import *
from pygame.locals import *
from classes import *
pygame.init()

taille_fenetre=600
pygame.display.set_caption('megaman_x')

fenetre=pygame.display.set_mode((taille_fenetre,taille_fenetre))

game = True
#boucle principale
pygame.key.set_repeat(5,5)
while game:
    #initialiation de tous les compteurs de vies d enemies 
    compteur_cartouche_niveau2_2=0
    compteur_cartouche_niveau1=0
    compteur_cartouche_niveau2=0
    compteur_cartouche_niveau5_tank=0
    compteur_cartouche_niveau3_1=0
    compteur_cartouche_niveau3_2=0
    compteur_cartouche_niveau4_1=0
    compteur_cartouche_niveau4_2=0
    compteur_cartouche_niveau4_3=0
    compteur_cartouche_niveau5_1=0
    compteur_cartouche_niveau5_1_2=0
    compteur_cartouche_niveau5_1_3=0
    compteur_cartouche_niveau5_2_1=0
    compteur_cartouche_niveau5_2_2=0
    compteur_cartouche_niveau5_2_3=0
    compteur_cartouche_niveau5_3_1=0
    mouvement_planex=330
    mouvement_planex1=270
    mouvement_planey=360
    #fly mode for plane
    fly=True
    #fenetre de bienvenue dans le jeu
    fenetre.blit(acceuil,(0,0))
    pygame.display.flip()
    pygame.time.wait(3000)

    game_jeu = True
    game_accueil = True
    #fenetre des options
    fenetre.blit(option,(0,0))
    pygame.display.update()
    
    #boucle d'acceuil
    while game_accueil:
        

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                game_accueil = False
                game_jeu = False
                game = False
                by=pygame.image.load('./images/by.png')
                fenetre.blit(by,(0,0))
                pygame.display.update()
                pygame.time.wait(2000)
                #variable de choix du niveau
                choix = 0
            #choix des niveaux 
            elif event.type == KEYDOWN:             
                
                if event.key == K_F1:
                    game_accueil = False  
                    choix = './niveau/niveau1'       
                elif event.key == K_F2:
                    game_accueil = False
                    choix = './niveau/niveau2'
                elif event.key == K_F3:
                    game_accueil = False
                    choix = './niveau/niveau3'
                elif event.key == K_F4:
                    game_accueil = False
                    choix = './niveau/niveau4'
                elif event.key == K_F5:
                    game_accueil = False
                    choix = './niveau/niveau5'

    if choix != 0:
        
        fond = pygame.image.load('./images/Fond.png')
        #Génération d'un niveau à partir d'un fichier
        niveau = Niveau(choix)
        niveau.fichier_reader()
        niveau.afficher(fenetre)
        if choix != 0:
            perso=Perso("./images/2.png","./images/3.png","./images/1.png","./images/4.png",niveau)
     
    #boucle du jeu
    while game_jeu:

        ballex=perso.x+15
        balley=perso.y

        for event in pygame.event.get():

            if event.type == QUIT:
                game_jeu = False
                game = False
                by=pygame.image.load('./images/by.png')
                fenetre.blit(by,(0,0))
                pygame.display.update()
                pygame.time.wait(2000)
            
            if event.type == KEYDOWN:
                #si l'utilisateur presse Echap ici,retour au choix
                if event.key == K_ESCAPE:
                    game_jeu = False 
                #déplacement de megamax
                elif event.key == K_RIGHT:
                    perso.deplacer('droite')
                elif event.key ==K_LEFT:
                    perso.deplacer('gauche')
                elif event.key==K_DOWN:
                    perso.deplacer('bas')
                elif event.key==K_UP:
                    perso.deplacer('haut')
                    jump.play()
                #le tir 
                elif event.key==K_x:
                    cartouche.play()
                        
                    if perso.direction==perso.droite or perso.direction==perso.bas or perso.direction==perso.haut :
                        ballex=perso.x+10
                        while ballex <600:
                            ballex+=5
                            #le compteur de vie (enemies) pour le niveau1
                            if choix=='./niveau/niveau1': 
                                if ballex>390 and balley<120:
                                    compteur_cartouche_niveau1+=1
                            #le compteur de vie (enemies) pour le niveau2
                            elif choix=='./niveau/niveau2': 
                                if ballex>320 and ballex<340 and balley>170 and balley< 190:
                                    compteur_cartouche_niveau2+=1
                               
                            #le compteur de vie (enemies) pour le niveau3
                            if choix=='./niveau/niveau3':
                                if ballex>260 and balley>50 and balley<80:
                                    compteur_cartouche_niveau3_1+=1
                                elif balley>80:
                                    compteur_cartouche_niveau3_2+=1
                            #le compteur de vie (enemies) pour le niveau 4
                            if ballex>70 and choix=='./niveau/niveau4':
                                if balley>230:
                                    compteur_cartouche_niveau4_1+=1
                            if ballex>140 and choix=='./niveau/niveau4':
                                if balley>110 and balley<150:
                                    compteur_cartouche_niveau4_3+=1     
                            #le compteur de vie (enemies) pour le niveau 5
                            if choix=='./niveau/niveau5' and ballex>100:
                                if balley>250 and balley<290:
                                    compteur_cartouche_niveau5_1+=1
                                    compteur_cartouche_niveau5_1_2+=1
                                    compteur_cartouche_niveau5_1_3+=1
                                elif balley==300:
                                    compteur_cartouche_niveau5_2_1+=1
                                    compteur_cartouche_niveau5_2_2+=1
                                    compteur_cartouche_niveau5_2_3+=1
                            if choix=='./niveau/niveau5' and ballex>100:
                                if balley>300:
                                    compteur_cartouche_niveau5_3_1+=1
                            if ballex>430 and choix=='./niveau/niveau5':  
                                if balley>460 and balley< 600:
                                    compteur_cartouche_niveau5_tank+=1
                            fenetre.blit(balle,(ballex,balley))
                            pygame.display.flip()
                    elif perso.direction==perso.gauche:
                        ballex=perso.x-10
                        balley=perso.y
                        while ballex>0:
                            ballex-=10
                            #le compteur de vie enemie 2 pour le niveau2
                            if choix=='./niveau/niveau2' and ballex<200 and balley<200 and perso.direction==perso.gauche :
                                compteur_cartouche_niveau2_2+=1
                            fenetre.blit(balle1,(ballex,balley))
                            pygame.display.flip()
        
        
        fenetre.blit(fond, (0,0))
        niveau.afficher(fenetre)     
        #gerer les enemies dans le niveau1
        if choix=='./niveau/niveau1':
            if compteur_cartouche_niveau1<150:
                fenetre.blit(enemie,(410,60))
        #gerer les enemies dans le niveau2
        if choix=='./niveau/niveau2' :
            if compteur_cartouche_niveau2<20:
                fenetre.blit(enemie,(330,180))
            if compteur_cartouche_niveau2_2<50:
                fenetre.blit(Enemie,(90,180))
        #gerer les enemies dans le niveau3
        if choix=='./niveau/niveau3':
            if compteur_cartouche_niveau3_1<15:
                fenetre.blit(enemie,(270,60))
            if compteur_cartouche_niveau3_2<5:
                fenetre.blit(enemie,(270,90))
        #gerer les enemies dans le niveau4
        if choix=='./niveau/niveau4':
            if compteur_cartouche_niveau4_1<150:
                fenetre.blit(enemie,(90,240))
            if compteur_cartouche_niveau4_3<150:
                fenetre.blit(enemie,(150,120))
            if fly==True:
                mouvement_planey+=5
            if mouvement_planey==480:
                fly=False
                mouvement_planex-=0.3
               
                if perso.y==480:
                    
                    mouvement_planex-=50
                    if perso.y==mouvement_planey and mouvement_planex<30 and perso.x<60:
                        game_jeu=False
            if mouvement_planex<0:
                mouvement_planex=360

            if compteur_cartouche_niveau4_2<4:
                fenetre.blit(plane,(mouvement_planex,mouvement_planey))
        #gerer les enemies dans le niveau5
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_tank<900:
            fenetre.blit(tank,(450,480))
        if compteur_cartouche_niveau5_tank>100:
            tannk.play()
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_1<150:
            fenetre.blit(enemie,(210,270))
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_1_2<200:
            fenetre.blit(enemie,(240,270))
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_1_3<250:
            fenetre.blit(enemie,(270,270))
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_2_1<150:
            fenetre.blit(enemie,(210,300))
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_2_2<200:
            fenetre.blit(enemie,(240,300))
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_2_3<250:
            fenetre.blit(enemie,(300,300))
        if choix=='./niveau/niveau5' and compteur_cartouche_niveau5_3_1<150:
            fenetre.blit(enemie,(270,330))
        #l'image dans la bonne direction
        fenetre.blit(perso.direction, (perso.x, perso.y)) 
        pygame.display.flip()
        #quand le personnage arrive a l'arrivé ,retour au choix
        try:
            if niveau.structure[perso.case_x+1][perso.case_y+1]=='a' :
                game_jeu=False
        except IndexError:
            game_jeu=False
pygame.quit()