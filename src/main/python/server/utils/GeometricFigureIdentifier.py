import math

class Point(object):

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y

def calcularFiguraGeometrica(arrayDePontos):
    
    distanciaEntrePontos = distanciaEntrePontosAtual = 0
    result = True
    
    for x in range(0, len(arrayDePontos)):
        
        if((x + 1) < (len(arrayDePontos))):
            distanciaEntrePontosAtual = calculoDistanciaEntrePontos(arrayDePontos[x], arrayDePontos[x+1])
        else:
            distanciaEntrePontosAtual = calculoDistanciaEntrePontos(arrayDePontos[x], arrayDePontos[0])
            
        if(distanciaEntrePontos == 0):
            distanciaEntrePontos = distanciaEntrePontosAtual
        elif(distanciaEntrePontosAtual != distanciaEntrePontos):
            result = False
            break
            
    return result
            
            
def calculoDistanciaEntrePontos(ponto1, ponto2):
    
    print (math.floor(math.sqrt((ponto1.x - ponto2.x)**2 + (ponto1.y - ponto2.y)**2)))
    return math.floor(math.sqrt((ponto1.x - ponto2.x)**2 + (ponto1.y - ponto2.y)**2))