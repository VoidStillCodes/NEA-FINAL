#-- Imports --#
import pygame
import random 
#-------------#

#-- Character class --#
class Shinobi:
    def __init__(self):
        self.name = ""
        self.village = ""
        self.nature_type = ""
        self.clan = ""
        self.stats = None
        self.Inventory = []
        self.Jutsu = []
        self.position = (0,0)
        #metadata
        self.health = 100
        self.exp = 0
        self.level = 1
        self.xp_to_next_level = 100
        self.max_health = 100
        self.chakra = 100
        self.max_chakra = self.chakra
    
    def move(self):
        pass 
    
    def use_Jutsu(self):
        pass
    
    def take_damage(self):
        pass
#---------------------#
class Enemy:
    def __init__(self):
        pass
    
    def update(self):
        pass
    
    def attack(self):
        pass 
