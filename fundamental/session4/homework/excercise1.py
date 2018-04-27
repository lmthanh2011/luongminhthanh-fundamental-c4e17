numbers = [1,6,8,1,2,1,5,6]
i = int(input('Enter a number? '))

# #dungcount
# n = numbers.count(i)
# message = "{0} appears {1} time in my list".format(i,n)
# print (message)

#khongdungcount
solan= 0
for n in range(len(numbers)):
    if numbers[n]==i:
        solan = solan +1
message = "{0} appears {1} time in my list".format(i,solan)
print (message)
