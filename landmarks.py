from random import randint

m = [[0]*100 for i in range(100)]
print("Map is {}x{}".format(len(m), len(m[0])))

n_lands = randint(5, 11)
landmarks = []
landmarks = [[randint(0, 99), randint(0, 99)] for l in range(n_lands)]

for l in landmarks:
    m[l[0]][l[1]] = 'L'

robot = [randint(0, 99), randint(0, 99)]
while robot in landmarks:
    robot = [randint(0, 99), randint(0, 99)]

m[robot[0]][robot[1]] = 'R'


print("{} landmarks".format(len(landmarks)))
for i in range(len(landmarks)):
    print("Landmark #{} is at ({}, {})".format(i,
                                               landmarks[i][0],
                                               landmarks[i][1]
                                              ))
print("Robot is at ({}, {})".format(robot[0], robot[1]))

#for line in m:
#    for c in line:
#        print(c, end=' ')
#    print("")
