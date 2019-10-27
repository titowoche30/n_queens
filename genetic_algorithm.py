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

        for i in range(self.generation_size):
            el_idx = np.random.choice(range(self.generation_size), p=probs)
            next_generation[i] = self.current_generation[el_idx]

        self.current_generation = next_generation

    def __assemble_child(self, parent_1, parent_2):
        '''
            Let god guides you 1
        '''
        print(parent_1)
        print(parent_2)

        new_pos = self.board_size * [None]
        uniques = list(set((
            self.all_positions - 
            ((set(j for (i, j) in parent_1)) | set(j for (i, j) in parent_2))
        )))
        np.random.shuffle(uniques)

        print(new_pos)
        print(uniques)

        for (i, j) in parent_1:
            new_pos[i] = j

        for (i, j) in parent_2:
            new_pos[i] = j

        # print('UNIQUES LEN = ' + str(len(uniques)))
        # print('NONE LEN    = ' + str(len([None for p in new_pos if p is None])))
        # print(uniques)
        # print(new_pos)
        k = 0
        for i in range(self.board_size):
            if new_pos[i] is None:
                # a = next(uniques)
                # print(a)
                new_pos[i] = uniques[k]
                k += 1
        # print(new_pos)
        # print('')

        return Board(self.board_size, new_pos)

    def crossover(self):
        '''
        Let god guides you 2
        '''
        for i in (0, self.upper_bound, 2):
            if np.random.random() < self.crossover_rate:

                cross_point = np. random.randint(1, self.board_size-1)

                parent_1 = self.current_generation[i]
                parent_2 = self.current_generation[i+1]

                no_conflicts_1 = set(range(self.board_size)) - set(parent_1.conflicts)
                no_conflicts_1 = set((row, parent_1[row]) for row in no_conflicts_1)

                no_conflicts_2 = set(range(self.board_size)) - set(parent_2.conflicts)
                no_conflicts_2 = set((row, parent_2[row]) for row in no_conflicts_2)

                self.current_generation[i] = self.__assemble_child(no_conflicts_1, no_conflicts_2)
                self.current_generation[i+1] = self.__assemble_child(no_conflicts_2, no_conflicts_1)
                # input()

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

    def run(self):
        i = 0

        before = date.now()
        while not any(self.current_generation):

            heap.heapify(self.current_generation)            
            # print('GEN: {:>10d}, GEN_FIT: {:>10d}, BEST_IND: {}  '.format(
            #     i+1, self.generation_fitness(), repr(self.current_generation[0])
            # ), end='\r', flush=True)

            self.proportional_selection()
            self.crossover()
            self.mutation()

            i += 1

        print('\n\nLAST GENERATION: ' + str(i+1))
        print('LAST GENERATION FITNESS: ' + str(self.generation_fitness()))
        print('ELAPSED TIME: ' + str(date.now() - before))

        heap.heapify(self.current_generation)
        pprint(self.current_generation)
        print('')
        print(self.current_generation[0])