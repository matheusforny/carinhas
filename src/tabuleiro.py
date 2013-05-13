#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Jogo das Carinhas - Tabuleiro
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
class Tabuleiro:
    """Campo do jogo onde se joga as pecas"""
    def __init__(self, gui):
        self.casas = []
