import pygame
import sys
from game_state import GameState
from player import Player
from config import *

def main():
    """Main game function"""
    try:
        # Initialize game state
        game = GameState()
        
        # Create player at center of screen
        player = Player(x=0, y=0)  # Temporary position, will be centered properly
        player.center_on_position(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        
        # Main game loop
        while game.running:
            # Handle events
            game.handle_events()
            
            # Handle player input
            keys = pygame.key.get_pressed()
            player.handle_input(keys)
            
            # Clear screen
            game.clear_screen()
            
            # Draw player
            player.draw(game.screen)
            
            # Update display
            game.update_display()
        
        # Clean up
        game.cleanup()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main() 