import pygame

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music Player")

songs = ["1.mp3", "2.mp3", "3.mp3"]
music_directory = "/Users/temirbekboltay/Desktop/lab-7/music/"
i = 0

font = pygame.font.Font(None, 32)
pause_text = font.render("PAUSED", True, (255, 0, 0))
x, y = pause_text.get_rect().center

pygame.mixer.music.load(music_directory + songs[i])
pygame.mixer.music.play()

paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            elif event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(music_directory + songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(music_directory + songs[i])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    song_title = font.render(songs[i], True, (0, 0, 0))
    screen.blit(song_title, (10, 10))
    if paused or not pygame.mixer.music.get_busy():
        screen.blit(pause_text, (320 - x, 240 - y))
    pygame.display.update()

pygame.quit()
