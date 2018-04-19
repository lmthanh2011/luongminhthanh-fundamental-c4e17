#4b1
# patterns = []
# for i in range (20):
#     if i % 2 == 1:
#         patterns.append(0)
#     else:
#         patterns.append(1)
# print (*patterns)

#4b2
patterns = []
n = int(input("Enter the total number of 1's and 0's: "))
for i in range (n):
    if i % 2 == 1:
        patterns.append(0)
    else:
        patterns.append(1)
print (*patterns)
