#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Jogo das Carinhas - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Otavio Meirelles*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/10
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from tabuleiro import Tabuleiro
from random import random
class Carinhas:
    """Base do jogo com tabuleiro e carinhas."""
    def __init__(self, gui):
        """Constroi os objetos iniciais. """
        self.urls= ['https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_verdes_sem_bigode_II.png?disp=inline&size=G', 
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_verdes_com_barba_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_pretos_sem_barba_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_pretos_com_barba_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_verdes_sem_bigode.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_verdes_com_bigode.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_pretos_sem_bigode.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_pretos_com_bigode.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_sem_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_com_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_sem_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_com_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_com_bigode_(2).png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_sem_barba.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_sem_barba.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_com_bigode.png?disp=inline&size=G']
        self.d = 'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/tabuleiro.png?disp=inline&size=G' 
    def numeros(self, quantidade, bonecos):
        lista = []
        for a, qnti in enumerate(quantidade):
            for b in range(qnti):
                lista.append(bonecos[a])
        return (lista)


    def shufle(self, lista ):
        listainterna = lista[:]
        lista_saida = []
 
        while listainterna:
            indice_selecionado = int(random() * (len(listainterna)))
            elemento_selecionado = listainterna.pop(indice_selecionado)
            lista_saida.append(elemento_selecionado)
            lista = lista_saida[:]
        print(lista_saida)
        return(lista_saida)
         
  
    def build_base(self,gui, svg):
        """Constroi as partes do Jogo. """
        p = gui['banner']
        self.s = svg.svg(width = 800, height=500) 
        p <= self.s
        self.gui = gui
        #self.build_tabuleiro(gui)
        self.build_carinhas(svg)
    def build_tabuleiro(self,gui,lista):
        """Constroi o tabuleiro onde as pecas sao jogadas."""
        self.tabuleiro = [] #Tabuleiro(gui)
        c=0
        for i in range(12):
            interna = []
            for a in range(16):
                if (i<2) or (i>9):            
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50 , width=50, height=50))  
                    self.s<=interna[a]
                    c+=1
                elif (i==2) and (a==0) :
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50 , width=50, height=50))  
                    self.s<=interna[a]
                    c+=1
                elif (i==2) and (a==1) :
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50 , width=50, height=50))  
                    self.s<=interna[a]
                    c+=1
                elif (a==14) and (i==2):
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50 , width=50, height=50))  
                    self.s<=interna[a]
                    c+=1
                else :
                    interna.append(gui.image(href=self.d, x=a*50, y=i*50 , width=50, height=50))  
                    self.s<=interna[a]
            self.tabuleiro.append(interna)
    def build_carinhas(self,gui):
        """Posiciona as carinhas onde as pecas se iniciam."""
        qnt =[3, 4, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 2, 2, 4, 5] #67

        carinhas_ordenadas = self.numeros(qnt, self.urls)
        carinhas_embaralhadas = self.shufle(carinhas_ordenadas)
        self.build_tabuleiro(gui, carinhas_embaralhadas)

 
def main(doc,svg):
  print('Carinhas 0.1.0')
  carinhas =  Carinhas(doc)
  carinhas.build_base(doc,svg)

