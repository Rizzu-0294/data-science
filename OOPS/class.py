class Student:
    
    name="sahil"
    age=24
    address="Alwar"
    
    # default constructor 
    
    # parameteryzed constructor 
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

        print(f"the name is {name}")
        print(f"the name is {age}")
        print(f"the name is {address}")
        
    def show(self):
        # self keyword is used to refer the object to this particular method 
        print(self.name)
        print(self.age)
        print(self.address)

stu=Student("rizu",23,"bhiwadi")
# stu.show()
# stu.name="rizu"
# print(stu.name)

