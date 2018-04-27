from pymongo import MongoClient


#1 connect database

url="mongodb://lmthanh2011:minhngoc@ds253959.mlab.com:53959/c4e17"
client = MongoClient(url)



#2 get default database
db=client.get_default_database()


#3 Get blog collection
blog = db["blog"]

#4 Write a new blog
post = {
    'title': "hoom nay toi buon",
    'content': "toi van o nha code"
}
# blog.insert_one(post)
all_posts=blog.find()
for post in all_posts:
    print(post)
