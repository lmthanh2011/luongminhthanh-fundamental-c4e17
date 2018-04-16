size = [5,7,300,90,24,50,75]
#create list
print ("Hello, my name is Thanh and these are my sheeps sizes", size)
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
#month_nhap_so_thang
for m in range (2):
    print ("Month", m+1)
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
print ("Month 3")
for i in size:
    i2=i+50
    size.insert(size.index(i),i2)
    size.remove (i)
print ("One month has passed, here is my flock", size, sep="\n")
totalsize = sum(size)
print ('My flock has size in total:', totalsize)
totalmoney = totalsize*2
print ("I would get ", totalsize," * 2$ = ", totalmoney, "$", sep='')
