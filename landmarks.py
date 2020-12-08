import math
from random import randint, uniform

def introduce_error(v):
    return uniform(v*0.9, v*1.1)

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def main():
    size = 100
    m = [[0]*size for i in range(size)]
    print("Map is {}x{} ({:0.0f}x{:0.0f}m)\n".format(len(m), len(m[0]), len(m)/10, len(m[0])/10))

    n_lands = randint(5, 10)
    landmarks = []
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

    if angle == 0:
        for landmark in landmarks:
            if landmark[0] > robot[0]:
                landmarks_found.append(landmark)

    elif angle == 180:
        for landmark in landmarks:
            if landmark[0] < robot[0]:
                landmarks_found.append(landmark)

    else:
        tan = math.tan(math.radians(equation_angle))
        b = -robot[0]*tan + robot[1]

        for landmark in landmarks:
            if angle <= 180:
                if landmark[0]*tan + b < landmark[1]:
                    landmarks_found.append(landmark)
            else:
                if landmark[0]*tan + b > landmark[1]:
                    landmarks_found.append(landmark)

    print("{} landmarks ({} found):".format(len(landmarks), len(landmarks_found)))
    for i in range(len(landmarks)):
        found = True if landmarks[i] in landmarks_found else False
        print("Landmark #{} is at ({}, {}){}".format(i,
            landmarks[i][0],
            landmarks[i][1],
            " (found)\n" if found else "\n"
            ), end='')

    print("\nRobot is at ({}, {}) and {} degrees\n".format(robot[0], robot[1], angle))

    distances = [
                 {'real': dist(robot, l), 'robot': introduce_error(dist(robot, l))}
                 for l in landmarks_found
                ]
    for d in range(len(distances)):
        print("Distance to found landmark #{} is {:0.2f}m, robot estimated {:0.2f}m"
               .format(d, distances[d]['real']/10, distances[d]['robot']/10))

if __name__ == '__main__':
    main()
