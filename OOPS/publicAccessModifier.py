class First:
    name="rizwan"
    _sirname="ali"
    _age_=22
    __college__="LIET"           #magic variable
    __DOB="14th Feb 1998"        #private variable in class 

class Second(First):
    def one(self):
        print("hello")
    
s=Second()
print(s.name)
print(s._age_)
print(s.__college__) 
print(s._sirname) 
# print(s._First__DOB)   if we wanna call the private data variable using inheritance then 
# we can call that object with the class where we defined that private variable 
print(s.one())