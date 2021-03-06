# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:01:09 2019

@author: Student
"""
import random
import datetime

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "This is my first implementation of genetic algorithm."

startTime = datetime.datetime.now()

def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length-len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return genes

def get_fitness(guess):
    return sum(1 for expected, actual in zip(target,guess) if expected == actual)

def mutate(parent):
    index = random.randrange(0,len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{} \t {} \t {}".format(guess, fitness, timeDiff))
    
random.seed()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)

display(bestParent)


while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
