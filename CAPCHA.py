import pygame
import os
import random

pygame.init()

info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("CAPTCHA Verification")

# Load CAPTCHA images from a directory
captcha_directory = "./CAPCHA"
captcha_images = [img for img in os.listdir(captcha_directory) if img.endswith('.png')]

# Function to get a random CAPTCHA
def get_random_captcha():
    return random.choice(captcha_images)

# Function to display CAPTCHA and verify input
def run_captcha():
    running = True
    captcha_image_name = get_random_captcha()
    captcha_image_path = os.path.join(captcha_directory, captcha_image_name)
    captcha_answer = os.path.splitext(captcha_image_name)[0]  # Remove file extension

    # Load the CAPTCHA image
    captcha_image = pygame.image.load(captcha_image_path)
    
    # User input for verification
    user_input = ""
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape to exit
                    running = False
                elif event.key == pygame.K_RETURN:  # Check the input
                    if user_input == captcha_answer:
                        print("CAPTCHA Verified!")
                        running = False  # Exit the loop if verified
                    else:
                        print("Incorrect CAPTCHA. Try again!")
                        user_input = ""  # Clear input for retry
                elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                    user_input = user_input[:-1]
                else:
                    # Add the character to the user input
                    user_input += event.unicode

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the CAPTCHA image
        screen.blit(captcha_image, (info.current_w // 2 - captcha_image.get_width() // 2,
                                     info.current_h // 2 - captcha_image.get_height() // 2))

        # Render the user input
        font = pygame.font.Font(None, 36)
        text_surface = font.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface, (info.current_w // 2 - text_surface.get_width() // 2,
                                    info.current_h // 2 + captcha_image.get_height() // 2 + 20))

        pygame.display.flip()

    pygame.quit()

# Run the CAPTCHA
run_captcha()

