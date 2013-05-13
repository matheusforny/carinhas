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
if not '__package__' in dir():
    import svg
from tabuleiro import Tabuleiro
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
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/olhos_pretos_com_bigode.png?disp=inline&size=G']
        
        self.urls2 = ['https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_sem_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_com_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_sem_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_com_bigode_II.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_com_bigode_(2).png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_verdes_sem_barba.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_sem_barba.png?disp=inline&size=G',
       'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/chapeu_olhos_pretos_com_bigode.png?disp=inline&size=G']
    def build_base(self,gui):
        """Constroi as partes do Jogo. """
        p = gui['banner']
        self.s = svg.svg(width = 800, height=5000) 
        p <= self.s
        self.gui = gui
        self.build_tabuleiro(gui)
        self.build_carinhas(gui)
    def build_tabuleiro(self,gui):
        """Constroi o tabuleiro onde as pecas sao jogadas."""
        self.tabuleiro = Tabuleiro(gui)
    def build_carinhas(self,gui):
        """Posiciona as carinhas onde as pecas se iniciam."""
        qnt = [3, 4, 4, 5, 5, 5, 4, 5] #35
        qnt2 = [5, 5, 5, 4, 2, 2, 4, 5] #32
 
        contador = 0
        for i, url in enumerate(self.urls):
            b = qnt[i]
            for a in range(b):
                c=svg.image(href=url, x=0, y=contador*80, width = 42, height = 76)
                contador = contador + 1
                self.s<=c
         
        contador = i = a= 0
        for i, url in enumerate(self.urls2):
            b = qnt2[i]
            for a in range(b):
                c=svg.image(href=url, x=80, y=contador*80, width=54.6, height=98.8)
                contador = contador + 1
                self.s<=c
 
def main(doc):
  print('Carinhas 0.1.0')
  carinhas =  Carinhas(doc)
  carinhas.build_base(doc)

