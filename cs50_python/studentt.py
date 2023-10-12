import sys
class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
        self.patronus=patronus
    def __str__(self):
        return f"{self.name} from {self.house}"
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house=house

    def charm(self):
        match self.patronus:
            case"stag":
                return"Pizza"
            case"Otter":
                return"monkey"
            case"jack Russell terrier":
                return"/"
            case _:
                return"|"
def main():
    student = get_students()
    print("Expecto Patronum!")
    student._house="Number Four, Privet "
    print(student.charm())
    print(student)

def get_students():
    name = input("Name: ")
    house = input("House: ")
    patronus=input("Patronus: ")
    student = Student(name,house,patronus)
    return student

if __name__ =="__main__":
    main()