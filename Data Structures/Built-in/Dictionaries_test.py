import json

##DICTIONARY
dict = {
  "name": "SWETHA",
  "age": 20,
  "year": 2003
}
print(dict)
print(dict["name"])
print(len(dict))

#ordered, changeable and unique keys
studentDict = {
  "name": "swetha",
  "email": "swetha@a.com",
  "Age": 19,
  "Age": 20
}
print(studentDict)

print(studentDict["name"])

print(studentDict.get("name"))

#get all keys
print("keys ",studentDict.keys())

#get all values
print(studentDict.values())

#get both keys and values
print("items ",studentDict)

# looping keys
for x in studentDict:
  print(x)

for x in studentDict.keys():
  print(x)

# values
for x in studentDict:
  print(studentDict[x])

for x in studentDict.values():
  print(x)

# items
for x, y in studentDict.items():
  print(x, y)

#check if key exists
if "email" in studentDict:
  print("email key found")

print(len(studentDict))


studentDict = {
  "name": "swetha",
  "email": "swetha@a.com",
  "Age": 20,
  "address": ["billing", "residential", "office"]
}
print(studentDict["address"][1])

print(type(studentDict))

#modification
studentDict["name"] = "shiny"
studentDict.update({"email": "shiny@s.com"})
print(studentDict)

studentDict.update({"phone": 12345})

#remove
studentDict.pop("name")
studentDict.popitem()
del studentDict["email"]
studentDict.clear()
del studentDict


#Nested
studentDict = {
  "student 1" : {
    "name" : "Tyler",
    "class" : 10,
    "roll no" : 38
  },
  "student 2" : {
    "name" : "Ryan",
    "class" : 11,
    "roll no" : 29
  },
  "student 3" : {
    "name" : "christyn",
    "class" : 12,
    "roll no": 6
  }
}

student1 = {
    "name" : "Tyler",
    "class" : 10,
    "roll no" : 38
  }

student2 = {
    "name" : "Ryan",
    "class" : 10,
    "roll no": 29
  }

student3 = {
    "name" : "Christyn",
    "class" : 10,
    "roll no": 6
  }

print(studentDict)
print(len(studentDict))
print(student3.get("name"))
print(student2.get("roll no"))
print(student1.get("class"))
#print("Sports Students of class 10 \n", json.loads(str(studentDict)))
print("Sports Students of class 10 \n", studentDict)