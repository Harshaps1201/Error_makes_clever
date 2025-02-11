a={"name":"harsha",
   "age":25,
   "location":"Tvpm",
   "students":["bala","john"]}
print(a)
print(a["name"])
print(a.keys())
print(a.values())
a["age"]=24
print(a)
a["color"]="red"
print(a)
a.update({"location":"India"})
print(a)
a.pop("age")
print(a)
del a["name"]
print(a)
a.clear()
print(a)
del a
print(a)