import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

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
        # Limpar dados existentes na Treeview
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
                # Inserir dados na Treeview em cascata
                self.tree.insert("", tk.END, values=row)

        except mysql.connector.Error as error:
            messagebox.showerror("Erro", f"Erro ao buscar dados: {error}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        self.update()

# Exemplo de utilização da classe TabelaClientes:
if __name__ == "__main__":
    root = tk.Tk()
    tabela_clientes = TabelaClientes(root)
    tabela_clientes.atualizar_tabela()
    root.mainloop()
