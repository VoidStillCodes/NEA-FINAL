#-- Imports --#
import pygame
#-------------#

# TitleScreen class --#
class TitleScreen:
    def __init__(self, game):
        self.game = game
        self.menu_options = ["Start Game", "Load Game", "Options", "Exit"]
        self.selected_option = 0
        # Use None for default pygame font, or provide a path to a .ttf file
        self.title_font = pygame.font.Font(None, 74)
        self.option_font = pygame.font.Font(None, 36)
        self.selected_color = (255, 215, 0)  # Gold for selected option
        self.normal_color = (255, 255, 255)  # White for normal options
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                elif event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()
    
    def select_option(self):
        if self.selected_option == 0:  # Start Game
            self.game.state = "PLAY"
        elif self.selected_option == 1:  # Load Game
            print("Load Game not implemented yet")
        elif self.selected_option == 2:  # Options
            print("Options not implemented yet")
        elif self.selected_option == 3:  # Exit
            self.game.running = False
    
    def update(self):
        pass
    
    def render(self):
        self.game.screen.fill((0, 0, 0))
        
        # Render title
        title_text = self.title_font.render("Naruto: The Game", True, (255, 140, 0))
        title_rect = title_text.get_rect(center=(self.game.screen.get_width() // 2, 100))
        self.game.screen.blit(title_text, title_rect)
        
        # Render menu options
        for i, option in enumerate(self.menu_options):
            color = self.selected_color if i == self.selected_option else self.normal_color
            option_text = self.option_font.render(option, True, color)
            option_rect = option_text.get_rect(center=(self.game.screen.get_width() // 2, 300 + i * 60))
            self.game.screen.blit(option_text, option_rect)
        
        # Render instructions
        instruction_font = pygame.font.Font(None, 24)
        instruction_text = instruction_font.render("Use UP/DOWN arrows and ENTER to select", True, (150, 150, 150))
        instruction_rect = instruction_text.get_rect(center=(self.game.screen.get_width() // 2, 
                                                             self.game.screen.get_height() - 50))
        self.game.screen.blit(instruction_text, instruction_rect)
        
        pygame.display.flip()