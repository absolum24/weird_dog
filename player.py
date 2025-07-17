import pygame
import random
from config import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.flipped_image = None  # Store flipped version of the image
        self.eat_image = None
        self.eat_flipped_image = None
        self.sit_image = None
        self.sit_flipped_image = None
        self.christmas_image = None
        self.christmas_flipped_image = None
        self.christmas_eat_image = None
        self.christmas_eat_flipped_image = None
        self.sign_image = None
        self.sign_flipped_image = None
        self.width = FALLBACK_PLAYER_SIZE
        self.height = FALLBACK_PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.facing_right = True  # Track which direction the dog is facing
        self.eating = False  # Track if the dog is eating
        self.eat_timer = 0  # Timer for eating state
        self.sitting = False  # Track if the dog is sitting
        self.random_move = False  # Track if the dog is moving randomly
        self.rand_dx = 0  # Random movement direction x
        self.rand_dy = 0  # Random movement direction y
        self.christmas_mode = False  # Track if Christmas mode is active
        self.sign_mode = False  # Track if sign mode is active
        self._load_images()
    
    def _load_images(self):
        """Load and scale the dog images"""
        try:
            # Load the original image
            original_image = pygame.image.load("dog.png")
            original_width = original_image.get_width()
            original_height = original_image.get_height()
            # Calculate new dimensions
            self.width = int(original_width * PLAYER_SCALE_FACTOR)
            self.height = int(original_height * PLAYER_SCALE_FACTOR)
            # Scale the image
            self.image = pygame.transform.scale(original_image, (self.width, self.height))
            # Create flipped version of the image
            self.flipped_image = pygame.transform.flip(self.image, True, False)
            # Load and scale the eating image
            try:
                eat_image = pygame.image.load("dog_eats.png")
                eat_image = pygame.transform.scale(eat_image, (self.width, self.height))
                self.eat_image = eat_image
                self.eat_flipped_image = pygame.transform.flip(eat_image, True, False)
            except pygame.error:
                self.eat_image = None
                self.eat_flipped_image = None
            # Load and scale the Christmas image
            try:
                christmas_image = pygame.image.load("dog_christmas.png")
                christmas_image = pygame.transform.scale(christmas_image, (self.width, self.height))
                self.christmas_image = christmas_image
                self.christmas_flipped_image = pygame.transform.flip(christmas_image, True, False)
            except pygame.error:
                self.christmas_image = None
                self.christmas_flipped_image = None
            # Load and scale the Christmas eating image
            try:
                christmas_eat_image = pygame.image.load("dog_eats_christmas.png")
                christmas_eat_image = pygame.transform.scale(christmas_eat_image, (self.width, self.height))
                self.christmas_eat_image = christmas_eat_image
                self.christmas_eat_flipped_image = pygame.transform.flip(christmas_eat_image, True, False)
            except pygame.error:
                self.christmas_eat_image = None
                self.christmas_eat_flipped_image = None
            # Load and scale the sitting image
            try:
                sit_image = pygame.image.load("dog_sit.png")
                sit_image = pygame.transform.scale(sit_image, (self.width, self.height))
                self.sit_image = sit_image
                self.sit_flipped_image = pygame.transform.flip(sit_image, True, False)
            except pygame.error:
                self.sit_image = None
                self.sit_flipped_image = None
            # Load and scale the sign image
            try:
                sign_image = pygame.image.load("dog_sign.png")
                sign_image = pygame.transform.scale(sign_image, (self.width, self.height))
                self.sign_image = sign_image
                self.sign_flipped_image = pygame.transform.flip(sign_image, True, False)
            except pygame.error:
                self.sign_image = None
                self.sign_flipped_image = None
            print(f"Dog images loaded successfully. Size: {self.width}x{self.height}")
        except pygame.error:
            print("Error: Could not load dog.png. Make sure the file exists in the same folder.")
            print("Using fallback red rectangle.")
            self.image = None
            self.flipped_image = None
            self.eat_image = None
            self.eat_flipped_image = None
            self.christmas_image = None
            self.christmas_flipped_image = None
            self.christmas_eat_image = None
            self.christmas_eat_flipped_image = None
            self.sit_image = None
            self.sit_flipped_image = None
            self.sign_image = None
            self.sign_flipped_image = None
            self.width = FALLBACK_PLAYER_SIZE
            self.height = FALLBACK_PLAYER_SIZE
    
    def center_on_position(self, x, y):
        """Center the player on the given position"""
        self.x = x - self.width // 2
        self.y = y - self.height // 2
    
    def handle_input(self, keys):
        """Handle player movement, eating, sitting, random, Christmas, and sign state based on key presses"""
        now = pygame.time.get_ticks()
        # Toggle Christmas mode on C press (on key down, not hold)
        if hasattr(self, '_last_c'):
            last_c = self._last_c
        else:
            last_c = False
        if keys[pygame.K_c] and not last_c:
            self.christmas_mode = not self.christmas_mode
        self._last_c = keys[pygame.K_c]
        # Sign mode: pressing P sets sign mode, any other action unsets it
        if hasattr(self, '_last_p'):
            last_p = self._last_p
        else:
            last_p = False
        if keys[pygame.K_p] and not last_p:
            self.sign_mode = True
        elif (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_e] or keys[pygame.K_r] or keys[pygame.K_f] or keys[pygame.K_c]):
            self.sign_mode = False
        self._last_p = keys[pygame.K_p]
        # Random movement state: pressing F sets random, any other action unsets it
        if keys[pygame.K_f]:
            if not self.random_move:
                # Pick a random direction (not zero)
                while True:
                    self.rand_dx = random.choice([-1, 0, 1])
                    self.rand_dy = random.choice([-1, 0, 1])
                    if self.rand_dx != 0 or self.rand_dy != 0:
                        break
                self.random_move = True
            # Cancel eating if F is pressed
            self.eating = False
            self.eat_timer = 0
        elif keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_r] or keys[pygame.K_e]:
            self.random_move = False
        # Sitting state: pressing R sets sitting, any other action (including E) unsets it
        if keys[pygame.K_r]:
            self.sitting = True
            # Cancel eating if R is pressed
            self.eating = False
            self.eat_timer = 0
        elif keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_f] or keys[pygame.K_e]:
            self.sitting = False
        # Eating state: pressing E starts eating for 4 seconds, any other action cancels it
        if keys[pygame.K_e] and not self.sitting and not self.random_move:
            if not self.eating:
                self.eating = True
                self.eat_timer = now
        elif (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_r] or keys[pygame.K_f]) and self.eating:
            self.eating = False
            self.eat_timer = 0
        # Handle eating timer
        if self.eating and self.eat_timer:
            if now - self.eat_timer >= 4000:
                self.eating = False
                self.eat_timer = 0
        # Only allow movement if not sitting, not random, and not eating
        if not self.sitting and not self.random_move and not self.eating:
            if keys[pygame.K_a] and self.x > 0:  # A key - move left
                self.x -= self.speed
                self.facing_right = False  # Face left
            if keys[pygame.K_d] and self.x < WINDOW_WIDTH - self.width:  # D key - move right
                self.x += self.speed
                self.facing_right = True   # Face right
            if keys[pygame.K_w] and self.y > 0:  # W key - move up
                self.y -= self.speed
            if keys[pygame.K_s] and self.y < WINDOW_HEIGHT - self.height:  # S key - move down
                self.y += self.speed
        elif self.random_move and not self.sitting and not self.eating:
            # Move randomly, bounce off edges
            next_x = self.x + self.rand_dx * self.speed
            next_y = self.y + self.rand_dy * self.speed
            bounced = False
            if next_x < 0 or next_x > WINDOW_WIDTH - self.width:
                self.rand_dx *= -1
                bounced = True
            if next_y < 0 or next_y > WINDOW_HEIGHT - self.height:
                self.rand_dy *= -1
                bounced = True
            if bounced:
                next_x = self.x + self.rand_dx * self.speed
                next_y = self.y + self.rand_dy * self.speed
            self.x = max(0, min(WINDOW_WIDTH - self.width, next_x))
            self.y = max(0, min(WINDOW_HEIGHT - self.height, next_y))
            # Update facing direction
            if self.rand_dx < 0:
                self.facing_right = False
            elif self.rand_dx > 0:
                self.facing_right = True
    
    def draw(self, screen):
        """Draw the player on the screen"""
        # Choose which image to draw
        img = None
        img_flipped = None
        if self.sitting and self.sit_image and self.sit_flipped_image:
            img = self.sit_image
            img_flipped = self.sit_flipped_image
        elif self.eating:
            # Use Christmas eating image if in Christmas mode and available
            if self.christmas_mode and self.christmas_eat_image and self.christmas_eat_flipped_image:
                img = self.christmas_eat_image
                img_flipped = self.christmas_eat_flipped_image
            elif self.eat_image and self.eat_flipped_image:
                img = self.eat_image
                img_flipped = self.eat_flipped_image
        elif self.sign_mode and self.sign_image and self.sign_flipped_image:
            img = self.sign_image
            img_flipped = self.sign_flipped_image
        elif self.christmas_mode and self.christmas_image and self.christmas_flipped_image:
            img = self.christmas_image
            img_flipped = self.christmas_flipped_image
        elif self.image and self.flipped_image:
            img = self.image
            img_flipped = self.flipped_image
        if img and img_flipped:
            if self.facing_right:
                screen.blit(img, (self.x, self.y))
            else:
                screen.blit(img_flipped, (self.x, self.y))
        else:
            # Draw fallback red rectangle
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        """Get the player's rectangle for collision detection"""
        return pygame.Rect(self.x, self.y, self.width, self.height) 
