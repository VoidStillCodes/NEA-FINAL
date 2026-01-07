#-- Imports --#
import pygame
from main import game
from dungeon import Dungeon
from characters import Shinobi
#--------------#
# PlayScreen class --#
class PlayScreen:
    def __init__(self):
        self.game = game
        self.dungeon = Dungeon()
        self.player = Shinobi()
        pass