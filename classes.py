import pygame
from pygame.locals import * 

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def fichier_reader(self):

		with open(self.fichier, "r") as fichier:
			colone_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les lettre contenus dans le fichier
				for lettre in ligne:
					#On ignore les "\n" de fin de ligne
					if lettre != '\n':
						#On ajoute la lettre à la liste de la ligne
						ligne_niveau.append(lettre)
				#On ajoute la ligne à la liste du niveau
				colone_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = colone_niveau
	
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure"""
		#téléchargement des images
		mur = pygame.image.load('./images/mur.png')
		Fire=pygame.image.load('./images/fire.png').convert()
		Fire.set_colorkey((255,255,255))
		arrive=pygame.image.load('./images/arrive.png').convert()
		arrive.set_colorkey((255,255,255))
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for lettre in ligne:
				#On calcule la position réelle en pixels
				x = num_case * 30
				y = num_ligne * 30
				#mur
				if lettre == 'm':		  
					fenetre.blit(mur, (x,y))
				#bombe
				elif lettre =='b':
					fenetre.blit(Fire,(x,y))
				#arrive
				elif lettre=='a':
					fenetre.blit(arrive,(x,y))
						
				num_case += 1
			num_ligne += 1


class Perso:
	"""Classe pour créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
	
		right=pygame.image.load('./images/2.png').convert()
		right.set_colorkey((255,255,255))
		self.droite = right
		left=pygame.image.load('./images/3.png').convert()
		left.set_colorkey((255,255,255))
		self.gauche =left
		down=pygame.image.load('./images/1.png').convert()
		down.set_colorkey((255,255,255))
		self.bas=down
		up=pygame.image.load('./images/1.png').convert()
		up.set_colorkey((255,255,255))
		self.haut=up
		
		#Position du personnage en cases et en pixels
		
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.bas
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
		
	
	
	def deplacer(self, direction):
		"""Methode déplacement dee personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < 20:
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm' and self.niveau.structure[self.case_y][self.case_x+1] != 'b':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * 30
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm' and self.niveau.structure[self.case_y][self.case_x-1] != 'b':
					self.case_x -= 1
					self.x = self.case_x * 30
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm' and self.niveau.structure[self.case_y-1][self.case_x] != 'b':
					self.case_y -= 1
					self.y = self.case_y * 30
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < 20:
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and self.niveau.structure[self.case_y+1][self.case_x] != 'b':
					self.case_y += 1
					self.y = self.case_y * 30
			self.direction = self.bas
	
