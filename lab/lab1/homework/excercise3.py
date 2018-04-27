import matplotlib
matplotlib.use ("TkAgg")

from matplotlib import pyplot

from pymongo import MongoClient

url="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(url)

db=client.get_default_database()

customer =db["customers"]

allcustomer = customer.find()
reflist = []
for eachcustomer in allcustomer:
    customerref = eachcustomer.get("ref")
    reflist.append (customerref)
ref_count =[]

ref_count = [reflist.count('events'), reflist.count('ads'), reflist.count('wom')]

ref_type = ["events", "ads", "wom"]

pyplot.pie (ref_count, labels = ref_type, autopct="%.1f%%", shadow=True, explode=[0.1, 0.2 ,0])
pyplot.axis ("equal")
pyplot.title ("reference comparision")

pyplot.show()
