# menu = ['pho', 'com rang', 'my xao', 'bun rieu']
# print (menu)
# #create
# menu.append('hu tiu')
# print (menu)
#
# print (menu[1])
#
# #fori
# for i in range (len(menu)):
#     print (menu[i], end=", ")
#
# #foreach
# for item in menu:
#     print ((item), end=", ")
#
# #for emum
# for i, item in enumerate(menu):
#     message = "{0}.{1}".format(i+1,item)
#     print (i+1, item)

name = "nguyen"
age = 22
status = "single"
address = "doi can"

message = "{0}, {1} tuoi, tinh trang quan he: {2}, song o: {3}".format(name,age,status,address)
print (message)
print (name, str(age), status, address)
