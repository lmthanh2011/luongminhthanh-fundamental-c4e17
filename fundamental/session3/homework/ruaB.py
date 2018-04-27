from turtle import *
speed (5)
shape ('triangle')

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (5):
    color (colors[i])
#ve hinh
    for canh in range (i+3):
        forward (100)
        goc = 360/(i+3)
        left (goc)
mainloop()
