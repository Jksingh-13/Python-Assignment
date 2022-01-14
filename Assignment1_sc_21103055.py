
# Name= Jaskeerat, SID= 21103055
#1
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
avg = (a+b+c)/3
print("Average of the three numbers is :"avg)


#2
gi= int(input("enter your gross income:"))
nd = int(input("Enter your number of dependents:"))
taxable_income= gi - 10000 -(3000*nd)
tax = taxable_income*0.2
print("Your income tax is :"tax)


#3
SID = int(input("Enter your SID:"))
Name= input("Enter your name:")
Gender= input("Enter your Gender:")
Course_name= input("Enter your course name:")
cgpa= float(input("Enter your CGPA:"))
Student=[SID, Name, Gender, Course_name, cgpa]
print(Student)


#4
a=int(input("Enter marks of students:"))
b=int(input("Enter marks of students:"))
c=int(input("Enter marks of students:"))
d=int(input("Enter marks of students:"))
e=int(input("Enter marks of students:"))
marks=[a,b,c,d,e]
marks.sort()
print(marks)



#5a
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("Part a question :"color)


#5b


color[3]= 'Purple'
print("Part b of question :"color)