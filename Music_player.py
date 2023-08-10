
import os
import pygame
import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedStyle

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x150")

        # Add a style with a theme
        style = ThemedStyle(root)
        style.set_theme("clam")

        pygame.init()
        pygame.mixer.init()

        # Create buttons and volume control
        self.play_button = ttk.Button(root, text="Play", command=self.play_music, style="TButton")
        self.play_button.pack(pady=20)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_music, style="TButton")
        self.stop_button.pack(pady=5)

        self.pause_button = ttk.Button(root, text="Pause", command=self.pause_music, style="TButton")
        self.pause_button.pack(pady=5)

        self.resume_button = ttk.Button(root, text="Resume", command=self.resume_music, style="TButton")
        self.resume_button.pack(pady=5)

        self.volume_label = ttk.Label(root, text="Volume")
        self.volume_label.pack()

        self.volume_scale = tk.Scale(root, from_=0, to=1, resolution=0.1, orient="horizontal", command=self.set_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack()

        # Get the current working directory
        self.current_directory = os.getcwd()

    def play_music(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_directory, title="Select Music",
                                               filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*")))
        if file_path:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def set_volume(self, value):
        volume = float(value)
        pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
