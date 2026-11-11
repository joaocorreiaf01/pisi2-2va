import random
import time
from flyfood import calcular_custo_rota
from dados_entrega_flyfood import total_pontos_entrega, origem
from deap import algorithms, base, benchmarks, cma, creator, gp, tools
from lerBrasil58 import distancias, custoCaminho

#para alterar para o flyfood, colocar "flyfood"
problema = "brasil58"

#consta em inglês na documentação, mantive igual
#segue trecho: https://deap.readthedocs.io/en/master/tutorials/basic/part1.html
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

tamanho_populacao = 1000
tamanho_torneio = 3
probabilidade_cruzamento = 0.8
probabilidade_mutacao = 0.2
quantidade_geracoes = 3000
lista_pontos = list(total_pontos_entrega)

if problema == "flyfood":
    quantidade_pontos = len(lista_pontos)
else:
    quantidade_pontos = 58

def avaliar_rota(individuo):
    rota = []

    if problema == "flyfood":
        for indice in individuo:
            rota.append(lista_pontos[indice])
        custo_rota = calcular_custo_rota(origem, total_pontos_entrega, rota)
        
    else:
        for indice in individuo:
            rota.append(indice + 1)
        custo_rota = custoCaminho(rota, distancias)

    return (custo_rota,)

def mutacao_insercao(individuo):
    posicao_retirada, posicao_nova = random.sample(range(len(individuo)), 2)
    ponto = individuo.pop(posicao_retirada)
    individuo.insert(posicao_nova, ponto)
    return (individuo,)

#toolbox evaluate, mate, mutate e select precisam estar em inglês devido ao eaMuPlusLambda, conforme descrito em documentação do deap
toolbox = base.Toolbox()
toolbox.register("gerar_rota_aleatoria", random.sample, range(quantidade_pontos), quantidade_pontos)
toolbox.register("criar_individuo", tools.initIterate, creator.Individual, toolbox.gerar_rota_aleatoria)
toolbox.register("criar_populacao", tools.initRepeat, list, toolbox.criar_individuo)
toolbox.register("evaluate", avaliar_rota)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", mutacao_insercao)
toolbox.register("select", tools.selBest)

populacao = toolbox.criar_populacao(tamanho_populacao)

#a aplicação do halloffame foi utilizando o repositório do deap no github como referência
#exemplo de uso: https://github.com/DEAP/deap/blob/master/examples/ga/tsp.py
melhores_rotas = tools.HallOfFame(1)

tempo_inicial = time.time()
algorithms.eaMuPlusLambda(populacao, toolbox, tamanho_populacao, tamanho_populacao, probabilidade_cruzamento, probabilidade_mutacao, quantidade_geracoes, halloffame=melhores_rotas, verbose=False)
tempo_total = time.time() - tempo_inicial

melhor_individuo = melhores_rotas[0]
melhor_rota = []

if problema == "flyfood":
    for indice in melhor_individuo:
        melhor_rota.append(lista_pontos[indice])

    custo_melhor_rota = calcular_custo_rota(origem, total_pontos_entrega, melhor_rota)

else:
    for indice in melhor_individuo:
        melhor_rota.append(indice + 1)
        
    custo_melhor_rota = custoCaminho(melhor_rota, distancias)

print(f"melhor rota: {melhor_rota}")
print(f"custo: {custo_melhor_rota}")
print(f"tempo: {tempo_total:.2f} segundos")