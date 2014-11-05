#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Carinhas
# Copyright 2013-2014 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Carinhas é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser  útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
#  a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, escreva para a Fundação do Software
# Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
############################################################
Jogo das Carinhas - Teste
############################################################

Verifica a funcionalidade do cliente web.

"""
import unittest
from random import shuffle
from client.caras.carinhas import Carinhas
from client.caras import main


class CarinhasTest(unittest.TestCase):

    def setUp(self):
        class Gui(object):
            def __getitem__(self, x):
                return self
           
            def __le__(self, *x):
                pass

            def setAttribute(self, *x):
                self.opacity = 0.5

            def image(self, *x, **kw):
                return self

            def svg(self, *x, **kw):
                return self
       
        self.gui = Gui()
        self.app = Carinhas(self.gui)

    def test_tabuleiro(self):
        """garante que tem casas no tabuleiro."""
        casas = list(range(16))
        shuffle(casas)
        self.app.build_base(self.gui, self.gui)
        t = self.app.tabuleiro
        self.assertEqual(len(t), 12)
        self.assertEqual(len(t[0]), 16)

    def test_monta_tabuleiro(self):
        """garante que tem carinhas no tabuleiro."""
        self.app.s = self.gui
        self.app.build_tabuleiro(self.gui, self.gui)
        t = self.app.tabuleiro
        self.assertEqual(len(t), 12)
        self.assertEqual(len(t[0]), 16)

    def test_main(self):
        """garante que main coloca carinhas no tabuleiro."""
        carinhas = main(self.gui, self.gui)
        t = carinhas.tabuleiro
        self.assertEqual(len(t), 12)
        self.assertEqual(len(t[0]), 16)


if __name__ == '__main__':
    unittest.main()