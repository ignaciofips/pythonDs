import os
import tkinter as tk
from tkinter import messagebox
from loginTela import clique

def abrir_tela_login():
    tela_login = clique()
    tela_login.iniciar()

def botao_cliente():
    abrir_tela_login()

def formCalculadora():
    sub_form = tk.Toplevel(root)
    sub_form.title("Calculadora")
    sub_form.geometry("500x400")
    label = tk.Label(sub_form, text="Digitar dois números e calcular: adição subtração multiplicação e divisão")
    label.pack()

def formMedia():
    sub_form = tk.Toplevel(root)
    sub_form.title("Média das Notas")
    sub_form.geometry("500x400")
    label = tk.Label(sub_form, text="Formulário Média de Valores")

    txN1 = tk.Entry(sub_form)
    txN2 = tk.Entry(sub_form)
    txN3 = tk.Entry(sub_form)
    txN4 = tk.Entry(sub_form)

    label.pack()

    txN1.pack()
    txN2.pack()
    txN3.pack()
    txN4.pack()

    def media():
        n1 = float(txN1.get())
        n2 = float(txN2.get())
        n3 = float(txN3.get())
        n4 = float(txN4.get())

        m = (n1+n2+n3+n4)/4

        messagebox.showinfo("Média:", m)

    btMedia = tk.Button(sub_form, height=1, width=12, text="Calcular Média", command=media)
    btMedia.pack()

def formSobre():
    about_window = tk.Toplevel(root)
    about_window.title("Sobre")
    about_window.geometry("500x400")
    label = tk.Label(about_window, text="Este é um exemplo de aplicação com menu.")
    label2 = tk.Label(about_window, text="Este é um exemplo de aplicação com menu.")

    label.pack()
    label2.pack()

def formTriangulo():
    about_window = tk.Toplevel(root)
    about_window.title("Triângulo")
    about_window.geometry("500x400")

def abrir_devs():
    os.system('python teladevs.py')

root = tk.Tk()
root.title("Componente - Desenvolvimento de Sistemas")
root.geometry("700x500")

#-------------------------------------------------------

# componente com os submenus
barraMenu = tk.Menu(root)

#-------------------------------------------------------
# item da barra de sub menus sair

opcao_menu_arquivo = tk.Menu(barraMenu, tearoff=0)
opcao_menu_arquivo.add_command(label="Cliente", command=abrir_tela_login)
opcao_menu_arquivo.add_command(label="Administrador", command=abrir_tela_login)
opcao_menu_arquivo.add_command(label="Empresas", command=abrir_tela_login)

barraMenu.add_cascade(label="login", menu=opcao_menu_arquivo)

#-----------------------------------------------------

opcao_menu_exe = tk.Menu(barraMenu, tearoff=0)
opcao_menu_exe.add_command(label="Calculadora", command=formCalculadora)
opcao_menu_exe.add_command(label="Média", command=formMedia)
opcao_menu_exe.add_command(label="Triângulo", command=formTriangulo)

barraMenu.add_cascade(label="Exercícios", menu=opcao_menu_exe)

#-------------------------------------------------------

# item da barra de sub menus
opcao_menu_arquivo = tk.Menu(barraMenu, tearoff=0)
opcao_menu_arquivo.add_command(label="Sair", command=root.quit)

barraMenu.add_cascade(label="Arquivo", menu=opcao_menu_arquivo)

#-------------------------------------------------------

opcao_menu_ajuda = tk.Menu(barraMenu, tearoff=0)
opcao_menu_ajuda.add_command(label="Sobre", command=formSobre)
opcao_menu_ajuda.add_command(label="Devs", command=abrir_devs)

barraMenu.add_cascade(label="Ajuda", menu=opcao_menu_ajuda)

#-------------------------------------------------------

root.config(menu=barraMenu)
root.mainloop()
