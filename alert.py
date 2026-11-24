import pygame
import os

class AlertSystem:
    def __init__(self, sound_path):
        self.enabled = False
        if os.path.exists(sound_path):
            try:
                pygame.mixer.init()
                self.sound = pygame.mixer.Sound(sound_path)
                self.enabled = True
            except Exception as e:
                print(f"⚠️ Audio output unavailable ({e}), alerts will be visual only")
        else:
            print("⚠️ Alarm sound not found, alerts will be silent")

    def play(self):
        if self.enabled:
            self.sound.play()
