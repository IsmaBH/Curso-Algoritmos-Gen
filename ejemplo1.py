import random
from deap import base
from deap import creator
from deap import tools

def funcion_objetivo(x):
    """
    Funcion objetivo del problema, en escencia es el elemento que va a evaluar
    a cada indivuo de la poblacion
    """
    for i in range(len(x)):
        if x[i] > 100 or x[i] < -100:
            return -1
        res = math.sqrt(x[0]**2 + x[1]**2)
    return res

#Creamos los ejemplos para definir el problema y el tipo de individuo
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

#Generacion de genes
toolbox.register("attr_uniform", random.uniform, -100, 100)

#Generacion de individuos y poblacion
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_uniform, 2)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

individuo = toolbox.individual()
poblacion = toolbox.population()
