import os

from code.algorithms import random, hillclimb, bfs


def test(RushHour, algorithm, to_print):
    '''
    A function that does a single run of an algorithm.
    '''
    # plays game until won
    while not RushHour.game_won():
        # prints gameboard
        if to_print == 'yes':
            os.system('cls')
            RushHour.printboard()

        # algorithm selection
        if algorithm == '1':
            random.random_pure(RushHour)
        elif algorithm == '2':
            random.random_constraint(RushHour)
        elif algorithm == '3':
            hillclimb.hillclimb(RushHour)
        elif algorithm == '4':
            bfs.bfs(RushHour)
            