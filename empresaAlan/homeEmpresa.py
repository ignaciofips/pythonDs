import customtkinter as ctk
from tkinter import Menu, messagebox
import os
from PIL import Image, ImageTk

def fazer_login(email_entry, senha_entry, root):
    email = email_entry.get()
    senha = senha_entry.get()
    if email == "admin" and senha == "1234":
        print("Login bem-sucedido!")
        root.destroy()  # Fechar a janela de login
        abrir_tela_cadastro_cliente()
    else:
        print("Usuário ou senha incorretos!")
        messagebox.showerror("Erro de Login", "Usuário ou senha incorretos!")

def criar_tela_login():
    root = ctk.CTk()
    root.geometry("500x300")

    texto = ctk.CTkLabel(root, text="Fazer login")
    texto.pack(padx=10, pady=10)

    email_entry = ctk.CTkEntry(root, placeholder_text="Seu email")
    email_entry.pack(padx=10, pady=10)

    senha_entry = ctk.CTkEntry(root, placeholder_text="Sua senha", show="*")
    senha_entry.pack(padx=10, pady=10)

    botao = ctk.CTkButton(root, text="Login", command=lambda: fazer_login(email_entry, senha_entry, root))
    botao.pack(padx=10, pady=10)

    root.mainloop()

def abrir_devs():
    os.system('python teladevs.py')

def abrir_tela_administrador():
    criar_tela_login()

def abrir_tela_cadastro_cliente():
    os.system('python cadastroCliente.py')

def formCalculadora():
    sub_form = ctk.CTkToplevel(root)
    sub_form.title("Calculadora")
    sub_form.geometry("500x400")
    label = ctk.CTkLabel(sub_form, text="Digite dois números e calcule: adição, subtração, multiplicação e divisão")
    label.pack(pady=10)

def formMedia():
    sub_form = ctk.CTkToplevel(root)
    sub_form.title("Média das Notas")
    sub_form.geometry("500x400")
    label = ctk.CTkLabel(sub_form, text="Formulário Média de Valores")
    label.pack(pady=10)

    txN1 = ctk.CTkEntry(sub_form)
    txN2 = ctk.CTkEntry(sub_form)
    txN3 = ctk.CTkEntry(sub_form)
    txN4 = ctk.CTkEntry(sub_form)

    txN1.pack(pady=5)
    txN2.pack(pady=5)
    txN3.pack(pady=5)
    txN4.pack(pady=5)

    def media():
        n1 = float(txN1.get())
        n2 = float(txN2.get())
        n3 = float(txN3.get())
        n4 = float(txN4.get())

        m = (n1+n2+n3+n4)/4

        messagebox.showinfo("Média", f"A média é: {m}")

    btMedia = ctk.CTkButton(sub_form, text="Calcular Média", command=media)
    btMedia.pack(pady=20)

def formSobre():
    about_window = ctk.CTkToplevel(root)
    about_window.title("Sobre")
    about_window.geometry("500x600")

    # Adicionar texto
    texto = ctk.CTkLabel(about_window, text="Este é um exemplo de aplicação com menu.\nMais informações sobre o projeto.")
    texto.pack(pady=10)

    # Adicionar imagens
    image_paths = ["image1.png", "image2.png", "image3.png"]  # Substitua pelos caminhos reais das suas imagens
    for img_path in image_paths:
        img = Image.open(img_path)
        img = img.resize((450, 150), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        label_img = ctk.CTkLabel(about_window, image=img_tk)
        label_img.image = img_tk  # Manter uma referência da imagem para evitar que seja destruída pelo garbage collector
        label_img.pack(pady=10)

def formTriangulo():
    about_window = ctk.CTkToplevel(root)
    about_window.title("Triângulo")
    about_window.geometry("500x400")
    label = ctk.CTkLabel(about_window, text="Formulário Triângulo")
    label.pack(pady=10)

# Configuração da janela principal e menus
root = ctk.CTk()
root.title("Componente - Desenvolvimento de Sistemas")
root.geometry("700x500")

# Componente com os submenus
barraMenu = Menu(root)

# Menu Login
opcao_menu_arquivo = Menu(barraMenu, tearoff=0)
opcao_menu_arquivo.add_command(label="Cliente", command=abrir_tela_administrador)
opcao_menu_arquivo.add_command(label="Administrador", command=abrir_tela_administrador)
opcao_menu_arquivo.add_command(label="Empresas", command=abrir_tela_administrador)
barraMenu.add_cascade(label="Login", menu=opcao_menu_arquivo)

# Menu Exercícios
opcao_menu_exe = Menu(barraMenu, tearoff=0)
opcao_menu_exe.add_command(label="Calculadora", command=formCalculadora)
opcao_menu_exe.add_command(label="Média", command=formMedia)
opcao_menu_exe.add_command(label="Triângulo", command=formTriangulo)
barraMenu.add_cascade(label="Exercícios", menu=opcao_menu_exe)

# Menu Arquivo
opcao_menu_arquivo_sair = Menu(barraMenu, tearoff=0)
opcao_menu_arquivo_sair.add_command(label="Sair", command=root.quit)
barraMenu.add_cascade(label="Arquivo", menu=opcao_menu_arquivo_sair)

# Menu Ajuda
opcao_menu_ajuda = Menu(barraMenu, tearoff=0)
opcao_menu_ajuda.add_command(label="Sobre", command=formSobre)
opcao_menu_ajuda.add_command(label="Devs", command=abrir_devs)
barraMenu.add_cascade(label="Ajuda", menu=opcao_menu_ajuda)

# Configuração da barra de menu
root.config(menu=barraMenu)

root.mainloop()
