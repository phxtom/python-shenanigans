import pygame
import time
import random

# Infinite metal pipe clanking sound periodically interrupted by silence

pygame.mixer.init()

clank_sound = pygame.mixer.Sound("clanker.mp3")

print("This program will play an infinite metal pipe clanking sound periodically interrupted by silence.")

time.sleep(1)

running = input("Type 'y' to start the infinite pipe clanking sound, or 'CTRL + C' to exit (Control + C on Mac):\n")

if running == "y":
    print("...")
    while running == "y":
        clank_sound.play()
        time.sleep(0.2) # Play every 0.2 seconds

        if random.random() < 0.05:  # 5% chance for silence
            clank_sound.stop()
            time.sleep(3)  # Pause between clanks