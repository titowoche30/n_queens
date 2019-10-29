import numpy as np
#from SA import SA
#from HC import HC
from tab import Tab
from genetic_algorithm import GA
from board import Board
import sys
from SA import SA

#queen = [5,3,2,1,4,0]         Coluna da rainha da linha i.
#                              Nesse exemplo a rainha da linha 0 estaria 
#                              na coluna 5, a rainha da linha 1 na coluna 3
#i x v[i]

if __name__ == '__main__':
    n = int(sys.argv[1])

    # b = Board(n)
    # print(b)
    
    limite = '*'*30
    print(limite+"GENETIC ALGORITHM"+limite)    
    

    ga = GA(n, 20, 10000, .005, .5)
    ga.run()


    ##---------------------SA-----------------##
    
    queens = np.arange(0,n)
    tab = Tab(queens)
    
    print("\n\n"+limite+"SIMULATED ANNEALING"+limite)
    sa = SA(tab,0.000001,4000)
    aval,tab = sa.run()
    print('FITNESS =',aval)
    print(tab)
    
    
    ##---------------------HC-----------------##
#    queens = np.arange(0,n)
#    
#    tab2 = Tab(queens)
#    hc = HC(tab2)
#    aval,tab2=hc.run()
#    
#    print('aval do HC=',aval)
#    tabHC = tab2.tabuleiro()