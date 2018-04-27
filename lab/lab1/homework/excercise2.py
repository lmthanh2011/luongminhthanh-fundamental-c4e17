from pymongo import MongoClient

url="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(url)

db=client.get_default_database()

posts = db["posts"]

postbyThanh = {
    'title': "hoom nay toi buon",
    'author': "anonymous",
    'content': "toi van o nha code"
}
posts.insert_one(postbyThanh)
all_posts=posts.find()
for post in all_posts:
    print(postbyThanh)
