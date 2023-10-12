class vault:
    def __init__(self,galleons=0,stickels=0,knuts=0):
        self.galleons = galleons
        self.stickels = stickels
        self.knuts=knuts
    def __str__(self):
        return f"{self.galleons}Galleons,{self.stickels}Sickles,{self.knuts}knuts"
    def __add__(self,other):
        galleons = self.galleons + other.galleons
        stickles = self.stickels + other.stickels
        knuts = self.knuts + other.knuts
        return vault(galleons,stickles,knuts)


potter = vault(100,50,25)
print(potter)

weasley = vault(25,50,100)
print(weasley)
galleons=potter.galleons + weasley.galleons
stickles=potter.stickels + weasley.stickels
knuts = potter.knuts + weasley.knuts

total = potter + weasley
print(total)