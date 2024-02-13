import tkinter as tk
from hexagonal_grid import HexagonalGrid
import load
import renderer
import movement
import gui
import turn_handler
import os
from PIL import Image
from checkwinstate import voitto

def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def scale_image_to_screen(input_image_path, output_image_path):
    screen_width, screen_height = get_screen_size()
    
    # Open the input img
    image = Image.open(input_image_path)
    #Calc img future size
    scale_factor_width = screen_width / image.width
    scale_factor_height = screen_height / image.height
    scale_factor = min(scale_factor_width, scale_factor_height)
    
    # Resize the image
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    resized_image = image.resize((new_width, new_height))
    
    # Save the resized image
    resized_image.save(output_image_path)

input_path = "tausta.webp"
output_path = "peli.png"

scale_image_to_screen(input_path, output_path)

a = 1

def b():
    print("peli tuhottu")
    global a
    a = 0
    exit()
def c():
    os.system("python win.py")
    b()
filename = "save.csv"

# Create Tkinter window
root = tk.Tk()
root.attributes('-fullscreen', True)
background_image = tk.PhotoImage(file="peli.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Create HexagonalGrid instance
grid = HexagonalGrid(root, scale=20, grid_width=50, grid_height=25)
grid.grid(row=0, column=0, padx=5, pady=5)

# Load grid from CSV using grid_loader
load.load_grid_from_csv(grid, filename)
gui.baseUI(root, filename)
renderer.render_unit(grid, filename)
renderer.render_city(grid, filename)
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=2) 
# Bind the canvas to the select_unit function
grid.bind("<Button-1>", lambda event: movement.select_unit(event, grid, filename, root))
# Bind the right-click event to the move_unit function
grid.bind("<Button-3>", lambda event: movement.move_unit(event, grid, filename, turn_handler.get_current_turn(filename), root))
# Run Tkinter event loop
QuitButton = tk.Button(button_frame, text="Quit", command=lambda: b())
QuitButton.grid(row=0, column=0, padx=10, pady=10)
if voitto(filename, 45,11, 45, 13):
    c()
root.mainloop()
while a:
    print(a)
    os.system("python game.py")