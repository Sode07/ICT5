import tkinter as tk
import winsound
import generate
from PIL import Image

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
