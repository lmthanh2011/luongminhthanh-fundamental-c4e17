
from random import choice
print ("python word jumble.py")
#lay chu cai
text = "champion"
character = list(text)
#random chw cai
for i in range (len(character)):
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
