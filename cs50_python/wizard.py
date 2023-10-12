class wizard:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        super().__init__(self,name,house)
        self.name=name
class student(wizard):
    def __init__(self,name,house):
        super().__init__(self,name,house)
        self.house=house

class professor(wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.object = subject

student = student("Harry","Gryffindor")
professor = professor("Severos","he was Slytherins teacher")
