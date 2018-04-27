from getpass import getpass
while True:
    username = getpass ("username ")
    password = getpass ("password ")
    #cach1
    if username == "c4e":
        if password == "ctc":
            print ("Welcome")
        else:
             print ('fail')
    else:
         print ('fail')
    #cach 2
    if username != "c4e":
        print ("no such user")
    else:
        #valid username
        if password != "codethechange":
            print ("wrong password")
        else:
            print("welcome, c4e")
            break
