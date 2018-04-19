#
#
# while True:
#     username = input ("username?")
#     password = input ("password?")
#
#     if username != "c4e":
#         print ("no such user")
#     elif password != "codethechange":
#         print ("wrong password")
#     else:
#         print ("Welcome")
#         break


n=0
while n<3:
    username = input ("username?")
    password = input ("password?")

    if username != "c4e":
        print ("no such user")
        n+=1
        print ("chi con", str(3-n), "lan")
    elif password != "codethechange":
        print ("wrong password")
        n+1
        print ("chi con", str(3-n), "lan")
        
    else:
        print ("Welcome")
        n+=3
