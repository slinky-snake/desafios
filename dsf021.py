import pygame
pygame.init()
print('olá, eu sou um mp3 player')#nenhuma musica funcionou
pygame.mixer.music.load('nous deux.mp3')
pygame.mixer.music.play()
pygame.event.wait()

