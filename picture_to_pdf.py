from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a Picture file", filetypes=[("PNG files", "*.png"),("JPG files", "*.jpg"),("JPEG files", "*.jpeg")])
    return file_path

def picture_to_pdf(png_file_path):
    pdf_file_path = os.path.splitext(png_file_path)[0] + ".pdf"
    with Image.open(png_file_path) as im:
        im.save(pdf_file_path, "PDF", resolution=100.0)

# Beispiel Aufruf des Skripts
png_file_path = select_file()
if png_file_path:
    picture_to_pdf(png_file_path)
