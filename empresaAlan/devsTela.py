import os
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser

# Funções para abrir os links
def abrir_linkedin():
    webbrowser.open('https://www.linkedin.com')

def abrir_github():
    webbrowser.open('https://www.github.com')

def abrir_instagram():
    webbrowser.open('https://www.instagram.com')

# Função para a tela da Calculadora
def formCalculadora():
    sub_form = tk.Toplevel(root)
    sub_form.title("Calculadora")
    sub_form.geometry("500x400")
    label = tk.Label(sub_form, text="Digitar dois números e calcular: adição subtração multiplicação e divisão")
    label.pack()

# Função para a tela da Média das Notas
def formMedia():
    sub_form = tk.Toplevel(root)
    sub_form.title("Média das Notas")
    sub_form.geometry("500x400")
    label = tk.Label(sub_form, text="Formulário Média de Valores")
    # ... (resto do código da função formMedia)

# Função para a tela Sobre
def formSobre():
    about_window = tk.Toplevel(root)
    about_window.title("Sobre")
    about_window.geometry("500x400")
    label = tk.Label(about_window, text="Este é um exemplo de aplicação com menu.")
    label2 = tk.Label(about_window, text="Este é um exemplo de aplicação com menu.")
    # ... (resto do código da função formSobre)

# Função para a tela Triângulo
def formTriangulo():
    about_window = tk.Toplevel(root)
    about_window.title("Triângulo")
    about_window.geometry("500x400")
    # ... (resto do código da função formTriangulo)

# Função para a tela dos Desenvolvedores
def formDevs():
    win = tk.Toplevel(root)
    win.title("Desenvolvedores")
    win.geometry("500x550")
    win.configure(background="black")

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


root = tk.Tk()
root.title("Componente - Desenvolvimento de Sistemas")
root.geometry("700x500")


barraMenu = tk.Menu(root)


opcao_menu_arquivo = tk.Menu(barraMenu, tearoff=0)
opcao_menu_arquivo.add_command(label="Sair", command=root.quit)
barraMenu.add_cascade(label="Arquivo", menu=opcao_menu_arquivo)


opcao_menu_exe = tk.Menu(barraMenu, tearoff=0)
opcao_menu_exe.add_command(label="Calculadora", command=formCalculadora)
opcao_menu_exe.add_command(label="Média", command=formMedia)
opcao_menu_exe.add_command(label="Triângulo", command=formTriangulo)
barraMenu.add_cascade(label="Exercícios", menu=opcao_menu_exe)


opcao_menu_ajuda = tk.Menu(barraMenu, tearoff=0)
opcao_menu_ajuda.add_command(label="Sobre", command=formSobre)
opcao_menu_ajuda.add_command(label="Devs", command=formDevs)
barraMenu.add_cascade(label="Ajuda", menu=opcao_menu_ajuda)

