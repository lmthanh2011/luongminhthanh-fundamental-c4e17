# # person = ["Quan", 40, "single", "hanoi", 2, 11]
# # #print (person)


# person = {}
# print (person)
#
# person ={
#     "name": "Quan"
# }
# print (person)


teencodedict ={
    "ns": "noi",
    "r": "roi",
    "pt": "party"
}
print (teencodedict.keys)
while True:
    #1
    code = input("Your code? ")
    if code in teencodedict:
        print (teencodedict[code])
    else:
        print ("not found")
        userchoice = input("Wish to contribute? (Y/N)? ").upper()
        if userchoice == Y:
            translation = input("Enter translation: ")
            teencodedict[code]= translation
            print (teencodedict)
