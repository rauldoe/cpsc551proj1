# clear;python3 chuck.py
# clear;python chuck.py

import Blog

blog = Blog.Blog()

# poster = "bob"
# topic = "distsys"
# t1 = blog._rd((poster, topic, str))
# print("reading poster: " + poster + ", topic: " + topic)
# print("got message: " + t1["output"][2])

poster = str
topic = "gtcn"
t2 = blog._rd_next((poster, topic, str))
print("reading" + " topic: " + topic)
print("got message: " + t2["output"][2] + " poster: " + t2["output"][0])

poster = str
topic = "distsys"
t2 = blog._rd_next((poster, topic, str))
print("reading" + " topic: " + topic)
print("got message: " + t2["output"][2] + " poster: " + t2["output"][0])

