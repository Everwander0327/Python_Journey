person1 = {"Name":"Neko", "Age":22}
person2 = dict(Name="Forger", Age=21)

print(person1.get("Name"))
print(person2.get("Age"))
person1["gender"] = "Male"

print(person1)

person1.update({"Name": "John","age":23})

print(person1)

