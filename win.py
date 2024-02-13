import tkinter as tk
import winsound
import generate
from PIL import Image

def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def scale_image_to_screen(input_image_path, output_image_path):
    screen_width, screen_height = get_screen_size()
    
    # Open the input image
    image = Image.open(input_image_path)
    
    # Calculate scaling factors for width and height
    scale_factor_width = screen_width / image.width
    scale_factor_height = screen_height / image.height
    
    # Choose the smaller scaling factor to fit the image on screen
    scale_factor = min(scale_factor_width, scale_factor_height)
    
    # Resize the image
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    resized_image = image.resize((new_width, new_height))
    
    # Save the resized image
    resized_image.save(output_image_path)

# Example usage
input_path = "voitto.webp"
output_path = "voitto.png"

scale_image_to_screen(input_path, output_path)
root = tk.Tk()

winsound.PlaySound('voitto.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
for widget in root.winfo_children():
    widget.destroy()
root.attributes("-fullscreen", True)
background_image = tk.PhotoImage(file="voitto.png")
background_image = background_image.subsample(background_image.width() // root.winfo_screenwidth(), background_image.height() // root.winfo_screenheight())
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.mainloop()
