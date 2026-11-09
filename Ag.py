import random
from deap import algorithms, base, benchmarks, cma, creator, gp, tools
from flyfood import ler_arquivo, calcular_custo_rota

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

quantidade_linhas, quantidade_colunas, origem, total_pontos_entrega = ler_arquivo("matriz.txt")

lista_pontos = list(total_pontos_entrega)
quantidade_pontos = len(lista_pontos)

toolbox = base.Toolbox()
toolbox.register("gerar_rota_aleatoria", random.sample, range(quantidade_pontos), quantidade_pontos)
toolbox.register("criar_individuo", tools.initIterate, creator.Individual, toolbox.gerar_rota_aleatoria)
toolbox.register("criar_populacao", tools.initRepeat, list, toolbox.criar_individuo)

tamanho_populacao = 5
populacao = toolbox.criar_populacao(tamanho_populacao)

print(f"pontos: {lista_pontos}")
print(f"populacao inicial: {populacao}")
