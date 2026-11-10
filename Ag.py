import random
import time
from flyfood import calcular_custo_rota
from dados_entrega_flyfood import total_pontos_entrega, origem
from deap import algorithms, base, benchmarks, cma, creator, gp, tools

#consta em inglês na documentação, mantive igual
#segue trecho: https://deap.readthedocs.io/en/master/tutorials/basic/part1.html
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

tamanho_populacao = 600
probabilidade_mutacao_por_posicao = 0.4
tamanho_torneio = 3
probabilidade_cruzamento = 0.9
probabilidade_mutacao = 0.4
quantidade_geracoes = 3000
lista_pontos = list(total_pontos_entrega)
quantidade_pontos = len(lista_pontos)

def avaliar_rota(individuo):
    rota = []
    for indice in individuo:
        rota.append(lista_pontos[indice])

    custo_rota = calcular_custo_rota(origem, total_pontos_entrega, rota)
    return (custo_rota,)

#toolbox evaluate, mate, mutate e select precisam estar em inglês devido ao eaSimple,
#segue trecho: https://deap.readthedocs.io/en/master/tutorials/basic/part2.html#using-the-toolbox em "Algoritmos"
toolbox = base.Toolbox()
toolbox.register("gerar_rota_aleatoria", random.sample, range(quantidade_pontos), quantidade_pontos)
toolbox.register("criar_individuo", tools.initIterate, creator.Individual, toolbox.gerar_rota_aleatoria)
toolbox.register("criar_populacao", tools.initRepeat, list, toolbox.criar_individuo)
toolbox.register("evaluate", avaliar_rota)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=probabilidade_mutacao_por_posicao)
toolbox.register("select", tools.selTournament, tournsize=tamanho_torneio)

populacao = toolbox.criar_populacao(tamanho_populacao)

#a aplicação do halloffame foi utilizando o repositório do deap no github como referência
#exemplo de uso: https://github.com/DEAP/deap/blob/master/examples/ga/tsp.py
melhores_rotas = tools.HallOfFame(1)

tempo_inicial = time.time()
algorithms.eaSimple(populacao, toolbox, probabilidade_cruzamento, probabilidade_mutacao, quantidade_geracoes, halloffame=melhores_rotas, verbose=False)
tempo_total = time.time() - tempo_inicial

melhor_individuo = melhores_rotas[0]

melhor_rota = []
for indice in melhor_individuo:
    melhor_rota.append(lista_pontos[indice])

custo_melhor_rota = calcular_custo_rota(origem, total_pontos_entrega, melhor_rota)

print(f"melhor rota: {melhor_rota}")
print(f"custo: {custo_melhor_rota}")
print(f"tempo: {tempo_total:.2f} segundos")