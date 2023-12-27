from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

def crop_matrix(matrix, left, right, top, bottom):
    cropped_matrix = matrix[top:-bottom, left:-right, :]
    return cropped_matrix

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file dialog to select an image file
image_path = filedialog.askopenfilename(title='Select an image file')

if image_path:
    image = Image.open(image_path)
    image = image.convert("RGBA")  # Convert to RGBA mode

    image_matrix = np.array(image)

    print("Original Image Matrix:")
    print(image_matrix)

    left = int(input("Enter the number of columns to crop from the left: "))
    right = int(input("Enter the number of columns to crop from the right: "))
    top = int(input("Enter the number of rows to crop from the top: "))
    bottom = int(input("Enter the number of rows to crop from the bottom: "))

    cropped_matrix = crop_matrix(image_matrix, left, right, top, bottom)

    print("\nCropped Image Matrix:")
    print(cropped_matrix)

    # Open a file dialog to save the cropped image
    save_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG', '*.png'), ('JPEG', '*.jpg;*.jpeg')])

    if save_path:
        cropped_image = Image.fromarray(cropped_matrix)
        cropped_image.save(save_path)
        print(f"Cropped image saved at: {save_path}")

        original_image = Image.open(image_path)
        original_image.show(title='Original Image')
        cropped_image.show(title='Cropped Image')

        cropped_image_matrix = np.array(cropped_image)
        print("\nCropped Image Matrix:")
        print(cropped_image_matrix)