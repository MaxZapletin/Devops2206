a = "Max Zap"
b = 'Max Zap'
c = "max \"zap\""
d = "devops experts"
h = {"fname": "Max",
     "lname": "zap",
     "age": 33,
     "hobbies": ["sea"]}
i = ("max", "zap", 30, True)
print(i[2])
k[2] = 30
# e = b + d
print(b + " from " + d)
e = f"{h['fname']} {h['lname']} and hobbie is {h['hobbies']}"
print(e)
g = "%s %s" % (b, d)
print(b + str(k[2]))
print(" ".join(h["hobbies"]))



