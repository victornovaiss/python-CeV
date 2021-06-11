import pygame 
import os

path = os.getcwd() + "\exercicios\ex021.mp3"

pygame.init()
pygame.mixer.music.load(path)
pygame.mixer.music.play()
pygame.event.wait()

input('Aperte Enter para parar a música')