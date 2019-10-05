import numpy as np
import copy
from tab import Tab

class SA():
    def __init__(self,tab,tf,it):
        self.tab = tab
        self.tf = tf
        self.it = it
        
    def random_tab(self,m):
        queens0 = np.arange(m)
         
        for i in range(m-1,0,-1):
            x = np.random.randint(m)
            queens0[i],queens0[x] = queens0[x],queens0[i]
            
        return Tab(queens0)
        
    def P(self,delta,tempAtual):
        try:
            return np.exp(delta/tempAtual)    
        except OverflowError:
            return 1    
    
    def pertub(self,tab,swaps):
        x = np.random.randint(tab.n,size=swaps)
        for i in range(swaps-1):
            tab.queens[x[i]],tab.queens[x[i+1]] = tab.queens[x[i+1]],tab.queens[x[i]]
            
        return tab
    
    
    
    def run(self,):
        alpha = 0.1
        n = self.tab.n
        
        current,best = self.tab,self.tab
        aux = self.random_tab(n)
        aux2 = copy.deepcopy(aux)
        
        FA_best = best.AF()
        
        T = (FA_best*alpha) / np.log(n) 
        lbda = (self.tf/T) ** (1.0/self.it)
      
        for i in range(self.it):
            if T > self.tf:
                current=self.pertub(aux,8)
                if aux2.AF() > current.AF():
                    aux = copy.deepcopy(current)
                    if best.AF() > aux.AF():
                        best = copy.deepcopy(aux)
                elif np.random.randn() <  self.P(aux.AF() - current.AF(), T):
                    aux = copy.deepcopy(current)
            
            T *= lbda
        
        
        return best.AF(),best