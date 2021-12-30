import tkinter
from tkinter import filedialog, Text
from PIL import ImageTk, Image

root = tkinter.Tk()

frame = tkinter.LabelFrame(root, text="Imagen Original", padx=10, pady=10)
frame.grid(row=0, column=0, padx = 10, pady = 10)

frame1 = tkinter.LabelFrame(root, text="Deteccion", font = ("arial", 50), padx=10, pady=10)
frame1.grid(row=0, column=1, padx = 10, pady = 10)

label = tkinter.Label(frame)
label1 = tkinter.Label(frame1)

def loadImage():
    global img
    label.pack_forget()

    filename = filedialog.askopenfilename(initialdir = "./", title = "Seleccionar Imagen", filetypes = [("images", "*.jpg *.png")])
    img = Image.open(filename)
    resize_img = img.resize((416,416))
    my_image = ImageTk.PhotoImage(resize_img)
    #label = tkinter.Label(frame, image = my_image)
    label.configure(image = my_image)
    label.image = my_image
    label.pack()

def detect():
    global img
    label1.pack_forget()
    img = Image.open("detectimage.jpg")
    resize_img = img.resize((416,416))
    my_image = ImageTk.PhotoImage(resize_img)
    #label = tkinter.Label(frame, image = my_image)
    label1.configure(image = my_image)
    label1.image = my_image
    label1.pack()

#canvas = tkinter.Canvas(root, height=480, width=720, bg="#ecf0f1")
#canvas.pack()
#
#frame = tkinter.Frame(root, bg="#9b59b6")
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFileButton = tkinter.Button(root, text="Abrir Archivo", font=("arial", 16), padx=10, pady=10, fg="white", bg="#3498db", command=loadImage)
openFileButton.grid(row=1, column=0)

detectButton = tkinter.Button(root, text="Detectar", font=("arial", 16), padx=10, pady=10, fg="white", bg="#3498db", command=detect)
detectButton.grid(row=1, column=1)

root.mainloop()
