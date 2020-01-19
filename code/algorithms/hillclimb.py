import copy
import os
import random
from sys import argv
from time import sleep

from .random import random_constraint
from ..classes import board


def hillclimb():
    # asks user how many times the algorithm should try to improve amount of moves
    slices, improvements, runtimes = 0, 0, 0
    
    while slices <= 0 or improvements <= 0 or runtimes <= 0:
        try:
            slices = int(input('Slices? '))
            improvements = int(input('Improvements per slice? '))
            runtimes = int(input('Times to run? '))
        except ValueError:
            pass

    info_dict = {'slices': slices, 'improvements': improvements, 'runtimes': runtimes}
    plotting_data = [info_dict]

    # runs the hillclimber a certain amount of times
    for i in range(runtimes):
        boardstates = []
        boardstates_indexes = {}
        plot_data = {}
        RushHour_initial = board.RushHour(f'data/{argv[1]}')
    
        # do a random run and save the moves that were done
        while not RushHour_initial.game_won():
            move = random_constraint(RushHour_initial)
            boardstates.append(move + (str(RushHour_initial.matrix),))

            if str(RushHour_initial.matrix) in boardstates_indexes:
                boardstates_indexes[str(RushHour_initial.matrix)].append(len(boardstates) - 1)
            else:
                boardstates_indexes[str(RushHour_initial.matrix)] = [len(boardstates) - 1]

        plot_data['initial'] = len(boardstates)
        # print('length:', len(boardstates))

        # cut that shit
        for boardstate in boardstates_indexes:
            print(boardstate)
            first = i

            for j, check in enumerate(boardstates[i + 1:], 1):
                if check[2] == boardstate[2]:
                    last = i + j
                    del boardstates[first:last]
                    break
        
        plot_data['elimination'] = len(boardstates)

        slice_times = 0

        while slice_times < slices:
            slice_times += 1
            print('slice:', slice_times)
            first_slice = 0
            last_slice = 0
            
            while last_slice - first_slice <= (len(boardstates) // 10):
                first_slice = random.randrange(0, len(boardstates) // 2)
                last_slice = random.randrange(len(boardstates) // 2, len(boardstates))
                
            boardstates_initial = boardstates[first_slice:last_slice]
            RushHour_template = board.RushHour(f'data/{argv[1]}')

            for boardstate in boardstates[:first_slice + 1]:
                RushHour_template.move(RushHour_template.cars[boardstate[0]], boardstate[1])

            improvement_times = 0

            while improvement_times < improvements:
                improvement_times += 1
                RushHour_new = copy.deepcopy(RushHour_template)
                boardstates_new = [boardstates_initial[0]]

                while not boardstates_new[-1][2] == boardstates_initial[-1][2] and len(boardstates_new) < len(boardstates_initial):
                    move = random_constraint(RushHour_new)
                    boardstates_new.append(move + (str(RushHour_new.matrix),))

                if len(boardstates_new) < len(boardstates_initial):
                    del boardstates[first_slice:last_slice]
                    print('Improved')
                    
                    for i, boardstate in enumerate(boardstates_new):
                        boardstates.insert(first_slice + i, boardstate)

                    break

            plot_data[str(slice_times)] = len(boardstates)
            print(len(boardstates))

        


        print(plot_data['initial'])
        print(len(boardstates))
        plotting_data.append(plot_data)
        
    return plotting_data

    # alle boardstates na slice van list in dictionary opslaan
    # dictionary met indexes van lijst voor het filteren van dubbele moves
    # selectieve eliminatie moet dan voor slicing!!