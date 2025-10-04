import pygame
import time
import random

pygame.mixer.init()

clank_sound = pygame.mixer.Sound("clanker.mp3")

print("This program will play an infinite silence occasionally interrupted by a metal pipe clanking sound.")

time.sleep(1)

running = input("Type 'y' to start the infinite pipe clanking sound, or 'CTRL + C' to exit (Control + C on Mac):")

if running == "y":
    while running == "y":
        clank_sound.play()
        time.sleep(random.randint(5, 900))  # Random delay between clanks