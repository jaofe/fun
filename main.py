import time
import pygame
import os
import random
import keyboard
import sys

WAIT_TIME = 1800

def capcha():
    pygame.init()

    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption("CAPTCHA Verification")

    # Update path for PyInstaller
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundled executable
        base_path = sys._MEIPASS
    else:
        # If run normally (e.g., in an IDE)
        base_path = os.path.abspath(".")

    captcha_directory = os.path.join(base_path, "CAPCHA")
    
    # Hard-code the number of CAPTCHA images
    captcha_count = 1040

    # Function to get a random CAPTCHA image without listing all
    def get_random_captcha():
        random_index = random.randint(0, captcha_count - 1)
        return os.listdir(captcha_directory)[random_index]

    def block_keys():
        keyboard.block_key('alt')
        keyboard.block_key('tab')
        keyboard.block_key('windows')
        keyboard.block_key('esc')
        keyboard.block_key('ctrl')

    def unblock_keys():
        keyboard.unblock_key('alt')
        keyboard.unblock_key('tab')
        keyboard.unblock_key('windows')
        keyboard.unblock_key('esc')
        keyboard.block_key('ctrl')

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

        block_keys()

        try:
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:  # Verify input
                            if user_input == captcha_answer:
                                print("CAPTCHA Verified!")
                                running = False  # Exit the loop if verified
                            else:
                                user_input = ""  # Clear input for a new attempt
                        elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                            user_input = user_input[:-1]
                        elif event.unicode.isalnum():  # Allow only letters and numbers
                            user_input += event.unicode

                # Move rendering inside the main loop
                screen.fill((0, 0, 0))
                screen.blit(captcha_image, (info.current_w // 2 - captcha_image.get_width() // 2,
                                            info.current_h // 2 - captcha_image.get_height() // 2))
                font = pygame.font.Font(None, 36)
                text_surface = font.render(user_input, True, (255, 255, 255))
                screen.blit(text_surface, (info.current_w // 2 - text_surface.get_width() // 2,
                                           info.current_h // 2 + captcha_image.get_height() // 2 + 20))
                pygame.display.flip()
        finally:
            unblock_keys()

        pygame.quit()

    # Run the CAPTCHA
    run_captcha()


def run_script():
    while True:
        # Execute the CAPCHA.py script
        capcha()
        
        time.sleep(WAIT_TIME)

if __name__ == '__main__':
    run_script()
