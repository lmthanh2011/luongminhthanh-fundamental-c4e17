patterns = []
# for i in range (10):
#     for j in range (10):
#         x=i+j
#         if x % 2 == 1:
#             patterns.append(0)
#         else:
#             patterns.append(1)
#     print (*patterns)
#     del patterns[0:10]

# #de bai in 10x10 ma hinh trong de bai co 9x9 thoi ban oi

n = int(input("Enter a number: "))
for i in range (n):
    for j in range (n):
        x=i+j
        if x % 2 == 1:
            patterns.append(0)
        else:
            patterns.append(1)
    print (*patterns)
    del patterns[0:n]
