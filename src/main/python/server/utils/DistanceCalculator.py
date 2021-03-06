import math

class Point(object):

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y

def calcularProximidadeEntreDoisPontos(ponto1, ponto2, arrayPontos, tamanhoMapa):
    
    coeficienteDeDistancia = 0.6
    
    minimoX = tamanhoMapa
    maximoX = 0
    minimoY = tamanhoMapa
    maximoY = 0
    
    for ponto in arrayPontos:
        if(ponto.x > maximoX):
            maximoX = ponto.x
        if(ponto.x < minimoX):
            minimoX = ponto.x
        if(ponto.y > maximoY):
            maximoY = ponto.y
        if(ponto.y < minimoY):
            minimoY = ponto.y
            
    raioDeDistanciaX = 2 + (math.fabs(maximoX - minimoX) * coeficienteDeDistancia)
    raioDeDistanciaY = 2 + (math.fabs(maximoY - minimoY) * coeficienteDeDistancia)
    
    if(math.fabs(ponto1.x - ponto2.x) <= raioDeDistanciaX):
        print("Estao proximos verticalmente")
        if(math.fabs(ponto1.y - ponto2.y) <= raioDeDistanciaY):
            print("Estao proximos horizontalmente")
        else:
            print("Estao longe horizontalmente")
    else:
        print("Estao longe verticalmente")