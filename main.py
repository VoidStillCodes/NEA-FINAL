#-- Imports--#
import os
import pygame
#-----------#
#game class --#
class game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.state = ""
        #self.dungeon = Dungeon()
    
    def run(self):
        
        pass 
    
    def change_state(self):
        if self.state == "PLAY":
            pass 
        elif self.state == "TITLE":
            pass
        pass 
    
    def handle_events(self):
        pass
    
    def update(self):
        pass 
    
    def render(self):
        pass