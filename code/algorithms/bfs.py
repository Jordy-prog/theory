import copy

def bfs(RushHour):
    archive = set()
    archive.add(str(RushHour.matrix))
    queue = []
    queue.append(RushHour)

    knowndepths = set()
    while len(queue):
        parent = queue.pop(0)
        for car in parent.cars.values():
            free_space = car.look_around(parent)
            for distance in range(free_space['front']):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], distance + 1)
                if child.game_won():
                    return True
                if str(child.matrix) not in archive:
                    archive.add(str(child.matrix))
                    queue.append(child)
            
            for distance in range(0, free_space['rear'], -1):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], (distance - 1))
                if child.game_won():
                    return True
                if str(child.matrix) not in archive:
                    archive.add(str(child.matrix))
                    queue.append(child)
        if len(child.steps) not in knowndepths:
            knowndepths.add(len(child.steps))
            print(len(child.steps))
        
        
            