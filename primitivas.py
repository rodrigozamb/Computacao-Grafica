import pygame

size = (900, 600)
white=[255,255,255]
black=[0,0,0]


pygame.init()
screen = pygame.display.set_mode(size)


def _linhaH(x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0
    for x in range(dx):
        screen.set_at((x + x0, y), color)
        if D > 0:
            y = y + yi
            D = D - 2*dx
        D = D + 2*dy


def _linhaV(x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0
    for y in range(dy):
        screen.set_at((x, y + y0), color)
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx


def segmento_reta(x0, y0, x1, y1, color):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            _linhaH(x1, y1, x0, y0, color)
        else:
            _linhaH(x0, y0, x1, y1, color)
    else:
        if y0 > y1:
            _linhaV(x1, y1, x0, y0, color)
        else:
            _linhaV(x0, y0, x1, y1, color)


def linha(x0, y0, x1, y1, color):
    segmento_reta(x0, y0, x1, y1, color)
    pygame.display.flip()


def circulo(x0, y0, r, color):
    global db
    x = 0
    y = r
    d = 1 - r
    circulo_aux (x, y, x0, y0, color)
    while y > x :
        if d < 0 :
            d = d + ( 2 * x ) + 3
        else:
            d = d + 2 * ( x - y ) + 5
            y = y - 1
        x = x + 1
        circulo_aux(x, y, x0, y0, color)
    pygame.display.flip()
    

def circulo_aux(x, y, x0, y0, color):
    screen.set_at((x + x0, y + y0), color)
    screen.set_at((x0 - y, x + y0), color)
    screen.set_at((x0 - y, y0 - x), color)
    screen.set_at((x0 - x, y0 - y), color)
    screen.set_at((x0 - x, y + y0), color)
    screen.set_at((x + x0, y0 - y), color)
    screen.set_at((y + x0, y0 - x), color)
    screen.set_at((y + x0, x + y0), color)

def retangulo(x, y, w, h, color):
    segmento_reta(x, y, w, y, color)
    segmento_reta(w, y, w, h, color)
    segmento_reta(w, h, x, h, color)
    segmento_reta(x, h, x, y, color)
    pygame.display.flip()

def quadrado(x, y, w, h, color):
    segmento_reta(x, y, w, y, color)
    segmento_reta(w, y, w, h, color)
    segmento_reta(w, h, x, h, color)
    segmento_reta(x, h, x, y, color)
    pygame.display.flip()


