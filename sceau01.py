#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# prend une pelle et un sceau
import tkinter as tk
from tkinter import simpledialog, filedialog
from PIL import Image, ImageDraw, ImageFont

# Créer une fenêtre Tkinter
root = tk.Tk()
root.withdraw()  # Ne pas afficher la fenêtre Tkinter


# Demander le chemin de l'image
chemin_image = filedialog.askopenfilename(title="Sélectionnez une image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

# Ouvrir l'image
image = Image.open(chemin_image)
draw = ImageDraw.Draw(image)



# Ouvrir l'image modifiée
image.show()
