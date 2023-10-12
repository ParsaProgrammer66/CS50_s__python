import random
class hat:
    def __init__(self):
        houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")

hat = hat()
hat.sort("Harry")