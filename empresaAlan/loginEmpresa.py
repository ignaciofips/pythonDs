# telaLogin.py
import customtkinter as ctk
from tkinter import messagebox

class TelaLogin:
    def __init__(self, master=None):
        self.root = ctk.CTkToplevel(master)
        self.root.title("Tela de Login")
        self.root.geometry("300x200")

        self.label_usuario = ctk.CTkLabel(self.root, text="Usuário:")
        self.label_senha = ctk.CTkLabel(self.root, text="Senha:")
        self.entry_usuario = ctk.CTkEntry(self.root)
        self.entry_senha = ctk.CTkEntry(self.root, show="*")

        self.label_usuario.pack(pady=10)
        self.entry_usuario.pack(pady=5)
        self.label_senha.pack(pady=10)
        self.entry_senha.pack(pady=5)

        self.botao_login = ctk.CTkButton(self.root, text="Login", command=self.verificar_login)
        self.botao_login.pack(pady=20)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos!")

    def iniciar(self):
        self.root.mainloop()
