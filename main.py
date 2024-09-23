import datetime
import pygame
import time
# import customtkinter

# app = customtkinter.CTk()
# app.mainloop()

while True:
    now = datetime.datetime.now()
    if f'{now.hour}:{now.minute}' == "5:50":
        for i in range(0, 20):
            pygame.mixer.init()
            pygame.init()
            pygame.mixer.music.load('Vegas - Good Things (Original Mix).mp3')
            pygame.mixer.music.play()
            time.sleep(60)
        break
