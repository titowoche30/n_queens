# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:14:00 2019

@author: Malu Maia
"""

from tab import Tab
import numpy as np
from board import Board
from pprint import pprint
from time import sleep
import heapq as heap
from itertools import product

from datetime import datetime as date

class GA():    
    def __init__(self,board_size, generation_size, max_generations, mutation_rate, crossover_rate):
        self.board_size = board_size
        self.generation_size = generation_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.current_generation = [Board(self.board_size) for _ in range(self.generation_size)]
        self.best_element = min(self.current_generation)
        
        self.upper_bound = self.generation_size-2
        self.upper_bound = self.upper_bound if self.upper_bound % 2 == 0 else self.upper_bound-1
        self.all_positions = set(range(self.board_size))

    def generation_fitness(self, n=0):
        n = n if n > 0 else self.generation_size
        return sum(ind.fitness for ind in self.current_generation[:n])

    def proportional_selection(self):
        '''
        OBS_1: We're calculating the total colisions of each board, so,
        higher the value is, lower is the probability of the element
        be chosen. Let P(x_i) be the proportion of element x_i (x_i.fitness/generation_fitness),
        we take 1 - P(x_i) of all elements. We know SUM{i=1, n}(P(x_i)) = 1, but we want
        SUM{i=1, n}(1 - P(x_i)) be equals 1. (n = generation_size)

            SUM{i=1, n}(1 - P(x_i)) = SUM{i=1, n}(1) - SUM{i=1, n}(P(x_i))
                                    = (n - 1 + 1) * 1 - 1
                                    = n - 1

        In order to get SUM{i=1, n}(1 - P(x_i)) = 1, we must divide it by n - 1
        '''

        next_generation = self.generation_size * [None]
        gen_fit = self.generation_fitness()
        probs = [ # OBS_1
            (1 - ind.fitness/gen_fit) / (self.generation_size-1)
            for ind in self.current_generation
        ]

        best = float('inf')
        for i in range(self.generation_size):
            el_idx = np.random.choice(range(self.generation_size), p=probs)
            next_generation[i] = self.current_generation[el_idx]

            # Keep tracking of the best element of the new generation
            if next_generation[i] < best:
                best = next_generation[i]

        self.current_generation = next_generation
        self.best_element = best

    def __assemble_child(self, parent_1, parent_2):
        '''
            Let god guides you 1
        '''

        new_pos = self.board_size * [None]
        seen = []

        for (i, j) in parent_1:
            new_pos[i] = j
            seen.append(j)

        for (i, j) in parent_2:
            if j not in seen:
                new_pos[i] = j

        uniques = list(self.all_positions - set(new_pos))
        np.random.shuffle(uniques)
        uniques = iter(uniques)

        for i in range(self.board_size):
            if new_pos[i] is None:
                new_pos[i] = next(uniques)

        return Board(self.board_size, new_pos)

    def crossover(self):
        '''
        Let god guides you 2
        '''
        for i in (0, self.upper_bound, 2):
            if np.random.random() < self.crossover_rate:

                parent_1 = self.current_generation[i]
                parent_2 = self.current_generation[i+1]

                # Get all the pairs in the form of (i , V[i]) that has no colisions
                # all_positions = {k : 0 <= k < board_size}
                no_conflicts_1 = self.all_positions - set(parent_1.conflicts)
                no_conflicts_1 = set((row, parent_1[row]) for row in no_conflicts_1)

                no_conflicts_2 = self.all_positions - set(parent_2.conflicts)
                no_conflicts_2 = set((row, parent_2[row]) for row in no_conflicts_2)

                self.current_generation[i] = self.__assemble_child(no_conflicts_1, no_conflicts_2)
                self.current_generation[i+1] = self.__assemble_child(no_conflicts_2, no_conflicts_1)

                # Check if one of the 2 new elements is best than the current best
                if self.current_generation[i] < self.best_element:
                    self.best_element = self.current_generation[i]

                if self.current_generation[i+1] < self.best_element:
                    self.best_element = self.current_generation[i+1]

    def mutation(self):
        '''
        Swap 2 randomly selected queens
        '''
        for i in range(self.generation_size):
            if np.random.random() < self.mutation_rate:
                idx1, idx2 = np.random.randint(0, self.board_size), np.random.randint(0, self.board_size)
                new_pos = self.current_generation[i]
                new_pos[idx1], new_pos[idx2] = new_pos[idx2], new_pos[idx1]
                self.current_generation[i] = Board(self.board_size, new_pos)

                # Check if mutation has created a best element than the current one
                if self.current_generation[i] < self.best_element:
                    self.best_element = self.current_generation[i]

    def run(self):
        i = 1

        before = date.now()
        while not any(self.current_generation): # or i <= self.max_generations

            print('GEN: {:>10d}, GEN_FIT: {:>10d}, BEST_IND: {}  '.format(
                i, self.generation_fitness(), repr(self.current_generation[0])
            ), end='\r', flush=True)

            self.proportional_selection()
            self.crossover()
            self.mutation()

            i += 1

        self.best_element = min(self.current_generation)

        print((80 + self.board_size) * ' ')
        print('\nLAST GENERATION: ' + str(i))
        print('LAST GENERATION FITNESS: ' + str(self.generation_fitness()))
        print('ELAPSED TIME: ' + str(date.now() - before))

        pprint(self.current_generation)
        print('')
        print(self.best_element)
