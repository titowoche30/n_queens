import numpy as np

class Tab():
    def __init__(self,queens):
        #queens tem que ser np.array
        self.queens = queens
        self.n = queens.size
        
    def AF(self):
        #Quantidade de choques
        cont = 0
        
        #diag \
        for j in range(self.n):
            for k in range(j+1,self.n):
                if self.queens[j] - j == self.queens[k] - k:
                    #print('choque em {} e {}'.format(self.queens[j], self.queens[k]))
                    cont+=1
        
        #diag /
        for j in range(self.n):
            for k in range(j+1,self.n):
                if self.queens[j] + j == self.queens[k] + k: 
                    #print('choque em {} e {}'.format(self.queens[j],self.queens[k]))
                    cont+=1            
                    
        return cont
    
    
    def tabuleiro(self):
        var = ''
        for i in range(self.n):
            for j in range(self.n):
                if self.queens[i] == j:
                    var = var + '[X]'
                else:
                    var = var + '[]'
            var = var + '\n'
        
        return var
    