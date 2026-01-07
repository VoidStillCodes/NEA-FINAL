#-- Imports --#
import pygame
from main import game
#-------------#

# TitleScreen class --#
class TitleScreen:
    def __init__(self, game):
        self.screen = pygame.display.set_mode((1400, 800))
        self.game = game
        self.menu_options = ["Start Game", "Load Game", "Options", "Exit"]
        self.title_font = pygame.font.Font("Ariel", 74)
        self.option_font = pygame.font.Font("Ariel", 36)
    
    def run(self):
        self.handle_events()
        self.update()
        self.render()
        pass
        
    
    def handle_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.game.running = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    self.game.state = "PLAY"
    
    def update(self):
        
        pass
    
    def render(self):
        self.screen.fill((0, 0, 0))
        title_text = self.title_font.render("Naruto: The Game", True, (255, 255, 255))
        self.screen.blit(title_text, (1400 // 2 - title_text.get_width() // 2, 100))
        for i, option in enumerate(self.menu_options):
            option_text = self.option_font.render(option, True, (255, 255, 255))
            self.screen.blit(option_text, (1400 // 2 - option_text.get_width() // 2, 300 + i * 60))
        pygame.display.flip()