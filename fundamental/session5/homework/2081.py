
text = input("Enter your text: ")
character = list(text) #tach thanh chu cai

character.sort() #xep theo alphabetical order
from collections import Counter
alphabet = Counter(character)
for key, value in alphabet.items():
    print (key, ": ",value, sep="")
