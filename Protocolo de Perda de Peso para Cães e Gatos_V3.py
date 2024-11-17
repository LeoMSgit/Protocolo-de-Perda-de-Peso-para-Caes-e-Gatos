import tkinter as tk
from tkinter import ttk, messagebox


def calcular_tpps(peso_atual, porcentagem_min, porcentagem_max):
    return peso_atual * porcentagem_min, peso_atual * porcentagem_max


def calcular_peso_meta_e_nepp_cao(peso_atual, ecc):
    if ecc in [8, 9]:
        peso_meta = peso_atual * 0.80
        nepp = 70 * (peso_meta ** 0.75)
    elif ecc in [6, 7]:
        peso_meta = peso_atual * 0.85
        nepp = 70 * (peso_meta ** 0.75)
    else:
        return None, None
    return peso_meta, nepp


def calcular_peso_meta_e_nepp_gato(peso_atual, ecc):
    if ecc in [8, 9]:
        peso_meta = peso_atual * 0.85
        nepp = 85 * (peso_atual ** 0.4)
    elif ecc in [6, 7]:
        peso_meta = peso_atual * 0.90
        nepp = 85 * (peso_atual ** 0.4)
    else:
        return None, None
    return peso_meta, nepp


def calcular_quantidade_racao(nepp, valor_energetico_racao, refeicoes_por_dia):
    valor_energetico_racao_por_grama = valor_energetico_racao / 100.0
    racao_diaria = nepp / valor_energetico_racao_por_grama
    return racao_diaria / refeicoes_por_dia


def calcular():
    try:
        peso_atual = float(entry_peso.get())
        ecc = int(entry_ecc.get())
        refeicoes = int(entry_refeicoes.get())
        valor_energetico = float(entry_valor_energetico.get())
        animal = animal_var.get()

        if animal == "Cão":
            tpps_min, tpps_max = calcular_tpps(peso_atual, 0.01, 0.02)
            peso_meta, nepp = calcular_peso_meta_e_nepp_cao(peso_atual, ecc)
        else:
            tpps_min, tpps_max = calcular_tpps(peso_atual, 0.005, 0.01)
            peso_meta, nepp = calcular_peso_meta_e_nepp_gato(peso_atual, ecc)

        if peso_meta is None:
            messagebox.showerror("Erro", "ECC inválido. Deve ser entre 6 e 9.")
            return

        racao_por_refeicao = calcular_quantidade_racao(nepp, valor_energetico, refeicoes)

        result_text.set(
            f"TPPS: {tpps_min:.2f} - {tpps_max:.2f} Kg\n"
            f"Peso Meta: {peso_meta:.2f} Kg\n"
            f"NEPP: {nepp:.2f} Kcal\n"
            f"Ração por Refeição: {racao_por_refeicao:.2f} g"
        )
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro de entrada: {e}")


def limpar():
    entry_peso.delete(0, tk.END)
    entry_ecc.delete(0, tk.END)
    entry_refeicoes.delete(0, tk.END)
    entry_valor_energetico.delete(0, tk.END)
    result_text.set("")


# Configuração da Interface
root = tk.Tk()
root.title("Protocolo de Perda de Peso")

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 10), padding=6)

frame = ttk.Frame(root, padding="70")
frame.grid(row=0, column=0, padx=20, pady=20)

animal_var = tk.StringVar(value="Cão")

# Inputs
ttk.Label(frame, text="Animal:").grid(row=0, column=0, sticky="w")
ttk.Radiobutton(frame, text="Cão", variable=animal_var, value="Cão").grid(row=0, column=1, sticky="w")
ttk.Radiobutton(frame, text="Gato", variable=animal_var, value="Gato").grid(row=0, column=2, sticky="w")

ttk.Label(frame, text="Peso Atual (Kg):").grid(row=1, column=0, sticky="w")
entry_peso = ttk.Entry(frame, width=20)
entry_peso.grid(row=1, column=1, columnspan=2, sticky="w")

ttk.Label(frame, text="ECC (6-9):").grid(row=2, column=0, sticky="w")
entry_ecc = ttk.Entry(frame, width=20)
entry_ecc.grid(row=2, column=1, columnspan=2, sticky="w")

ttk.Label(frame, text="Refeições por Dia:").grid(row=3, column=0, sticky="w")
entry_refeicoes = ttk.Entry(frame, width=20)
entry_refeicoes.grid(row=3, column=1, columnspan=2, sticky="w")

ttk.Label(frame, text="Valor Energético (kcal/100g):").grid(row=4, column=0, sticky="w")
entry_valor_energetico = ttk.Entry(frame, width=20)
entry_valor_energetico.grid(row=4, column=1, columnspan=2, sticky="w")

# Botões
ttk.Button(frame, text="Calcular", command=calcular).grid(row=6, column=0, pady=10)
ttk.Button(frame, text="Limpar", command=limpar).grid(row=6, column=1, pady=10)

# Resultados
result_text = tk.StringVar()
ttk.Label(frame, text="Resultados:", font=('Arial', 12, 'bold')).grid(row=8, column=0, columnspan=3, pady=5)
ttk.Label(frame, textvariable=result_text, relief="sunken", width=40, background="#f0f0f0").grid(row=9, column=0,
                                                                                                 columnspan=3, pady=5)

root.mainloop()
