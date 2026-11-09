def ler_arquivo(arquivo_matriz):
    origem = None
    pontos_entrega = {}

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
                    pontos_entrega[casa] = (i, j)

    return quantidade_linhas, quantidade_colunas, origem, pontos_entrega


quantidade_linhas, quantidade_colunas, origem, pontos_entrega = ler_arquivo("matriz.txt")

print(f"tamanho da matriz: {quantidade_linhas}x{quantidade_colunas}")
print(f"origem: {origem}")
print(f"pontos: {pontos_entrega}")