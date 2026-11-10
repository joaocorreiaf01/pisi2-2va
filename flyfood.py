def ler_arquivo(arquivo_matriz):
    origem = None
    total_pontos_entrega = {}

    with open(arquivo_matriz, "r") as arquivo:
        primeira_linha = arquivo.readline().split()
        quantidade_linhas = int(primeira_linha[0])
        quantidade_colunas = int(primeira_linha[1])

        for i, linha in enumerate(arquivo):
            casas = linha.split()

            for j, casa in enumerate(casas):
                if casa == "R":
                    origem = (i, j)
                elif casa != "0":
                    total_pontos_entrega[casa] = (i, j)

    return quantidade_linhas, quantidade_colunas, origem, total_pontos_entrega

def calcular_distancia(posicao_partida, posicao_chegada):
    distancia = abs(posicao_partida[0] - posicao_chegada[0]) + abs(posicao_partida[1] - posicao_chegada[1])

    return distancia

def calcular_custo_rota(origem, total_pontos_entrega, rota):
    custo_total = 0
    posicao_atual = origem

    for ponto_entrega in rota:
        proxima_posicao = total_pontos_entrega[ponto_entrega]
        custo_total += calcular_distancia(posicao_atual, proxima_posicao)
        posicao_atual = proxima_posicao

    custo_total += calcular_distancia(posicao_atual, origem)

    return custo_total


