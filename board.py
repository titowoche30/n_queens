from random import shuffle


class Board:

    def __init__(self, size, positions=None):
        self.size = size
        if positions is None:
            self.positions = list(range(self.size))
            shuffle(self.positions)
        else:
            self.positions = positions
        self.fitness, self.conflicts = self.__evaluate(True)

    def __evaluate(self, count_conflicts=False): # Evaluation function
        #Quantidade de choques
        cont = 0
        conflicts = set({})
        
        #diag \
        for j in range(self.size):
            for k in range(j+1,self.size):
                if self.positions[j] - j == self.positions[k] - k:
                    cont += 1
                    if count_conflicts: conflicts |= {j, k}
        
        #diag /
        for j in range(self.size):
            for k in range(j+1,self.size):
                if self.positions[j] + j == self.positions[k] + k: 
                    cont += 1
                    if count_conflicts: conflicts |= {j, k}
                    
        return cont, list(set(conflicts))

    def __bool__(self):
        return self.fitness == 0

    def __lt__(self, el):
        if isinstance(el, Board):
            return self.fitness < el.fitness

        if isinstance(el, (int, float)):
            return self.fitness < el

    def __getitem__(self, idx):
        return self.positions[idx]

    def __setitem__(self, idx, value):
        self.positions[idx] = value

    def __len__(self):
        return self.size

    def __str__(self):
        _str = ''
        for i in range(self.size):
            for j in range(self.size):
                if self.positions[i] == j:
                    _str += '[\033[30;42mX\033[m]' if i not in self.conflicts else '[\033[30;41mX\033[m]'
                else:
                    _str += '[]'
            _str += '\n'
        # _str += 'conflicts = ' + str(self.conflicts)
        _str += repr(self)
        
        return _str

    def __repr__(self):
        _str = '{'
        for i in range(self.size):
            _str += '\033[32mX\033[m' if i not in self.conflicts else '\033[31mX\033[m'
        
        _str += ', ' + str(self.fitness) + '}'

        return _str
