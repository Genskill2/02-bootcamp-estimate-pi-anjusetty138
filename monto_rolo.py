import math
import random

#input the no.of darts thrown for the estimation
darts = int(input('no.of darts thrown:'))

#let the initial no. of dart inside circle be 0
count_in_circle = 0   

for i in range(0,darts):

    #take the random location of dart
    x = random.random()
    y = random.random()
    distance = math.sqrt((x**2)+(y**2))

    #if the dart lies inside the circle
    if distance < 1.0:
        count_in_circle += 1

print('The estimated pi value is: {}'.format((count_in_circle/darts)*4))