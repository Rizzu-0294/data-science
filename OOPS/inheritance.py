class First:
    name="Sachin"
    age=48
    address="बहादुरपुर,अलवर"

    def __init__(self):
        print(self.name)
        print(self.age)
        print(self.address)
    
class Second(First):
     def show(self):
         print()
         


s=Second()
s.show()
# print(s.__age__)


# f=First()
