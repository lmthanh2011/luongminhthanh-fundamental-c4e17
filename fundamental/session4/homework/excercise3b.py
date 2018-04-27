from random import choice
#lay random tu list
listtext = ['melticulous',"champion","hexagon"]
for i in range (len(listtext)):
    print ("python word jumble.py")
    text = choice(listtext)
    listtext.remove(text)
    character = list(text)
#in chu cai ra
    for j in range (len(character)):
        random=choice(character)
        print (random, " ", end="")
        character.remove(random)
    print()
#nhap cau tra loi
    answer = input ("your answer: ")
    while answer != text:
        print (":(")
        answer = input ("your answer: ")
    else:
        print ("hura")
