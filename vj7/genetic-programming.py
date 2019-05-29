# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:48:39 2019

@author: Sandi Šegota
"""

"""
An example of genetic programming

The goal is to get number 29 using numbers in range [1,7]
"""

import random
import datetime

numbers = [1,2,3,4,5,6,7]
operations = ['+','-']

expectedTotal = 29 #vrijednost koju ciljamo

optimalLengthSolution = [7,'+',7,'+',7,'+',7,'+',7,'-',6]
minNumbers = (1 + len(optimalLengthSolution))/2
print("minNumbers = " + str(minNumbers))
maxNumbers = 6*minNumbers
print("maxNumbers = "+str(maxNumbers))

startTime = datetime.datetime.now()

def createPopulation(numbers,operations,minNumbers,maxNumbers):
    genes = [random.choice(numbers)]
    print("genes = "+str(genes))
    count = random.randint(minNumbers, 1+maxNumbers)
    print("count = "+ str(count))
    while count > 1:
        count -=1
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))
    return genes

def evaluate(genes):
    result = genes[0]
    #uzimamo svaki drugi da preskocimo brojeve
    for i in range(1, len(genes),2):
        operation = genes[i]
        nextValue = genes[i+1]
        if operation == '+':
            result += nextValue
        elif operation == '-':
            result-=nextValue
    return result

def getFitness(genes, expectedTotal):
    result = evaluate(genes)
    print("result = " + str(result))
    if result != expectedTotal:
        fitness = expectedTotal - abs(result - expectedTotal)
        print("fitness = " + str(fitness))
    else:
        fitness = 1000 - len(genes)
        print("fitness = " + str(fitness))
    return fitness

def mutate(genes, numbers, operations, minNumbers, maxNumbers):
    numberCount = (1+len(genes))/2
    appending = numberCount < maxNumbers and random.randint(0,100) == 0
    if appending:
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))
        return genes
    removing = numberCount > minNumbers and random.randint(0,20) == 0
    if removing:
        index = random.randrange(0, len(genes)-1)
        del genes[index]
        del genes[index]
        return genes
    index = random.randrange(0, len(genes)-1)
    genes[index] = random.choice(operations) if (index & 1) == 1 \
    else random.choice(numbers)
    return genes

def diplay(candidate, fitness, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(''.join(map(str,candidate)), fitness, timeDiff))
    
    
bestParent = createPopulation(numbers, operations, minNumbers,maxNumbers)
print("bestParent = " + str(bestParent))

evalParent = evaluate(bestParent)
print("result of best parent = " + str(evalParent))

parentFitness = getFitness(bestParent, expectedTotal)
display(bestParent, parentFitness, startTime)

while True:
    child = mutate(bestParent, numbers, operations, minNumbers, maxNumbers)
    #print("child = " + str(child))
    evalChild = evaluate(child)
    
    childFitness = getFitness(child, expectedTotal)
    
    display(child, childFitness, startTime)
    
    if evalChild == expectedTotal:
        break
    bestParent = child
    
    
    
    
    
    
    
    
    
    
    
    
    
    