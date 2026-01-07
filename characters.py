#-- Imports --#
import pygame
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
