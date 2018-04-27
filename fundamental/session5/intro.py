person = {
  "name":"Quan",
  "age":40
  "home": "Hanoi",

}
# person["age"]=22
# print (person)
#
# if "home" in person:
#   print (person["home"])

#update
# # person ["age"]=22
# # print (person)
#
# #create
# person["home"]="Hanoi"
# print (person)
#
# #del
# del person["name"]

#check key
print (*person.keys())
print (*person.values())

for key, value in person.item():
    print (key, ":", value)
