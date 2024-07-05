import customtkinter as ctk

def fazer_login(email_entry, senha_entry):
    email = email_entry.get()
    senha = senha_entry.get()
    if email == "admin" and senha == "1234":
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

def criar_tela_login():
    janela = ctk.CTk()
    janela.geometry("500x300")

    texto = ctk.CTkLabel(janela, text="Fazer login")
    texto.pack(padx=10, pady=10)

    email_entry = ctk.CTkEntry(janela, placeholder_text="Seu email")
    email_entry.pack(padx=10, pady=10)

    senha_entry = ctk.CTkEntry(janela, placeholder_text="Sua senha", show="*")
    senha_entry.pack(padx=10, pady=10)

    botao = ctk.CTkButton(janela, text="Login", command=lambda: fazer_login(email_entry, senha_entry))
    botao.pack(padx=10, pady=10)

    janela.mainloop()
