import numpy as np
from SA import SA
from HC import HC
from tab import Tab

#queen = [5,3,2,1,4,0]         Coluna da rainha da linha i.
#                              Nesse exemplo a rainha da linha 0 estaria 
#                              na coluna 5, a rainha da linha 1 na coluna 1
#i x v[i]

if __name__ == '__main__':
    n = 40
    ##---------------------SA-----------------##
    queens = np.arange(0,n)
    
    tab = Tab(queens)
    
    vet = list(range(1000,5001,500))
    
    for i in vet:
        sa = SA(tab,0.0001,i)
        aval,nada = sa.run()
        print('aval do SA com {} iteracoes={}'.format(i,aval))
    
    tabSA = tab.tabuleiro()
    
    ##---------------------HC-----------------##
#    queens = np.arange(0,n)
#    
#    tab2 = Tab(queens)
#    hc = HC(tab2)
#    aval,tab2=hc.run()
#    
#    print('aval do HC=',aval)
#    tabHC = tab2.tabuleiro()
