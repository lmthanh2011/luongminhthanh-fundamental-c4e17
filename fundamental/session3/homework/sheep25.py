size = [5,7,300,90,24,50,75]
print ("Hello, my name is Thanh and these are my sheeps sizes", size)
#grow_n_months
months = int(input("months?"))
for m in range (months):
    print ("month", m+1)
    #grow
    for i in size:
        i2=i+50
        size.insert(size.index(i),i2)
        size.remove (i)
    print ("One month has passed, here is my flock", size, sep="\n")
    #choose the biggest
    max = size[0]
    for i in size:
        if i> max:
            max = i
    print ("Now my biggest sheeps has size", max, "let's shear it")
    #change size
    size.insert(size.index(max),8)
    size.remove (max)
    print ("After shearing, here is my flock", end="\n")
    print (size)
