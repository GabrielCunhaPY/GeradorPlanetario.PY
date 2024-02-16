import tkinter as tk
from tkinter import scrolledtext, ttk
import random

tipos_de_estrela = ["Anã Vermelha", "Gigante Azul", "Estrela de Sequência Principal", "Estrela Binária"]
problemas_possiveis = ["Guerras entre Civilizações", "Desastres Naturais", "Epidemias e Doenças",
                       "Conflitos Políticos e Sociais", "Invasões Alienígenas", "Colapso Ecológico", "Pirataria Alienígena", "racismo"]
avanco_de_civilizacao = ["Primitiva", "Industrial", "Interplanetária", "Intergaláctica"]
tipo_de_civilizacao = ["Agressiva", "Passivo-agressiva", "Pacífica"]
tipos_de_planetas = ["Terrestre", "Desértico", "Gasoso", "Oceânico", "Congelado", "Artificial", "Anômalo"]

def gerar_sistema_planetario():
    sistema_planetario = {
        "estrela_central": {
            "tipo": random.choice(tipos_de_estrela),
            "massa": random.uniform(0.1, 10),  # em massas solares
            "tamanho": random.uniform(0.1, 100),  # em raios solares
            "temperatura_superficial": random.uniform(2000, 40000),  # em Kelvin
            "luminosidade": random.uniform(0.1, 100),  # em vezes a luminosidade do Sol
            "estagio_vida": random.choice(["Main Sequence", "Red Giant", "White Dwarf"]),
            "idade": random.uniform(0, 15),  # em bilhões de anos
        },
        "planetas": [],
        "elementos_exoticos": []
    }

    quantidade_planetas = random.randint(1, 10)
    for i in range(quantidade_planetas):
        habitavel = random.choice([True, False])
        planeta = {
            "nome": f"Planeta {i+1}",
            "tipo": random.choice(tipos_de_planetas),
            "diametro": random.uniform(2000, 200000),  # em quilômetros
            "massa": random.uniform(0.01, 100),  # em massas terrestres
            "composicao_atmosferica": random.choice(["Nitrogênio", "Oxigênio", "Dióxido de Carbono", "Amônia"]),
            "composicao_geologica": random.choice(["Rocha", "Gelo", "Metal"]),
            "periodo_rotacao": random.uniform(1, 100),  # em horas
            "periodo_translacao": random.uniform(50, 500),  # em dias
            "numero_luas": random.randint(0, 10),
            "presenca_aneis": random.choice([True, False]),
            "habitavel": habitavel,
            "satelites_naturais": []
        }

        for j in range(planeta["numero_luas"]):
            satelite = {
                "nome": f"Lua {j+1} de Planeta {i+1}",
                "diametro": random.uniform(10, 5000),  # em quilômetros
                "massa": random.uniform(0.0001, 0.1),  # em massas terrestres
            }
            planeta["satelites_naturais"].append(satelite)

        if habitavel:
            planeta["civilizacao"] = {
                "problemas_possiveis": random.choice(problemas_possiveis),
                "avanco_de_civilizacao": random.choice(avanco_de_civilizacao),
                "tipo_de_civilizacao": random.choice(tipo_de_civilizacao),
            }

        sistema_planetario["planetas"].append(planeta)

    return sistema_planetario


def imprimir_sistema_planetario(sistema):
    texto = "Sistema Planetário:\n-------------------\n\n"
    
    # Estrela Central
    texto += "Estrela Central:\n"
    for chave, valor in sistema["estrela_central"].items():
        valor_formatado = f"{valor:.2f}" if isinstance(valor, float) else valor
        if chave == "massa":
            valor_formatado += " massas solares"
        elif chave == "tamanho":
            valor_formatado += " raios solares"
        elif chave == "temperatura_superficial":
            valor_formatado += " K"
        elif chave == "idade":
            valor_formatado += " bilhões de anos"
        elif chave == "luminosidade":
            valor_formatado += " vezes a luminosidade do Sol"
        texto += f"  {chave.replace('_', ' ').capitalize()}: {valor_formatado}\n"
    texto += "\n-------------------\n"
    
    # Planetas e Satélites Naturais
    for i, planeta in enumerate(sistema["planetas"], start=1):
        texto += f"Planeta {i}: {planeta['nome']} ({planeta['tipo']})\n"
        for chave, valor in planeta.items():
            if chave in ["civilizacao", "nome", "tipo", "satelites_naturais"]: continue
            valor_formatado = f"{valor:.2f}" if isinstance(valor, float) else valor
            if chave == "diametro":
                valor_formatado += " km"
            elif chave == "massa":
                valor_formatado += " massas terrestres"
            elif chave == "periodo_rotacao":
                valor_formatado += " horas"
            elif chave == "periodo_translacao":
                valor_formatado += " dias"
            texto += f"  {chave.replace('_', ' ').capitalize()}: {valor_formatado}\n"
        
        # Satélites Naturais
        if planeta["satelites_naturais"]:
            texto += "\n  Satélites Naturais:\n"
            for lua in planeta["satelites_naturais"]:
                texto += f"    - {lua['nome']}:\n"
                for lua_chave, lua_valor in lua.items():
                    if lua_chave in ["diametro"]:
                        lua_valor_formatado = f"{lua_valor:.2f} km"
                    elif lua_chave in ["massa"]:
                        lua_valor_formatado = f"{lua_valor:.2f} massas terrestres"
                    elif lua_chave in ["distancia_orbital"]:
                        lua_valor_formatado = f"{lua_valor:.2f} km"
                    else:
                        lua_valor_formatado = lua_valor
                    texto += f"      {lua_chave.replace('_', ' ').capitalize()}: {lua_valor_formatado}\n"
                texto += "      ---\n"
        texto += "\n-------------------\n"
                
        if "civilizacao" in planeta:
            texto += "\n  Civilização:\n"
            for chave, valor in planeta["civilizacao"].items():
                texto += f"    {chave.replace('_', ' ').capitalize()}: {valor}\n"
        texto += "\n-------------------\n"

    return texto

def create_custom_theme():
    style = ttk.Style()
    style.theme_create('custom_dark', parent='alt', settings={
        ".": {
            "configure": {
                "background": '#333333',  # Cor de fundo
                "font": ('Arial', 12),
                "foreground": 'white'
            }
        },
        "TButton": {
            "configure": {
                "padding": 5,
                "background": '#5C5C5C',
                "foreground": 'white',
                "font": ('Arial', 12, 'bold')
            },
            "map": {
                "background": [('active', '#5C5C5F')],
                "foreground": [('active', 'white')]
            }
        },
        "TEntry": {
            "configure": {
                "padding": 5,
                "fieldbackground": '#333333',
                "foreground": 'white',
                "insertcolor": 'white'  # Cor do cursor
            }
        },
        "TLabel": {
            "configure": {
                "background": '#333333',
                "foreground": 'white',
                "font": ('Arial', 12, 'bold')
            }
        },
        "TFrame": {
            "configure": {
                "background": '#333333'
            }
        },
        "TScrolledText": {
            "configure": {
                "background": '#2B2B2B',
                "foreground": '#CCCCCC',
                "insertbackground": 'white'
            }
        }
    })
    style.theme_use('custom_dark')

def gerar_sistema_planetario_gui():
    sistema_planetario = gerar_sistema_planetario()
    texto = imprimir_sistema_planetario(sistema_planetario)

    # Atualizar o texto na área de texto
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.INSERT, texto)
    text_area.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Gerador de Sistema Planetário")
root.geometry("800x600")
root.configure(bg='#333333')

create_custom_theme()

main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10, fill='both', expand=True)

generate_button = ttk.Button(main_frame, text="Gerar Sistema Planetário", command=gerar_sistema_planetario_gui)
generate_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=80, height=25, font=("Consolas", 10))
text_area.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()
