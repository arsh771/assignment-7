#Q1
dict1={}
x=int(input("Enter number of items: "))
for x in range(n):
    key=input("Enter key ")
    value=input("Enter value ")
    dict1[key]=value
print(dict1)
val=input("Enter value to find")
for y,z in dict1.items():
    if(z==val):
        print("Key of value",val,"is",y)

#Q2
a={}
n=int(input("Enter number of items: "))
for x in range(n):
    name=input("Enter name ")
    b={}
    marks1=int(input("Enter marks in C "))
    marks2=int(input("Enter marks in C++ "))
    marks3=int(input("Enter marks in Python "))
    b['C']=marks1
    b['C++']=marks2
    b['Python']=marks3
    a[name]=b
print(a)
s=input("Enter name of student :")
print(a[s])
