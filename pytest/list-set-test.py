# Removing Duplicates on list by converting to set
list_students = ["Ana", "Ben", "Ana", "Carl", "Ben", "Dana"]
print(set(list_students))

#Find Common Students
math_class = {"Ana","Ben","Carl"}
science_class = {"Ben", "Carl", "Dana"}
common_students = math_class.intersection(science_class)
print(common_students)

#Find Students Only in One Class
math_class = {"Ana","Ben","Carl"}
science_class = {"Ben", "Carl", "Dana"}
student = math_class.difference(science_class)
print(student)

#Combine All Students
math_class = {"Ana","Ben","Carl"}
science_class = {"Ben", "Carl", "Dana"}
combine_class = math_class.union(science_class)
print(combine_class)



