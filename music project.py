import os
import pygame
from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("Advanced Music Player")

# Initialize Pygame Mixer
pygame.mixer.init()

# Track Information Variables
current_song = StringVar()
current_song.set("No Song")
current_artist = StringVar()
current_artist.set("No Artist")
current_album = StringVar()
current_album.set("No Album")

# Song List
song_list = []
song_listbox = Listbox(root, selectmode=SINGLE, font=("Arial", 12), width=50, height=20)
song_listbox.pack(padx=10, pady=10)

# Functions
def add_songs():
    songs = filedialog.askopenfilenames(filetypes=[("ALL Files", "*.mp3")])
    for song in songs:
        song_list.append(song)
        song_name = os.path.basename(song)
        song_listbox.insert(END, song_name)

def play_song():
    selected_song = song_listbox.curselection()
    if selected_song:
        song_index = selected_song[0]
        song_path = song_list[song_index]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        update_track_info(song_path)

def stop_song():
    pygame.mixer.music.stop()
    current_song.set("No Song")
    current_artist.set("No Artist")
    current_album.set("No Album")

def update_track_info(song_path):
    try:
        tags = pygame.mixer.music.get_tags()
        current_song.set(tags["title"])
        current_artist.set(tags["artist"])
        current_album.set(tags["album"])
    except:
        current_song.set(os.path.basename(song_path))
        current_artist.set("Unknown Artist")
        current_album.set("Unknown Album")

def next_song():
    selected_song = song_listbox.curselection()
    if selected_song:
        current_index = selected_song[0]
        if current_index < len(song_list) - 1:
            song_listbox.selection_clear(0, END)
            song_listbox.selection_set(current_index + 1)
            song_listbox.activate(current_index + 1)
            play_song()

def previous_song():
    selected_song = song_listbox.curselection()
    if selected_song:
        current_index = selected_song[0]
        if current_index > 0:
            song_listbox.selection_clear(0, END)
            song_listbox.selection_set(current_index - 1)
            song_listbox.activate(current_index - 1)
            play_song()

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

add_button = Button(button_frame, text="Add Songs", command=add_songs)
add_button.pack(side=LEFT, padx=5)

play_button = Button(button_frame, text="Play", command=play_song)
play_button.pack(side=LEFT, padx=5)

stop_button = Button(button_frame, text="Stop", command=stop_song)
stop_button.pack(side=LEFT, padx=5)

next_button = Button(button_frame, text="Next", command=next_song)
next_button.pack(side=LEFT, padx=5)

previous_button = Button(button_frame, text="Previous", command=previous_song)
previous_button.pack(side=LEFT, padx=5)

# Track Information
track_info_frame = Frame(root)
track_info_frame.pack(pady=10)

song_label = Label(track_info_frame, textvariable=current_song, font=("Arial", 14, "bold"))
song_label.pack()

artist_label = Label(track_info_frame, textvariable=current_artist, font=("Arial", 12))
artist_label.pack()

album_label = Label(track_info_frame, textvariable=current_album, font=("Arial", 12))
album_label.pack()

root.mainloop()
