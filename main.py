import random

# Definição das opções para cada categoria
tipos_de_estrela = ["Anã Vermelha", "Gigante Azul", "Estrela de Sequência Principal", "Estrela Binária"]
problemas_possiveis = ["Guerras entre Civilizações", "Desastres Naturais", "Epidemias e Doenças",
                       "Conflitos Políticos e Sociais", "Invasões Alienígenas", "Colapso Ecológico", "Pirataria Alienígena"]
avanco_de_civilizacao = ["Primitiva", "Industrial", "Interplanetária", "Intergaláctica"]
tipo_de_civilizacao = ["Agressiva", "Passivo-agressiva", "Pacífica"]
tipos_de_planetas = ["Terrestre", "Desértico", "Gasoso", "Oceânico", "Congelado", "Artificial", "Anômalo"]
caracteristicas_fisicas_astronomicas = {
    "distancia_entre_planetas": random.uniform(0.1, 50),  # em unidades astronômicas
    "excentricidade_orbitas_planetas": random.uniform(0, 1),
    "inclinação_axial_planetas": random.uniform(0, 90),  # em graus
    "rotação_sincronizada": random.choice([True, False]),
    "periodo_eclipses": random.uniform(0, 365),  # em dias
    "presenca_estacoes_ano": random.choice(["Sim", "Não"])
}

def gerar_sistema_planetario():
    sistema_planetario = {
        "estrela_central": {
            "tipo": random.choice(tipos_de_estrela),
            "massa": random.uniform(0.1, 10),  # em massas solares
            "tamanho": random.uniform(0.1, 100),  # em raios solares
            "temperatura_superficial": random.uniform(2000, 40000),  # em Kelvin
            "luminosidade": random.uniform(0.1, 100),  # em relação ao Sol
            "estagio_vida": random.choice(["Main Sequence", "Red Giant", "White Dwarf"]),
            "idade": random.uniform(0, 15),  # em bilhões de anos
        },
        "planetas": [],
        "asteroides_cometas": [],
        "caracteristicas_fisicas_astronomicas": caracteristicas_fisicas_astronomicas,
        "elementos_exoticos": []
    }

    quantidade_planetas = random.randint(1, 10)
    for i in range(quantidade_planetas):
        planeta = {
            "nome": f"Planeta {i+1}",
            "diametro": random.uniform(2000, 200000),  # em quilômetros
            "massa": random.uniform(0.01, 100),  # em massas terrestres
            "composicao_atmosferica": random.choice(["Nitrogênio", "Oxigênio", "Dióxido de Carbono", "Outros"]),
            "composicao_geologica": random.choice(["Rocha", "Gelo", "Metal"]),
            "distancia_orbital": random.uniform(0.1, 50),  # em unidades astronômicas
            "periodo_rotacao": random.uniform(1, 100),  # em horas
            "periodo_translacao": random.uniform(50, 500),  # em dias
            "inclinação_orbital": random.uniform(0, 90),  # em graus
            "numero_luas": random.randint(0, 10),
            "presenca_aneis": random.choice([True, False]),
            "satelites_naturais": []  # Adicionando lista vazia para satélites
        }
        # Geração dos satélites naturais para cada planeta
        for j in range(planeta["numero_luas"]):
            satelite = {
                "nome": f"Lua {j+1} de {planeta['nome']}",
                "diametro": random.uniform(10, 5000),  # em quilômetros
                "massa": random.uniform(0.0001, 0.1),  # em massas terrestres
                "distancia_orbital": random.uniform(1000, 100000),  # em quilômetros
                "caracteristicas_geologicas": random.choice(["Montanhas", "Vales", "Crateras"]),
                "composicao_atmosferica": random.choice(["Nenhuma", "Gás Volátil", "Traços de Nitrogênio"]),
            }
            planeta["satelites_naturais"].append(satelite)  # Adicionando o satélite ao planeta

        sistema_planetario["planetas"].append(planeta)

    # Geração de asteroides e cometas, elementos exóticos, etc., permanece igual

    return sistema_planetario

# Ajuste na função de impressão para incluir satélites naturais de cada planeta
def imprimir_sistema_planetario(sistema):
    print("Sistema Planetário:")
    print("-------------------\n")
    
    # Estrela Central
    print("Estrela Central:")
    for chave, valor in sistema["estrela_central"].items():
        print(f"  {chave}: {valor}")
    print("\n-------------------\n")
    
    # Planetas
    for i, planeta in enumerate(sistema["planetas"], start=1):
        print(f"Planeta {i}:")
        for chave, valor in planeta.items():
            if chave != "satelites_naturais":  # Não imprime satélites aqui
                print(f"  {chave}: {valor}")
        
        # Satélites Naturais
        if planeta["satelites_naturais"]:
            print("  Satélites Naturais:")
            for lua in planeta["satelites_naturais"]:
                print(f"    - {lua['nome']}:")
                print(f"      Diametro: {lua['diametro']} km")
                print(f"      Massa: {lua['massa']} massas terrestres")
                print(f"      Distância Orbital: {lua['distancia_orbital']} km")
                print("      ---")
        print("\n-------------------\n")

# Gerar e imprimir um sistema planetário
sistema_planetario = gerar_sistema_planetario()
imprimir_sistema_planetario(sistema_planetario)

    # Impressão de asteroides, cometas, características físicas astronômicas, e elementos exóticos segue

# Gerar e imprimir um sistema planetário
sistema_planetario = gerar_sistema_planetario()
imprimir_sistema_planetario(sistema_planetario)
