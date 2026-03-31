patient = {
    "name": "Maria",
    "age": 30,
    "address": "Bukidnon"
}

print("--- A. Patient Dictionary ---")
print("Name:", patient["name"])

patient["blood_type"] = "O+"
patient["age"] = 28
del patient["address"]

print("Updated patient:", patient)


students = {
    "s1": {"name": "Juan", "score": 85},
    "s2": {"name": "Ana",  "score": 90},
    "s3": {"name": "Leo",  "score": 88}
}

print("\n--- B. Students Dictionary ---")

for s in students.values():
    print("Name:", s["name"])

scores = [s["score"] for s in students.values()]
print("Average:", sum(scores) / len(scores))
print("Highest:", max(scores))


patients = {
    1: {"name": "Juan Dela Cruz", "age": 25, "barangay": "Poblacion"},
    2: {"name": "Ana Reyes",      "age": 30, "barangay": "Tunasan"},
    3: {"name": "Mark Santos",    "age": 28, "barangay": "Putatan"}
}

print("\n--- C. Clinic Record System ---")

for id, p in patients.items():
    print(f"{id} - {p['name']} - {p['age']} - {p['barangay']}")

patients[4] = {"name": "Maria Lopez", "age": 32, "barangay": "Alabang"}
print("Added:", patients[4])

patients[2].update({"age": 31, "barangay": "New Brgy"})
print("Updated ID 2:", patients[2])

print("\nEnter new patient:")
uid   = int(input("ID: "))
uname =     input("Name: ")
uage  = int(input("Age: "))
ubrgy =     input("Brgy: ")

patients[uid] = {"name": uname, "age": uage, "barangay": ubrgy}
print(f"\nNew Record: {uid} - {uname} - {uage} - {ubrgy}")