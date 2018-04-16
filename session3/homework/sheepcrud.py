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
