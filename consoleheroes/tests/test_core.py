# coding=utf-8
# Filename: test_core.py
"""
Unit tests for core.py

"""
from __future__ import division, absolute_import, print_function

__author__ = 'tamasgal'

from unittest import TestCase

from consoleheroes.core import Player, Enemy


class TestPlayer(TestCase):
    """Tests for the Player class"""

    def test_init(self):
        player = Player()

    def test_init_with_name(self):
        player = Player("foo")
        self.assertEqual("foo", player.name)

    def test_initial_gold(self):
        player = Player()
        self.assertEqual(0, player.gold)


class TestEnemy(TestCase):
    """Tests for the Enemy class"""

    def test_init(self):
        enemy = Enemy()
