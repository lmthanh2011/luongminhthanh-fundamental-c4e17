
print ("""Guess your number game,
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number""")
n = 51
max = 100
min = 0
while True:
    print ("Is", n, "is your number", end="")
    nhap = input ()
    if nhap == ('l'):
        max = n
        n = int((min+max)/2)+1

    elif nhap == ('s'):
        min = n
        n= int((min+max)/2)+1
    else nhap == ('c'):
        print ('I knew it')
        break
