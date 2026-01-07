#-- Imports--#
import os
import pygame
from title_screen import TitleScreen
#-----------#

#game class --#
class game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1400, 800))
        pygame.display.set_caption("Naruto: The Game")
        self.state = "TITLE"
        self.title_screen = TitleScreen(self)
        #self.dungeon = Dungeon()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
    
    def handle_events(self):
        if self.state == "TITLE":
            self.title_screen.handle_events()
        elif self.state == "PLAY":
            # Handle play state events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
    
    def update(self):
        if self.state == "TITLE":
            self.title_screen.update()
        elif self.state == "PLAY":
            # Update play state
            pass
    
    def render(self):
        if self.state == "TITLE":
            self.title_screen.render()
        elif self.state == "PLAY":
            # Render play state
            self.screen.fill((50, 50, 50))
            font = pygame.font.Font(None, 48)
            text = font.render("Game Started! (Press ESC to quit)", True, (255, 255, 255))
            self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 
                                   self.screen.get_height() // 2))
            pygame.display.flip()

if __name__ == "__main__":
    g = game()
    g.run()