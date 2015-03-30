# coding=utf-8
# Filename: test_core.py
"""
Unit tests for core.py

"""
from __future__ import division, absolute_import, print_function

__author__ = 'tamasgal'

from unittest import TestCase

from consoleheroes.core import Player

class TestPlayer(TestCase):
    """Tests for the Player class"""

    def test_init(self):
        player = Player()

