import numpy as np
#from SA import SA
#from HC import HC
from tab import Tab
from GA import GA

#queen = [5,3,2,1,4,0]         Coluna da rainha da linha i.
#                              Nesse exemplo a rainha da linha 0 estaria 
#                              na coluna 5, a rainha da linha 1 na coluna 3
#i x v[i]

if __name__ == '__main__':
    n = 40
    ##---------------------SA-----------------##
    queens = np.arange(0,n)
    tab = Tab(queens)
#    
#    sa = SA(tab,0.000001,4000)
#    aval,tab = sa.run()
#    print('aval=',aval)
#    print(tab)
        
    ga = GA(tab,10,20,0.01)
    pi = ga.populacao_inicial()
    ga.seleciona_individuo_cruzamento()
    ga.crossover()
    
    
    #tabSA = tab.tabuleiro()
    
    ##---------------------HC-----------------##
#    queens = np.arange(0,n)
#    
#    tab2 = Tab(queens)
#    hc = HC(tab2)
#    aval,tab2=hc.run()
#    
#    print('aval do HC=',aval)
#    tabHC = tab2.tabuleiro()