def calcular_tpps(peso_atual, porcentagem_min, porcentagem_max):
    """Calcula a Taxa de Perda de Peso Sugerida (TPPS) com base no peso atual."""
    return peso_atual * porcentagem_min, peso_atual * porcentagem_max


def calcular_peso_meta_e_nepp_cao(peso_atual, ecc):
    """Calcula o peso meta e o NEPP para cães com base no ECC."""
    if ecc == 8 or ecc == 9:
        peso_meta = peso_atual * 0.80
        nepp = 70 * (peso_meta ** 0.75)
    elif ecc == 6 or ecc == 7:
        peso_meta = peso_atual * 0.85
        nepp = 70 * (peso_meta ** 0.75)
    else:
        return None, None  # ECC inválido
    return peso_meta, nepp


def calcular_peso_meta_e_nepp_gato(peso_atual, ecc):
    """Calcula o peso meta e o NEPP para gatos com base no ECC."""
    if ecc == 8 or ecc == 9:
        peso_meta = peso_atual * 0.85
        nepp = 85 * (peso_atual ** 0.4)
    elif ecc == 6 or ecc == 7:
        peso_meta = peso_atual * 0.90
        nepp = 85 * (peso_atual ** 0.4)
    else:
        return None, None  # ECC inválido
    return peso_meta, nepp


def calcular_quantidade_racao(nepp, valor_energetico_racao, refeicoes_por_dia):
    """Calcula a quantidade de ração por refeição."""
    # Converte valor energético de 100g para valor por grama
    valor_energetico_racao_por_grama = valor_energetico_racao / 100.0
    # Calcula quantidade total de ração diária e por refeição
    racao_diaria = nepp / valor_energetico_racao_por_grama
    racao_por_refeicao = racao_diaria / refeicoes_por_dia
    return racao_por_refeicao


def protocolo_perda_peso_com_racao():
    # Entrada de dados do usuário
    try:
        animal = int(input('Escolha o animal (1) Cão; (2) Gato: '))
        if animal not in [1, 2]:
            raise ValueError("Opção inválida. Escolha 1 para Cão ou 2 para Gato.")

        if animal == 1:
            print('Calculando para: Cão')
            peso_atual = float(input('Digite o Peso Atual do animal (Kg): '))
            ecc = int(input('Digite o ECC do animal (6-9): '))

            tpps_min, tpps_max = calcular_tpps(peso_atual, 0.01, 0.02)
            print(f'TPPS de 1 a 2%: {tpps_min:.2f} a {tpps_max:.2f} Kg')

            peso_meta, nepp = calcular_peso_meta_e_nepp_cao(peso_atual, ecc)
            if peso_meta:
                print(f'Peso Meta: {peso_meta:.2f} Kg')
                print(f'NEPP: {nepp:.2f} Kcal')
            else:
                print("ECC inválido. Por favor, insira um valor entre 6 e 9.")

        elif animal == 2:
            print('Calculando para: Gato')
            peso_atual = float(input('Digite o Peso Atual do animal (Kg): '))
            ecc = int(input('Digite o ECC do animal (6-9): '))

            tpps_min, tpps_max = calcular_tpps(peso_atual, 0.005, 0.01)
            print(f'TPPS de 0,5 a 1%: {tpps_min:.2f} a {tpps_max:.2f} Kg')

            peso_meta, nepp = calcular_peso_meta_e_nepp_gato(peso_atual, ecc)
            if peso_meta:
                print(f'Peso Meta: {peso_meta:.2f} Kg')
                print(f'NEPP: {nepp:.2f} Kcal')
            else:
                print("ECC inválido. Por favor, insira um valor entre 6 e 9.")

        # Pergunta sobre ração e refeições
        refeicoes_por_dia = int(input("Quantas refeições o animal faz por dia? "))
        valor_energetico_racao = float(input("Qual o valor energético da ração (kcal por 100g)? "))

        # Calcular a quantidade de ração por refeição
        racao_por_refeicao = calcular_quantidade_racao(nepp, valor_energetico_racao, refeicoes_por_dia)
        print(f"Quantidade de ração por refeição: {racao_por_refeicao:.2f} gramas")

    except ValueError as e:
        print(f"Erro de entrada: {e}")

protocolo_perda_peso_com_racao()
