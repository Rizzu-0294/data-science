Dict={"name":"rizwan",
      "class":"CSE",
      "age":23,
      "college":"LIET",
      "college":"LIET",
      "value":45.5,
      "graduated":True,
      "list":[1,5,"hey boy"],
      "Set":(1,5,6,"hey "),
      "tuple":{True,False,45}
}
# print(dict)
# print(type(dict))
# print(dict["age"])
# print(dict.__len__())
# # print(dict["list"][0])
# # dict["graduated"]=False
# print(dict,end="")

# dictionary constructor 
# d= dict(naam="sachin",address="bhiwadi")
# print(d)
# print(type(d))

# built function with dictionary
# print(Dict.items())
# print(Dict.pop('age'))
# print(Dict)
# print(Dict.get("name"))
# print(Dict.keys())
# print(Dict.popitem())
# # print(Dict.update())


# nested Dictionary
# dt={
#     "dt1":{"name":"rizu","class":"higher"},
#     "dt2":{"hell":"heaven","Day":"Monday"},

# }
# print(dt["dt1"]["name"])

# def hello():
#     return "hey how you doin ? buddy!"
# dt={
#     "hello":hello()
# }
# print(dt["hello"])

# single line ifelse 
a=5
b=25
# print("a")if a>b else print("b")

# single line shorthand ifelse
# print("a") if a>b else print("equal") if a==b else print("b")

# if a>b & b<a:
#     print("both are correct ")
# else:
#     print("both are wrong")

# x=41
# if x>10:
#     pass
#     print("above ten")
#     if x>20:
#         print("above 20")
#     else:
        
#         print("but not above 20")



# taking input in python 
# c=int(input("Enter the value of a"))
# d=int(input("Enter the value of b"))
# x=c+d
# print("the sum of your given value is ",x)

# print(a+b)

# x=input("enter the character")
# if x=="a"| x=="e"| x=="i"| x=="o" | x=="u":
# # if x=='a'or'e'or'i'or'o'or'u':
#     print("the is vowel ")
# else:
#     print("this is consonant")


# num=20
# for i in range(num):
#     if (i%2==0):
#         continue
#     else:
#         print(i,end=" ")

# for i in range(1,9):
#     print(i)

# x=int(input("enter the value you wanna get table of"))
# for i in range(1,11):
#     # print(x,"x",i,"=",x*i)
#     print(f"{x}*{i}=",x*i)


# using enumerate we can get the value with the indexing 
fruits=["apple","banana","mango"]
for i ,f in enumerate(fruits):
    print(i,f)