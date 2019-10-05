from tab import Tab


class HC():
    def __init__(self,tab):
        self.tab = tab
        
        
        
        
        
    def run(self):
        n = self.tab.n
        best = self.tab.AF()
        imp = True        
        while imp:
            imp = False
            for i in range(n):
                for j in range(i):
                    self.tab.queens[i],self.tab.queens[j] = self.tab.queens[j],self.tab.queens[i]
                    nz = self.tab.AF()
                    if nz<best:
                        imp = True
                        best = nz
                        #print('FA no HC=',best)
                        if best==0: 
                            return best,self.tab
                    else:
                        self.tab.queens[i],self.tab.queens[j] = self.tab.queens[j],self.tab.queens[i]
        
        
        return best,self.tab