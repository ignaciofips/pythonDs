import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

def abrir_linkedin():
    webbrowser.open('https://www.linkedin.com')

def abrir_github():
    webbrowser.open('https://www.github.com')

def abrir_instagram():
    webbrowser.open('https://www.instagram.com')

win = tk.Tk()
win.geometry("500x550")
win.configure(background="black")
win.configure()


imagens = ['img/inacio.jpg', 'img/inacio.jpg', 'img/inacio.jpg', 'img/inacio.jpg']
for i, imagem in enumerate(imagens):
    img = Image.open(imagem)
    img = img.resize((100, 100)) # tamanho das imagens em px
    img = ImageTk.PhotoImage(img)
    painel = tk.Label(win, image=img)
    painel.image = img
    painel.grid(row=i, column=0, padx=10, pady=10)

    btn_linkedin = tk.Button(win, text="LinkedIn", command=abrir_linkedin, bg="blue")
    btn_linkedin.grid(row=i, column=1, padx=10)
    btn_github = tk.Button(win, text="GitHub", command=abrir_github, bg="purple")
    btn_github.grid(row=i, column=2, padx=10)
    btn_instagram = tk.Button(win, text="Instagram", command=abrir_instagram, bg="pink")
    btn_instagram.grid(row=i, column=3, padx=10)

win.mainloop()
