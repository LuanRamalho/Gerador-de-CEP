import tkinter as tk
import random

def generate_cep():
    cep = f"{random.randint(0, 99999):05d}-{random.randint(0, 999):03d}"
    cep_label.config(text=cep)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de CEP")
root.geometry("300x150")
root.configure(bg='#f0f8ff')  # cor de fundo colorida

# Label para mostrar o CEP gerado
cep_label = tk.Label(root, text="Clique no botão para gerar o CEP", font=("Helvetica", 16), bg='#f0f8ff')
cep_label.pack(pady=20)

# Botão para gerar o CEP
generate_button = tk.Button(root, text="Gerar CEP", command=generate_cep, bg='#87CEFA', font=("Helvetica", 12))
generate_button.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
