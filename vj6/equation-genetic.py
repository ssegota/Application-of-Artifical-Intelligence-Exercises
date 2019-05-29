# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:29:51 2018

@author: AdriaTINN-PC
"""

import random 

geneSet = [i for i in range(0,10)]
crossrate = 0.25
mutecoeff = 0.1
def InitialPopulation(geneSet):
    population = [[] for i in range(0,6)]
    targetLen = 4
    for i in range(0, len(population)):
        population[i].extend(random.sample(geneSet,targetLen))
    return population 
def FintessFunction(population): 
    F_obj = []
    for i in range(len(population)): 
        result = 0 
        result = abs((population[i][0] + 2*population[i][1] +\
                      3*population[i][2] + 4*population[i][3]) - 30)
        F_obj.append(result)
    print( "F_obj = " + str(F_obj))
    Fitness = []
    for i in range(len(F_obj)):
        result = 0 
        result = 1.0/(1 + F_obj[i])
        Fitness.append(result)
    print( "Fitness = " + str(Fitness))
    Total = sum(Fitness)
    Probability = [] 
    for i in range(len(Fitness)):
        Probability.append(Fitness[i]/Total)
    C_probability = []; cumulative = 0
    for i in range(len(Probability)):
        cumulative += Probability[i]
        C_probability.append(cumulative)
    print( "Cumulative Probability = " + str(C_probability))
    return F_obj, Fitness, Probability, C_probability
def generatingNewPopulation(population, C_probability): 
    R0 = [] 
    for i in range(len(C_probability)):
        R0.append(random.random())
    print( "R0 = " + str(R0))
    newPop = []
    for i in range(len(population)):
        try:
            if R0[i] > C_probability[i] and R0[i] < C_probability[i+1]:
                newPop.append(population[i + 1])
            elif R0[i] < C_probability[i] and R0[i] < C_probability[len(C_probability)-1]:
                newPop.append(population[i-2])
            elif R0[i] > C_probability[i] and R0[i] > C_probability[i+1]:
                newPop.append(population[i+2])
        except IndexError:
            pass
    print( "population = " + str(population))
    print( "newPop = " + str(newPop))
    return newPop 
def Crossover(newPop, crossrate):
    R1 = []; k = 0; C = [];indexList = [];mem_crossover = []; 
    for i in range(len(newPop)):
        R1.append(random.random())
    print( "R1 = " + str(R1))
    while k < len(newPop):
        if R1[k] < crossrate:
            indexList.append(k)
            mem_crossover.append(newPop[k])
        k += 1
    print( "mem_crossover = " + str(mem_crossover))
    for i in range(len(mem_crossover)): 
        C.append(random.randint(1,3))
    print( "C = " + str(C))
    newCrossChrom = [[] for i in range(len(mem_crossover))]
    for i in range(len(mem_crossover)):
        if i == len(mem_crossover) - 1:
            newCrossChrom[i].extend(mem_crossover[i][0:C[i]])
            newCrossChrom[i].extend(mem_crossover[0][C[i]:len(mem_crossover[i])]) 
        else: 
            newCrossChrom[i].extend(mem_crossover[i][0:C[i]])
            newCrossChrom[i].extend(mem_crossover[i+1][C[i]:len(mem_crossover[i])])
    for i in range(len(newPop)): 
        for j in range(len(indexList)):
            if indexList[j] == i:
                newPop[i] = newCrossChrom[j]
    newCrossPop = newPop#list(filter(None, newPop))            
    print( "newPopCross = " + str(newPop))
    print( "newPopCross = " + str(newCrossPop))
    return newCrossPop 

def mutation(newPop, mutecoeff): 
    totalGenes = len(newPop)*len(newPop[0])
    no_of_mutations = int(mutecoeff * totalGenes) 
    position = [random.randint(0,24) for i in range(no_of_mutations)] 
    print( "position = " + str(position))
    z = 0
    print( "newPop = " + str(newPop))
    for i in range(len(newPop)):
        for j in range(len(newPop[i])):
            for o in range(len(position)): 
                if position[o] == z: 
                    newPop[i][j] = random.choice(geneSet)
            z += 1
    return newPop

population = InitialPopulation(geneSet)
F_obj, Fitness, Probability, C_probability = FintessFunction(population)
k = 0; 
while True: 
    print( "Iteration No. {0}".format(str(k)))
    newPopulation = generatingNewPopulation(population, C_probability)
    newPopulation2 = Crossover(newPopulation, crossrate)
    newPopulation3 = mutation(newPopulation2, mutecoeff)
    print( "newPopulation3 = " + str(newPopulation3))
    F_obj, Fitness, Probability, C_prob2 = FintessFunction(newPopulation3)
    for i in range(len(F_obj)):
        print( "F_obj = " + str(F_obj[i]))
    expectedResult = 0 
    if expectedResult in F_obj:
        index = F_obj.index(expectedResult)
        print( "The solution is = " + str(newPopulation3[index]))
        break
    else: 
        pass   
    population = newPopulation3 
    C_probability = C_prob2   
    k += 1