import pygame
import os
os.environ["SDL_AUDIODRIVER"] = "dsp"


pygame.init()

screen = pygame.display.set_mode([400, 400])