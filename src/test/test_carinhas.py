#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Jogo das Carinhas - Teste
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
import unittest
from carinhas import Carinhas

class TestCatinhas(unittest.TestCase):

    def setUp(self):
        class Gui(object):
            pass
            def __getitem__(self, x):
                return self
           
            def setAttribute(self, *x):
                self.opacity = 0.5
       
        self.gui = Gui()
        self.app = Carinhas(self.gui)

    def test_tabuleiro(self):
        "garante que tem casas no tabuleiro."
        self.app.build_tabuleiro(self.gui)
        t = self.app.tabuleiro
        self.assertEqual(len(t.casas),0)

if __name__ == '__main__':
    unittest.main()