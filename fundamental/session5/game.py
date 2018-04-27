#hienmap
pattern =[]
n=0
# for y in range (4):
#     for x in range(4):
#         pattern.append("- ")
#     print(*pattern, end="\n")
#     del pattern[0:4]
px= 1
py= 1
bx=2
by=2
while True:
    for y in range (4):
        for x in range(4):
            if x== px and y== py:
                print ("P  ", end="")
            elif  x==bx and y==by:
                print ("B  ", end="")
            elif x==1 and y==3:
                print ("G  ", end="")
            else:
                print ("-  ", end="")

        print()

    move = input("Your move W/A/S/D? ").upper()
    nextpx=px
    nextpy=py
    dx=0
    dx=1

    if move=="W":
        dy=-1
    elif move=="A":
        dx=-1
    elif move=="S":
        dy=1
    elif move=="D":
        dx=1

    nextpx+=dx
    nextpy+=dy

    if 0<nextpx<4:
        px= nextpx
    if 0<nextpy<4:
        py=nextpy

    if nextpx==bx and nextpy=by:
        bx=dx
        by=dy
