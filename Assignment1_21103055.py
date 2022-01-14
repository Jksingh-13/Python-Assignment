
# Name= Jaskeerat, SID= 21103055
#1
a = int(input())
b = int(input())
c = int(input())

avg = (a+b+c)/3
print(avg)
######################################
#2
gi= int(input())
nd = int(input())
taxable_income= gi - 10000 -(3000*nd)
tax = taxable_income*0.2
print(tax)
############################
#3
SID = int(input())
Name= input()
Gender= input()
Course_name= input()
cgpa= float(input())
Student=[SID, Name, Gender, Course_name, cgpa]
print(Student)

###################
#4
a=int(input("marks of 1st student"))
b=int(input("marks of 2nd student"))
c=int(input("marks of 3rd student"))
d=int(input("marks of 4th student"))
e=int(input("marks of 5th student"))
marks=[a,b,c,d,e]
marks.sort()
print(marks)
##############
#5a
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)
#5b
color[3]= 'Purple'
print(color)

