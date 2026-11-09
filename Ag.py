import random
from deap import algorithms, base, benchmarks, cma, creator, gp, tools
from flyfood import ler_arquivo, calcular_custo_rota

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

quantidade_linhas, quantidade_colunas, origem, total_pontos_entrega = ler_arquivo("matriz.txt")

lista_pontos = list(total_pontos_entrega)
quantidade_pontos = len(lista_pontos)


def avaliar_rota(individuo):
    rota = []
    for indice in individuo:
        rota.append(lista_pontos[indice])

    custo_rota = calcular_custo_rota(origem, total_pontos_entrega, rota)

    return (custo_rota,)

tamanho_populacao = 5
probabilidade_mutacao_por_posicao = 0.05
tamanho_torneio = 3

toolbox = base.Toolbox()
toolbox.register("gerar_rota_aleatoria", random.sample, range(quantidade_pontos), quantidade_pontos)
toolbox.register("criar_individuo", tools.initIterate, creator.Individual, toolbox.gerar_rota_aleatoria)
toolbox.register("criar_populacao", tools.initRepeat, list, toolbox.criar_individuo)
toolbox.register("evaluate", avaliar_rota)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=probabilidade_mutacao_por_posicao)
toolbox.register("select", tools.selTournament, tournsize=tamanho_torneio)

populacao = toolbox.criar_populacao(tamanho_populacao)

print(f"pontos: {lista_pontos}")
print(f"populacao inicial: {populacao}")
print(avaliar_rota([1, 0, 2, 4, 5, 3]))