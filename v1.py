import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((900, 600))
white = [255, 255, 255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
black = [0,0,0]
MenuColor = [200,200,200]
width = 900
height = 600
size = (width,height)

mousePos = (0,0) 


screen.fill(white)
botoesMenu=[]

def iniciaMenu():
	pygame.draw.rect(screen,(200,200,200),pygame.Rect(0,0,width,100)) # Menu cinza principal

	aux = (width//30)
	pygame.draw.rect(screen,black,pygame.Rect((width//30),(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,red,pygame.Rect((width//30),(width//30)+50,50,5))         # Botao Linha
	botoesMenu.append((aux,(width//30),(aux+50),(aux+50)))

	aux = (width//30)+100
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+100,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,red,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+200
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+200,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,red,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+300
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+300,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,red,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+400
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+400,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,red,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+500
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+500,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,red,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+600
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+600,(width//30),50,50))     # Botao Externo Linha
	pygame.draw.rect(screen,red,pygame.Rect(aux,(width//30)+50,50,5))
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))

	aux = (width//30)+700
	pygame.draw.rect(screen,black,pygame.Rect((width//30)+700,(width//30),50,50))     # Botao Externo Linha
	botoesMenu.append((aux,(width//30),(aux+50),(width//30)+50))



def muda_botao(pos):
	print(pos)
	if pos[1]<100:
		for i in range(len(botoesMenu)):
			aux = botoesMenu[i][0]
			if pos[0]>= botoesMenu[i][0] and pos[0]<=botoesMenu[i][2] and pos[1]>=botoesMenu[i][1] and pos[1]<=botoesMenu[i][3]:
					pygame.draw.rect(screen,green,pygame.Rect(aux,(width//30)+50,50,5))
					print("botao ",i, "mp - ",pos, " posBot - ",botoesMenu[i])
			else:
				pygame.draw.rect(screen,MenuColor,pygame.Rect(aux,(width//30)+50,50,5))
		pygame.display.update()		




iniciaMenu()
print(botoesMenu)



while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			muda_botao(pygame.mouse.get_pos())
		pygame.display.update()		

	pygame.display.update()		


