# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:14:00 2019

@author: Malu Maia
"""

from tab import Tab
import random
import numpy as np

class GA():    
    def __init__(self,tab,k,n_geracoes,tx_mutacao):
        self.tab = tab
        self.queens = tab.queens
        self.k = k
        self.n_geracoes = n_geracoes
        self.tx_mutacao = tx_mutacao
        self.geracao = 0
        self.populacao = []
        
    def populacao_inicial(self):
        _queens = np.copy(self.queens)
        for _ in range(0,self.k):
            _queens = np.random.permutation(_queens)
            self.populacao.append(_queens)
        print(type(self.populacao))
        
    def soma_AF(self):
        soma=0
        for individuo in self.populacao:
            soma += Tab(individuo).AF()
        return soma
    
    
    def seleciona_individuo_cruzamento(self,populacao):
        melhor = float('inf')
        melhor_individuo = populacao[0]
        print(type(melhor_individuo))
        for individuo in populacao:
            print("oi")
            individuo_AF = Tab(individuo).AF()
            if(individuo_AF < melhor and random.random() < (individuo_AF/self.soma_AF())):
                print("teste")
                melhor = Tab(individuo).AF()
                melhor_individuo = individuo
        return type(melhor_individuo)
    
    def crossover(self):
#        indice = 0
        limite_print = '-'*70
        copia_populacao = self.populacao
        filhos = []
        
        for _ in (0,self.k,2):
            mae = self.seleciona_individuo_cruzamento(copia_populacao)
            
            print(limite_print)
            print("mae: ", mae)
            copia_populacao.remove(mae)
            print(limite_print)
            print(copia_populacao)
            
            pai = self.seleciona_individuo_cruzamento(copia_populacao)
            
            print(limite_print)
            print("pai: ",pai)
            copia_populacao.remove(pai)
            print(limite_print)
            print(copia_populacao)
            
            c = random.randint(1,self.tab.n)
            
            print(limite_print)
            print("c: {}".format(c))
            print(limite_print)
            
            filho1 = np.concatenate(mae[0:c], pai[c:self.tab.n], axis=None)
            filho2 = np.concatenate(pai[0:c], mae[c:self.tab.n], axis=None)  
            
            filhos.append(filho1)
            filhos.append(filho2)
        
        populacao_full = np.concatenate(filhos,self.populacao,axis=None)
        
        AFs = [{
            'AF': ind.AF(),
            'Indivíduo': ind
        } for ind in populacao_full]
    
        sorted(AFs,key=lambda elemento:elemento['AF'],reverse=True)
        print(AFs)
        
        
        def run():
            self.populacao_inicial()
            for geracao in range(self.n_geracoes):
                self.crossover()
                self.geracao += 1
            
            
                
                
                
                
        
        
        
    