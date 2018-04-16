items = ["T-shirt", "Sweater"]
order = input ("Welcome to our shop, what do you want (C, R, U, D)?")
if order == ('R'):
    print ("Our items:", ", ".join(items))
elif order == ("C"):
    newitem = input ("Enter new item:")
    items.append (newitem)
    print ("Our items:", ", ".join(items))
elif order == ("U"):
    i = int (input ("Update position?"))
    newitem = input ("New item?")
    items.insert (i,newitem)
    print ("Our items:", ", ".join(items))
elif order == ("D"):
        i = int(input ("Delete position?"))
        items.pop (i)
        print ("Our items:", ", ".join(items))
else:
    print ("Wrong order")
