from turtle import *
speed (0)
shape ('triangle')

mau = ["red","blue","red", "blue"]
for i in range (4):
    color (mau[i])
#ve hinh
    for canh in range (i+3):
        forward (100)
        goc = 360/(i+3)
        left (goc)
mainloop()
