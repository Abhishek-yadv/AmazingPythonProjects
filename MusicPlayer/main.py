# Import necessary modules
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

# Create the main window
music_play = tk.Tk()
music_play.title("My Music Player")
music_play.geometry("450x350")
music_play.configure(bg='lightgrey')  # Set background color for the window

# Ask the user to select a directory
directory = askdirectory()
os.chdir(directory)  # Change the current working directory

# Get a list of songs in the directory
song_list = os.listdir()

# Create a Listbox to display the songs
play_list = tk.Listbox(music_play, font="Arial 12 bold", bg='green', selectmode=tk.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)  # Insert each song into the Listbox
    pos += 1

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Define functions to control the music playback
def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))  # Load the selected song
    var.set(play_list.get(tk.ACTIVE))  # Update the song title label
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause() 

def unpause():
    pygame.mixer.music.unpause()  


# Create buttons for controlling the music playback
Button1 = tk.Button(music_play, width=8, height=2, font="Arial 12 bold",text="PLAY", command=play, bg="green", fg="white")
Button2 = tk.Button(music_play, width=8, height=2, font="Arial 12 bold",text="STOP", command=stop, bg="red", fg="white")
Button3 = tk.Button(music_play, width=8, height=2, font="Arial 12 bold",text="PAUSE", command=pause, bg="blue", fg="white")
Button4 = tk.Button(music_play, width=8, height=2, font="Arial 12 bold",text="UNPAUSE", command=unpause, bg="black", fg="white")

# Create a label to display the current song title
var = tk.StringVar()
song_title = tk.Label(music_play, font="Arial 12 bold", textvariable=var)

# Pack the widgets into the window
song_title.pack(pady=10)
play_list.pack(fill="both", expand="yes", padx=10, pady=5)
Button1.pack(side="left", padx=10, pady=5)
Button2.pack(side="left", padx=10, pady=5)
Button3.pack(side="left", padx=10, pady=5)
Button4.pack(side="left", padx=10, pady=5)

# Start the main event loop
music_play.mainloop()
