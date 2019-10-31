import numpy as np
import copy
#from board import Board
from tab import Tab

class SA():
    def __init__(self,tab,tf,it): #tf: final temperature -------- it: quantity of iterations
        self.tab = tab
        self.tf = tf
        self.it = it
 
    def random_tab(self,m):
        queens0 = np.arange(m)
        np.random.shuffle(queens0)
        return Tab(queens0)

        
    def P(self,delta,tempAtual): #probability of a solution be accepted, based on the formula.
        try:
            return np.exp(delta/tempAtual)
        except OverflowError:
            return 1    
    
    
    def pertub(self,tab,swaps): #apply a perturbation, swapping the positions of queens.
        tab = copy.deepcopy(tab)                    #Só aceite.
        x = np.random.randint(0,tab.n,size=swaps)
        for i in range(swaps-1):
            tab.queens[x[i]],tab.queens[x[i+1]] = tab.queens[x[i+1]],tab.queens[x[i]]
            
        return tab
                
    
    def run(self):
        alpha = 0.1
        n = self.tab.n
    
        current = copy.deepcopy(self.tab)
        best = copy.deepcopy(self.tab)
        aux = copy.deepcopy(self.random_tab(n))
        
        FA_best = best.AF()
        
        T = (FA_best*alpha) / np.log(n)
        lbda = (self.tf/T) ** (1.0/self.it)
        
        for i in range(self.it):
            if T > self.tf:
                current=self.pertub(aux,2)
                if aux.AF() > current.AF():
                    aux = copy.deepcopy(current)
                    if best.AF() > aux.AF():
                        best = copy.deepcopy(aux)
                        print('BEST_EVALUATE =',best.AF())
                elif np.random.rand() <  self.P(aux.AF() - current.AF(), T):
                    aux = copy.deepcopy(current)
                        
            T *= lbda
        
        return best.AF(),best