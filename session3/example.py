#name1 = ('Canh')
#name2 = 'Hieu'
#name3 = "Duc Anh"
#name4 = "Nguyen"
#name5 = "Don"

#names = []
#print (names)
#print (type(names))

#names =["Canh"]
#print(names)

names = ["Canh", "Hieu", "Duc Anh"]
#print(names)
#create
#names.append("Nguyen")
#print (names)

#newname = "don"
#names.append(newname
#print(names)

#read
#print(names[-5])

#names[0]="canh dai ka"
#print (names)
# print (len(names))
# #len=length
#
# for i in range (len(names)): (3):
#     print(names[i])

#foreach

# for n in (names):
#     for i in range (len(names)):
#         print(i+1, n)
#
# for n in (names):
#     prints (names[n], n]

no = 1
for n in names:
    #print (no, ".", n, sep="")
    #string format
    message = "{0}. {1}". format(no, n)
    print (message)
    no = no+1 #no+=1
