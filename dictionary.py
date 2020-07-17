# create dictionary
# d={}
# d0=dict()
# print(type(d))
# print(type(d0))

# dictionaries
# d1={"k1":"v1", "k2":"v2", "k3":"v3"}
# d2={1:"v1", 2:"v2", 3:"v3"}
# d3={1:"v1", 2:"v2", 3:"v1"}
# d4={"k1":"v1", "k2":"v2", "k1":"v3", "k1":"v4"}
# print(d1)
# print(d2)
# print(d3)
# print(d4)

# accessing keys
# d1={"k1":"v1", "k2":"v2", "k3":"v3"}
# for k in d1.keys():
#     print("key:", k)
# accessing values
# for v in d1.values():# first approach
#     print("value:", v)
# for k in d1.keys():# second approach
#     print("value:", d1[k])
# accessing keys and values
# for key,value in d1.items():
#     print(f"key: {key}, value: {value}")

# students dictionary
students={
    "s1":{
        "name":"John",
        "age":28,
        "married":False,
        "pets":"cat",
        "children":("abc","def"),
        "cars": [{"model": "m11", "mpg": 10},
                {"model": "m12", "mpg": 16}],
        "marks":{"physics":70,"Maths":71,"chemistry":72}},
    "s2": {
        "name": "Mike",
        "age": 26,
        "married": True,
        "pets": None,
        "children": None,
        "cars": [{"model": "m21", "mpg": 12},
                 {"model": "m22", "mpg": 16}],
        "marks": {"physics": 97, "Maths": 84, "chemistry": 85}},
    "s3": {
        "name": "mac",
        "age": 27,
        "married": True,
        "pets": None,
        "children": None,
        "cars": [{"model": "m31", "mpg": 10},
                 {"model": "m32", "mpg": 13}],
        "marks": {"physics": 100, "Maths": 94, "chemistry": 95}},
}

#questions and implementation
# 1. names of married students
married_students=[]
for key,value in students.items():
    # print(f"key {key}, value {value}")
    for k1,v1 in value.items():
        if k1 == "married" and value[k1]:
            married_students.append(value["name"])
print(married_students)

# 2. names of students with no pets
students_with_no_pets=[]
for key,value in students.items():
    for k1,v1 in value.items():
        if k1 == "pets" and value[k1] is None:
            students_with_no_pets.append(value["name"])
print(students_with_no_pets)

# 3. model of cars with mpg>15
cars = []
for key,value in students.items():
    for k1,v1 in value.items():
        if k1 == "cars":
            for ele in v1:
                for k2, v2 in ele.items():
                    if k2=="mpg" and v2>15:
                        cars.append(ele["model"])
print(cars)
