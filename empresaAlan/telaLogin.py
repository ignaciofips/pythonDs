
# import tkinter as tk
# from tkinter import messagebox
#
#
# def verificar_login():
#     emailUsuario = "admin"
#     senhaUsuario = "123"
#
#     if entry_email.get() == emailUsuario and entry_password.get() == senhaUsuario:
#         messagebox.showinfo("Aceito", "Login validado")
#     else:
#         messagebox.showerror("Inválido", "Senha ou usuário incorretos!")
#
# win = tk.Tk()
# win.geometry("300x200")
# win.title("Tela de Login")
#
# label_email = tk.Label(win, text="E-mail:")
# label_email.pack()
# entry_email = tk.Entry(win, width=35)
# entry_email.pack()
#
# label_password = tk.Label(win, text="Senha:")
# label_password.pack()
# entry_password = tk.Entry(win, width=35, show="*")
# entry_password.pack()
#
# btn_login = tk.Button(win, text="Verificar e Avançar", command=verificar_login)
# btn_login.pack(pady=10)
#
# win.mainloop()

# telaLogin.py
import tkinter as tk
from tkinter import messagebox

class TelaLogin:
    def __init__(self, master=None):
        self.root = tk.Toplevel(master)
        self.root.title("Tela de Login")
        self.root.geometry("300x200")

        self.label_usuario = tk.Label(self.root, text="Usuário:")
        self.label_senha = tk.Label(self.root, text="Senha:")
        self.entry_usuario = tk.Entry(self.root)
        self.entry_senha = tk.Entry(self.root, show="*")

        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.label_senha.pack()
        self.entry_senha.pack()

        self.botao_login = tk.Button(self.root, text="Login", command=self.verificar_login)
        self.botao_login.pack()

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos!")

    def iniciar(self):
        self.root.mainloop()
