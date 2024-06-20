# f=open("a.txt","r")
# print(f.read(10))
# print(f.readline())
# f.close()

# Write mode in file handling
# w=open("a.txt","w")
# w.write("something we all adore , one thing worth dying for , nothing but pain , stuck in this game , searching for fortune and fame")
# w.close()
# w=open("a.txt","r")
# print(w.read())

# f=open("a.txt","a")
# f.append("how did you do that...")
# f.close()
# f=open("a.txt","r")
# print(f.read())
# # # iteration on a.txt using loop 
# # for i in f:
# #     print(i,end=" ")


# append in file 
# f=open("a.txt","a")
# f.write(" hey")
# f.close()

# f=open("a.txt","r")
# print(f.read())

# x method to create a file if not exist 
try:
    a="one.txt"
    if a:
        f=open("one.txt","x")
        f.write("hellow sir")
        f.close()
        print("file is created ")
    else:
        print("file is already exist in the directory")
except Exception as e:
    print("duplicate should not be in the same directory, try it with other name ")
else:
    print("did it  ")
finally:
    print("done done done ")