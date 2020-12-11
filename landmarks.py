import math
from random import randint, uniform
from itertools import combinations
from pprint import pprint
from scipy.optimize import fsolve

def introduce_error(v):
    return uniform(v*0.95, v*1.05)

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def func(pr, x1, y1, x2, y2, x3, y3, d1, d2, d3):
    return [
            pr[0]*2*(x2-x1) + pr[1]*2*(y2-y1) + x1**2 - x2**2 + y1**2 - y2**2 - d1**2 + d2**2,
            pr[0]*2*(x3-x1) + pr[1]*2*(y3-y1) + x1**2 - x3**2 + y1**2 - y3**2 - d1**2 + d3**2
        ]

def teste(pr, x1, y1, x2, y2, x3, y3, d1, d2, d3):
    pprint ([
            pr[0]*2*(x2-x1) + pr[1]*2*(y2-y1) + x1**2 - x2**2 + y1**2 - y2**2 - d1**2 + d2**2,
            pr[0]*2*(x3-x1) + pr[1]*2*(y3-y1) + x1**2 - x3**2 + y1**2 - y3**2 - d1**2 + d3**2
        ])


def calc_position(triangulation, landmarks, distances):
    args = [
            landmarks[triangulation[0]][0], landmarks[triangulation[0]][1],
            landmarks[triangulation[1]][0], landmarks[triangulation[1]][1],
            landmarks[triangulation[2]][0], landmarks[triangulation[2]][1],
            distances[triangulation[0]]['robot'], distances[triangulation[1]]['robot'], distances[triangulation[2]]['robot']
            ]

    #pprint(args)

    position = fsolve(func, [1, 1], tuple(args))

    #teste(position, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])

    return position


def main():
    size = 100
    m = [[0]*size for i in range(size)]
    print("Map is {}x{} ({:0.0f}x{:0.0f}m)\n".format(len(m), len(m[0]), len(m)/10, len(m[0])/10))

    n_lands = randint(5, 10)
    landmarks = [[randint(0, size-1), randint(0, size-1)] for l in range(n_lands)]

    for l in landmarks:
        m[l[0]][l[1]] = 'L'

    while True:
        robot = [randint(0, size-1), randint(0, size-1)]
        if robot not in landmarks:
            break
    m[robot[0]][robot[1]] = 'R'

    angle = randint(0, 23) * 15
    equation_angle = angle + 90

    landmarks_found = []

    i = 0

    if angle == 0:
        for landmark in landmarks:
            if landmark[0] > robot[0]:
                landmarks_found.append(i)
            i += 1

    elif angle == 180:
        for landmark in landmarks:
            if landmark[0] < robot[0]:
                landmarks_found.append(i)
            i += 1

    else:
        tan = math.tan(math.radians(equation_angle))
        b = -robot[0]*tan + robot[1]

        for landmark in landmarks:
            if angle <= 180:
                if landmark[0]*tan + b < landmark[1]:
                    landmarks_found.append(i)
            else:
                if landmark[0]*tan + b > landmark[1]:
                    landmarks_found.append(i)
            i += 1

    print("{} landmarks ({} found):".format(len(landmarks), len(landmarks_found)))
    for i in range(len(landmarks)):
        found = True if i in landmarks_found else False
        print("Landmark #{} is at ({}, {}){}".format(i,
            landmarks[i][0],
            landmarks[i][1],
            " (found)\n" if found else "\n"
            ), end='')

    print("\nRobot is at ({}, {}) and {} degrees\n".format(robot[0], robot[1], angle))

    distances = [
                {'real': dist(robot, landmark), 'robot': introduce_error(dist(robot, landmark))}
                for landmark in landmarks
            ]

    for d in range(len(distances)):
        print("Distance to found landmark #{} is {:0.2f}m, robot estimated {:0.2f}m"
                .format(d, distances[d]['real']/10, distances[d]['robot']/10))


    triangulations = list(combinations(landmarks_found, 3))
    positions = []

    for triangulation in triangulations:
        pprint(triangulation)
        positions.append(calc_position(triangulation, landmarks, distances))

    pprint(positions)

if __name__ == '__main__':
    main()
