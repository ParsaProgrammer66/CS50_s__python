students = [
    {"name":"Hermione","House":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","House":"Gryffindor","patronus":"stag"},
    {"name":"Ron","House":"Gryffindor","patronus":"jack Russell terrier"},
    {"name":"Draco","House":"Slytherin","patronus":None}
]

for student in students:
    print(student["name"],student["House"],sep=" , ")

