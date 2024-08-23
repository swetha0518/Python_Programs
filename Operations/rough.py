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

import json
print(studentDict)
print(len(studentDict))
print(student3.get("name"))
print(student2.get("roll no"))
print(student1.get("class"))
#print("Sports Students of class 10 \n", json.loads(str(studentDict)))
print("Sports Students of class 10", studentDict)
print(json.dumps(studentDict))

# Write Python3 code here

import json

json_data = '[{"Employee ID":1,"Name":"Abhishek","Designation":"Software Engineer"},' \
			'{"Employee ID":2,"Name":"Garima","Designation":"Email Marketing Specialist"}]'

json_object = json.loads(json_data)

# Indent keyword while dumping the data decides to what level spaces the user wants.
print(json.dumps(json_object, indent = 1))

# Difference in the spaces
# near the brackets can be seen
print(json.dumps(json_object, indent = 3))
