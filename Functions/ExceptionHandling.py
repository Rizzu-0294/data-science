# try:

#     result=
# except  ZeroDivisionError as e:
#     print(f"can't divide any value to zero{0}")
# else:
#     print("no exception occur")
# finally:
#     print("this will always executes")

# try:
#     a=int(input("enter the first num "))
#     b=int(input("enter the second num "))
#     result=a+b
#     print(result)
# except ValueError as v:
#     print(f"different data type can't be add {v}")
# except TypeError as d:
#     print(f"can't sum the integer and float {d} ")
# else:
#     print("addition successful")
# finally:
#     print("integer will always sum with integer")


# try:
#     a=int(input("enter the value of a = "))
#     if a>0:
#         print(f"positive integer")
#     else:
#         print("the value is not positive ")
# except ValueError as e:
#     print(f"invalid input {e} ",end=" ")
# else:
#     print("here we go")
# finally:
#     print("hope you get that ....!")