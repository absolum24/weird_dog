import pygame
import sys
from config import *

class GameState:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self._initialize_pygame()
    
    def _initialize_pygame(self):
        """Initialize pygame and create the game window"""
        try:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.display.set_caption(WINDOW_TITLE)
            self.clock = pygame.time.Clock()
            
            if not self.screen or not self.clock:
                raise RuntimeError("Failed to initialize pygame display or clock")
                
        except Exception as e:
            print(f"Error initializing pygame: {e}")
            pygame.quit()
            sys.exit(1)
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def clear_screen(self):
        """Clear the screen with white background"""
        if self.screen:
            self.screen.fill(WHITE)
    
    def update_display(self):
        """Update the display and control frame rate"""
        pygame.display.flip()
        if self.clock:
            self.clock.tick(FPS)
    
    def cleanup(self):
        """Clean up pygame resources"""
        try:
            pygame.quit()
        except:
            pass  # pygame might already be quit
        sys.exit() 