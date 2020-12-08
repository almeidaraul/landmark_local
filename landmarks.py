import math
from random import randint

def main():
    m = [[0]*10000 for i in range(10000)]
    print("Map is {}x{}".format(len(m), len(m[0])))

    n_lands = randint(5, 11)
    landmarks = []
    landmarks = [[randint(0, 9999), randint(0, 9999)] for l in range(n_lands)]

    for l in landmarks:
        m[l[0]][l[1]] = 'L'

    robot = [randint(0, 9999), randint(0, 9999)]
    m[robot[0]][robot[1]] = 'R'

    angle = randint(0, 23) * 15
    equation_angle = angle + 90

    #robot[0] = 0
    #robot[1] = 0
    #angle = 0

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

    print("{} landmarks".format(len(landmarks)))
    for i in range(len(landmarks)):
        print("Landmark #{} is at ({}, {})".format(i,
            landmarks[i][0],
            landmarks[i][1]
            ))

    print("{} landmarks found".format(len(landmarks_found)))
    for i in range(len(landmarks_found)):
        print("Landmark Found #{} is at ({}, {})".format(i,
            landmarks_found[i][0],
            landmarks_found[i][1]
            ))

    print("Robot is at ({}, {}) and {} degrees".format(robot[0], robot[1], angle))#    print("")

if __name__ == '__main__':
    main()
