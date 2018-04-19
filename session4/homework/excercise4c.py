patterns = []
# 9x9
# for i in range (1,10):
#     for j in range (1,10):
#         x = i*j
#         patterns.append(x)
#     print (*patterns, end="\n")
#     del patterns[0:9]

#nhapn
n=int(input("Enter a number: "))
for i  in range (1,n+1):
    for j in range (1,n+1):
        x=i*j
        patterns.append(x)
    print (*patterns, end="\n")
    del patterns[0:n]
