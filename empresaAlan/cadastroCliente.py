import customtkinter as ctk
from tkinter import messagebox, ttk
import mysql.connector
import tkinter as tk

class TabelaClientes(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Lista de Clientes")
        self.geometry("800x400")

        self.columns = ("ID", "Nome", "Sobrenome", "CPF", "RG", "Email", "Rua", "Bairro", "CEP", "Data de Nascimento")
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def atualizar_tabela(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bdLoja"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tbcliente")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)

        except mysql.connector.Error as error:
            tk.messagebox.showerror("Erro", f"Erro ao buscar dados: {error}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        self.update()

def inserir_dados():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    cpf = entry_cpf.get()
    rg = entry_rg.get()
    email = entry_email.get()
    rua = entry_rua.get()
    bairro = entry_bairro.get()
    cep = entry_cep.get()
    dataNasc = entry_dataNasc.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bdLoja"
        )
        cursor = conn.cursor()
        sql = """INSERT INTO tbcliente 
                 (nomeCliente, sobrenomeCliente, cpfCliente, rgCliente, emailCliente, ruaCliente, bairroCliente, cepCliente, dataNasc) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (nome, sobrenome, cpf, rg, email, rua, bairro, cep, dataNasc)
        cursor.execute(sql, valores)
        conn.commit()

        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

        tabela_clientes = TabelaClientes(janela)
        tabela_clientes.atualizar_tabela()

    except mysql.connector.Error as error:
        messagebox.showerror("Erro", f"Erro ao inserir dados: {error}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

janela = ctk.CTk()
janela.title("Cadastro Cliente")
janela.geometry("800x600")

ctk.CTkLabel(janela, text="Nome:", anchor="w").grid(row=0, column=0, padx=(10, 0), pady=10)
entry_nome = ctk.CTkEntry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="Sobrenome:", anchor="w").grid(row=1, column=0, padx=(10, 0), pady=10)
entry_sobrenome = ctk.CTkEntry(janela)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="CPF:", anchor="w").grid(row=2, column=0, padx=(10, 0), pady=10)
entry_cpf = ctk.CTkEntry(janela)
entry_cpf.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="RG:", anchor="w").grid(row=3, column=0, padx=(10, 0), pady=10)
entry_rg = ctk.CTkEntry(janela)
entry_rg.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="Email:", anchor="w").grid(row=4, column=0, padx=(10, 0), pady=10)
entry_email = ctk.CTkEntry(janela)
entry_email.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="Rua:", anchor="w").grid(row=5, column=0, padx=(10, 0), pady=10)
entry_rua = ctk.CTkEntry(janela)
entry_rua.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="Bairro:", anchor="w").grid(row=6, column=0, padx=(10, 0), pady=10)
entry_bairro = ctk.CTkEntry(janela)
entry_bairro.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="CEP:", anchor="w").grid(row=7, column=0, padx=(10, 0), pady=10)
entry_cep = ctk.CTkEntry(janela)
entry_cep.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(janela, text="Data de Nascimento:", anchor="w").grid(row=8, column=0, padx=(10, 0), pady=10)
entry_dataNasc = ctk.CTkEntry(janela)
entry_dataNasc.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkButton(janela, text="Inserir", command=inserir_dados).grid(row=9, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
