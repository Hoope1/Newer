# edge_gui_tiles_kornia.py – Teil 1/4

import os
import torch
import torchvision.transforms as T
import kornia as K
import cv2
import numpy as np
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
from PIL import Image
import threading

# CUDA-Kontext vorbereiten
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# GUI Klasse
class EdgeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kornia Kantenerkennung (Tile-Modus für DexiNed)")

        tk.Label(root, text="Wähle einen Bild-Ordner:").pack(pady=5)

        self.select_button = tk.Button(root, text="Ordner wählen", command=self.select_folder)
        self.select_button.pack()

        self.progress = ttk.Progressbar(root, length=400)
        self.progress.pack(pady=10)

        self.status = tk.Label(root, text="")
        self.status.pack()

    def select_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        self.status.config(text="Verarbeite Bilder...")
        self.progress["value"] = 0
        threading.Thread(target=self.run_processing, args=(folder,), daemon=True).start()

    def run_processing(self, folder):
        from edge_processing import process_folder
        def update_progress(done, total):
            percent = int((done / total) * 100)
            self.progress["value"] = percent
            self.status.config(text=f"{done}/{total} Bilder verarbeitet")
        process_folder(folder, update_progress)
        self.status.config(text="Fertig!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EdgeApp(root)
    root.mainloop()
