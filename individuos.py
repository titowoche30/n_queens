from random import random, randint

class Individuo():
    def __init__(self, tab, tx_mutacao, geracao=0):
        self.tab = tab
        self.tx_mutacao = tx_mutacao
        self.cromossomo = []
    
    def crossover(self, mae, pai):
        n = len(mae)
        c = round(random()*n-1)
        metade1_filho1 = mae[0:c]
        metade2_filho1 = pai[c:n]
        metade1_filho2 = pai[0:c]
        metade2_filho2 = mae[c:n]
        filho1 = []
        filho2 = []
        for i in range(0,c):
            filho1.append(metade1_filho1[i])
            filho2.append(metade1_filho2[i])
        for j in range(0,n-c):
            filho1.append(metade2_filho1[j])
            filho2.append(metade2_filho2[j])
        
        filhos = [Individuo(self, self.tab, self.tx_mutacao, self.geracao+1),
                  Individuo(self, self.tab, self.tx_mutacao, self.geracao+1)]
        filhos[0],filhos[1] = filho1, filho2
        
        return filhos
        
    def mutacao(self, tx_mutacao):
        if (random() < tx_mutacao):
            indice_mutacao = round(random()*len(self.tab)-1)
            quadrado_aleatorio = randint(0,len(self.tab)+1)
            self.tab.queens[indice_mutacao] = quadrado_aleatorio
        self.cromossomo = self.tab.queens
        
        return self
    
    
            