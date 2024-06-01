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

f=open("a.txt","a")
f.append("how did you do that...")
f.close()
f=open("a.txt","r")
print(f.read())
# # iteration on a.txt using loop 
# for i in f:
#     print(i,end=" ")
