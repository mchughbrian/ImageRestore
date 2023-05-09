import cv2
import numpy as np
import torch
import torchvision
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk

def open_image():
    global img, gray, restored_image

    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Restore the image
        restored_image = restore_image(gray)

        # Display the original and restored images
        display_images(gray, restored_image)

def display_images(original_image, restored_image):
    global original_photo, restored_photo

    original_photo = ImageTk.PhotoImage(image=Image.fromarray(original_image))
    original_label.config(image=original_photo)
    original_label.image = original_photo

    restored_photo = ImageTk.PhotoImage(image=Image.fromarray(restored_image))
    restored_label.config(image=restored_photo)
    restored_label.image = restored_photo

def save_image():
    global restored_image

    if restored_image is not None:
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            cv2.imwrite(save_path, restored_image)

# Initialize the Tkinter window
root = Tk()
root.title("Image Restoration")

# Create the Open button
open_button = Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create the original and restored image labels
original_label = Label(root)
original_label.pack(side="left")
restored_label = Label(root)
restored_label.pack(side="left")

# Create the Save button
save_button = Button(root, text="Save Restored Image", command=save_image)
save_button.pack()

# Run the Tkinter main loop
root.mainloop()


#assess the image quality to see what model we should run
#explain what psnr is here
def compute_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr


