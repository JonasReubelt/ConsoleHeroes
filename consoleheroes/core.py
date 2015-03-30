# coding=utf-8
# Filename: core.py
"""
Core classes and functions.

"""
from __future__ import division, absolute_import, print_function

__author__ = 'tamasgal'


class Player(object):
    """Represents the main character."""

    def __init__(self, name="Unnamed Hero"):
        self.name = name
        self.gold = 0

class Enemy(object):
    """Represents an enemy."""

    def __init__(self):
        pass
