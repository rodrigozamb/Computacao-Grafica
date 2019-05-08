import pygame
import math
import sys
from primitivas import * 

#inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((900, 600))
screen.fill([255, 255, 255])

#cores
white = [255, 255, 255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
black = [0,0,0]
listaCores = [black,red,blue,green,white,(128,0,128),(255,20,147),(255,255,0),(0,255,255),(255,0,255),(128,128,128),(210,105,30),(56,176,222),(1,250,42),(255,215,0),(180,82,205)]
colorNum = 0
MenuColor = [200,200,200]

#janela
width = 900
height = 600
size = (width,height)

#variaveis de controle
mousePos = (0,0) 
botoesMenu=[]
primitivas = ['Linha','Retângulo','Quadrado','Círculo','Polilinha','Curva'] # relação numerica de cada primitiva
primitivaNum = 0; 
click_on = False
#menu = pygame.surface.Surface((900,100))


def iniciaMenu():
	global colorNum
	pygame.draw.rect(screen,(200,200,200),pygame.Rect(0,0,width,100)) # Menu cinza principal

	aux = (width//30)
	pygame.draw.rect(screen,black,pygame.Rect((width//30),(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,green,pygame.Rect((width//30),(width//30)+50,50,5))         # Botao Linha
	botoesMenu.append((aux,(width//30),(aux+50),(aux+50)))

	aux = (width//30)+100
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+100,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+200
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+200,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+300
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+300,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+400
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+400,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+500
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+500,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+600
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+600,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+700
	pygame.draw.rect(screen,listaCores[colorNum],pygame.Rect((width//30)+700,(width//30),50,50))     # Botao Externo Linha
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))
	
	#screen.set_clip((0,0,0,100))
	#screen.set_clip((0,100,900,600))

def muda_botao(pos):
	global primitivaNum
	global colorNum
	print(pos)
	a=-1


	for i in range(len(botoesMenu)):
		
		if pos[0]>= botoesMenu[i][0] and pos[0]<=botoesMenu[i][2] and pos[1]>=botoesMenu[i][1] and pos[1]<=botoesMenu[i][3]:
			a=i;
			if i != 7:
				primitivaNum = i					
	
	if(a==7):
		colorNum+=1
		if(colorNum == len(listaCores)):
			colorNum = 0
		aux = (width//30)+700
		pygame.draw.rect(screen,listaCores[colorNum],pygame.Rect((width//30)+700,(width//30),50,50))     # Botao Externo Linha

	elif (a!=-1):
		for i in range(len(botoesMenu)-1):
			aux = botoesMenu[i][0]
			if a==i:
				pygame.draw.rect(screen,green,pygame.Rect(aux,(width//30)+50,50,5))
			else:
				pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
	pygame.display.update()		

def desenha_linha(pos):
	deafultBack = screen.copy()
	while 1:
		for e in pygame.event.get():

			print("desenhando... ",click_on)
			x,y = pygame.mouse.get_pos()
			screen.blit(deafultBack,(0,0))
			linha(pos[0],pos[1],x,y,listaCores[colorNum])
		
			if(e.type == pygame.MOUSEBUTTONUP):
				return
		
def desenha_retangulo(pos):
	deafultBack = screen.copy()
	while 1:
		for e in pygame.event.get():
			x,y = pygame.mouse.get_pos()
			screen.blit(deafultBack,(0,0))
			retangulo(pos[0],pos[1],x,y,listaCores[colorNum])

			if(e.type == pygame.MOUSEBUTTONUP):
				return

def desenha_quadrado(pos):
	deafultBack = screen.copy()
	while 1:
		for e in pygame.event.get():
			x,y = pygame.mouse.get_pos()
			screen.blit(deafultBack,(0,0))

			##PEDIR PRO JUSTINO ME EXPLICAR ISSO DE SIGNAL E DAS COORDENADAS DE PARAMETRO
			signal = abs(y - pos[1]) // (y - pos[1]) if y != pos[1] else 1
			if(x<pos[0]):
				signal *=-1
			quadrado(pos[0],pos[1],x,pos[1] + ((x - pos[0]) * signal),listaCores[colorNum])

			if(e.type == pygame.MOUSEBUTTONUP):
				return

def desenha_circulo(pos):
	deafultBack = screen.copy()
	while 1:
		for e in pygame.event.get():
			x,y = pygame.mouse.get_pos()
			screen.blit(deafultBack,(0,0))
			raio = int( math.sqrt( ((x - pos[0]) ** 2) + ((y - pos[1]) ** 2) ) )
			#if r > start[0] - (screen_size[0] >> 2):
			#    r = start[0] - (screen_size[0] >> 2)
			circulo(pos[0], pos[1], raio, listaCores[colorNum])

			if(e.type == pygame.MOUSEBUTTONUP):
				return

def desenha_polilinha():
	while 1:
		for e in pygame.event.get():
			if(e.type == pygame.MOUSEBUTTONDOWN):
				poli_aux(pygame.mouse.get_pos())
				return

def poli_aux(pos):
	deafultBack = screen.copy()
	while 1:
		for e in pygame.event.get():

			print("desenhando... ",click_on)
			x,y = pygame.mouse.get_pos()
			screen.blit(deafultBack,(0,0))
			linha(pos[0],pos[1],x,y,listaCores[colorNum])
		
			if(e.type == pygame.MOUSEBUTTONDOWN):
				pygame.display.update()
				deafultBack = screen.copy()	
				pos=(x,y)
				aux = pygame.mouse.get_pressed()
				if aux[2]==1:
					return


def click_handle(pos):
	if(pos[1] <= 100):
		muda_botao(pos)
	elif(primitivaNum == 4):
		poli_aux(pos)
	if(primitivaNum == 0):
		desenha_linha(pos)
	if(primitivaNum == 1):
		desenha_retangulo(pos)
	if(primitivaNum == 2):
		desenha_quadrado(pos)
	if(primitivaNum == 3):
		desenha_circulo(pos)
	#if(primitivaNum == 5):       FALTA FAZER
	#	preenche(pos)
	



iniciaMenu()
print(botoesMenu)



while 1 :

	mousePos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			click_on = True
			click_handle(mousePos)
		

	
	pygame.display.update()		


