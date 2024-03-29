import pygame
import os

pygame.init()

# Constants for screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (4, 74, 61)
BUTTON_COLOR = (22, 104, 156)
BUTTON_TEXT_COLOR = (12, 70, 107)

# Directory containing music and album art files
MUSIC_DIRECTORY = "/Users/temirbekboltay/Desktop/lab-7/music"
ALBUM_ART_DIRECTORY = "/Users/temirbekboltay/Desktop/lab-7/Image/album_art"

# Initialize screen and font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 32)

# Fetch list of songs and album art files from directories
songs = [file for file in os.listdir(MUSIC_DIRECTORY) if file.endswith(".mp3")]
album_art_files = os.listdir(ALBUM_ART_DIRECTORY)

# Load album art images
album_art_images = [pygame.image.load(os.path.join(ALBUM_ART_DIRECTORY, filename)).convert() for filename in album_art_files]

# Initialize variables for current song index, paused state, and visualizer height
current_song_index = 0
paused = False
visualizer_height = 100

# Load the first song
pygame.mixer.music.load(os.path.join(MUSIC_DIRECTORY, songs[current_song_index]))
pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Toggle pause/play
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                # Play next song
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(os.path.join(MUSIC_DIRECTORY, songs[current_song_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                # Play previous song
                current_song_index = (current_song_index - 1) % len(songs)
                pygame.mixer.music.load(os.path.join(MUSIC_DIRECTORY, songs[current_song_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_ESCAPE:
                # Exit the program
                running = False

    # Update screen
    screen.fill(BACKGROUND_COLOR)
    
    # Display album art
    album_art = album_art_images[current_song_index]
    album_art_rect = album_art.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - visualizer_height // 2))
    screen.blit(album_art, album_art_rect)
    
    # Display song title
    song_title = font.render(songs[current_song_index], True, TEXT_COLOR)
    song_title_rect = song_title.get_rect(midtop=(SCREEN_WIDTH // 2, album_art_rect.bottom + 10))
    screen.blit(song_title, song_title_rect)

    # Display visualizer
    pygame.draw.rect(screen, BUTTON_COLOR, (0, SCREEN_HEIGHT - visualizer_height, SCREEN_WIDTH, visualizer_height))
    # Add code to draw visualizer bars based on audio amplitude

    # Display play/pause button
    play_pause_text = "Pause" if paused else "Play"
    play_pause_button = font.render(play_pause_text, True, BUTTON_TEXT_COLOR)
    play_pause_button_rect = play_pause_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - visualizer_height // 2))
    pygame.draw.rect(screen, BUTTON_COLOR, play_pause_button_rect, border_radius=10)
    screen.blit(play_pause_button, play_pause_button_rect)

    pygame.display.flip()

pygame.quit()

