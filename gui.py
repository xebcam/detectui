import tkinter
from tkinter import filedialog, Text
from PIL import ImageTk, Image

root = tkinter.Tk()

def loadImage():
    global filename
    filename = filedialog.askopenfilename(initialdir = "./", title =    "Seleccionar Imagen", filetypes = [("images", "*.jpg *.png")])

def detect():
    filename = filedialog.askopenfilename(initialdir = "./", title =    "Seleccionar Imagen", filetypes = [("images", "*.jpg *.png")])

#canvas = tkinter.Canvas(root, height=480, width=720, bg="#ecf0f1")
#canvas.pack()
#
#frame = tkinter.Frame(root, bg="#9b59b6")
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

img = Image.open(filename)

resize_img = img.resize((300,300))

my_image = ImageTk.PhotoImage(resize_img)
label = tkinter.Label(image=my_image)
label.grid(row=0, column=0)

openFileButton = tkinter.Button(root, text="Abrir Archivo", padx=10, pady=10, fg="white", bg="#3498db", command=loadImage)
openFileButton.grid(row=1, column=0)

detectButton = tkinter.Button(root, text="Detectar", padx=10, pady=10, fg="white", bg="#3498db", command=detect)
detectButton.grid(row=1, column=1)

root.mainloop()
