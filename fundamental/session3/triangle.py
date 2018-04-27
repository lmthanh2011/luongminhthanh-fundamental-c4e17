m= int(input("Nhap m "))
n= int(input("Nhap n "))

for i in range (m):
    for j in range (n):
        if j<=i:
            print ("*", end="")
        else:
            print(" ", end="")
    print ()
