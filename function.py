# def func(name):
#     print(f"hellow {name} how you doing..... ")

# func("sahil")

# args , to put multiple parameter in the function call  
# def hey(*name):
#     print("youngest child "+name[2])


# hey("rizu","sachin","aashish")

# def sqr():
#     num=int(input("Enter the value"))
#     print(f"the square of your given num is {num*num}")

# sqr()

# def sqr(ls):
#     temp_ls=[]
#     for i in ls:
#         temp_ls.append(i**2)
#         return temp_ls
    
# op = sqr([1,2,3,4,5])
# print(op)

# def avg(c,d):
#     print((c+d)/2)
# a=int(input("enter the first value"))
# b=int(input("enter the first value"))
# avg(a,b)

# def min(ls):
#     # putting first index varaible in min_ls 
#     min_ls=ls[0]
#     for i in range(1,len(ls)):
#         # is index variable of ls is less than min_ls  
#         if ls[i]<min_ls:
#         # then ls[i]==min_ls            
#          min_ls=ls[i]
#     print(f"min element is {min_ls}")
# lst=[0.36,1,5,7,9,2,6]
# min(lst)

# lamda function

# x=lambda a: a*10
# x=lambda a,b,c: a+b*c

# print(x(2,3,4))

def func(n):
    return lambda a:a*n

double = func(5)
print(double(11))