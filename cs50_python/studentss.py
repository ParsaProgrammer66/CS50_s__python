import csv

name = input("what is your name? ")
home = input("where is your home? ")

with open("students.csv","a") as file:
    writer=csv.writer(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})

