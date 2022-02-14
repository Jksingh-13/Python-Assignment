#Ques1

string1=input("Give a string-")
list1=[]
list2=string1.split()
y=len(list2)
d=dict()
t=dict()
if len(list2)==1:          
    for i in string1:      
        list1.append(i) 
    for j in list1:        
        if j in d:         
            d[j]=d[j]+1    
        else:
            d[j]=1
    print(d)        

else:
    for i in list2:        
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t)

#QUES--> 2
def leap_year(year):
    if year%400==0 and year%100==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False
Day= int(input("Give month-"))
Month= int(input("Give day-"))
Year= int(input("Give year-"))
if Month in [1,3,5,7,8,10,12]:
    if Day<31:
        print(Day+1,"/",Month,"/",Year)
    else:
        if Month==12:
            print("1/1/",Year+1)
        else:
            print("1/",Month+1,"/",Year)
elif Month in [4,6,9,11]:
    if Day<30:
        print(Day+1,"/",Month,"/",Year)
    else:
        print("1/",Month+1,"/",Year)
else:
    if leap_year(Year):
        if Day<29:
            print(Day+1,"/",Month,"/",Year)
        else:
            print("1 / 3 /",Year)
    else:
        if Day<28:
            print(Day+1,"/",Month,"/",Year)
        else:
            print("1 / 3 /",Year)
#QUES--> 3
List=[int(x) for x in input().split()]
output=[]
for i in range(len(List)):
    output.append((List[i],List[i]**2))
print(output)

#QUES--> 4
A=[["A+","Outstanding"],["A","Excellent"],["B+","Very Good"],["B","Good"],["C+","Average"],["C","Below Average"],["D","Poor"]]
grade=int(input("Give a number between 4 and 10 including them-"))
index=10-grade
print("Your grade is %s and %s Performance"%( (A[index])[0], (A[index])[1]  ))

#QUES--> 5
n=int(input()) # total number of rows
for row in range(n):
    spaces=" "*row #spaces before the pattern for every row 
    print(spaces,end="")
    for j in range( (2*n) - 1 - (2*row) ):
        print(chr(65+j),end="") #as chr(65)="A" and chr(66)="B" and so on.
    print() #for bringing pointer to next line

#QUES--> 6
student_info=dict()
n="y"
alistsid=[]

#(a)
print("----------------(a)-------------------")
while(n=="y"):
    sid=int(input("Give the sid (a number):"))
    name=input("Enter your name:")
    student_info[sid]=name
    n=input("give a letter y or n:")
    alistsid.append((sid,name))
print("The required dictionary--",student_info)
print("The list will be used in further parts--")
print("The required list--",alistsid)


#(b)
print("----------------(b)------------------------")
print("The dictionary we had-")
print(student_info)

newdict=dict()
alistname=[]

for (k,v) in student_info.items():
    newdict[v]=k
    alistname.append((v,k))
print("now we have exchanged the key value pair but its not sorted-")

print(newdict)
print("The unsorted list--")
print(alistname)
alistname.sort()

print("The sorted list--")
print(alistname)

print("The sorted dictionary-")
sorted_dict=dict(alistname)
print(sorted_dict)


required_dict_name=dict()
for (k,v) in sorted_dict.items():
    required_dict_name[v]=k
print("This is the dictionary sorted on the basis of name-")
print(required_dict_name)


#(c)
print("-----------------(c)-----------------")
print("The list we made before will be used now-")
print(alistsid)
alistsid.sort()
print("now the list is sorted-")
print(alistsid)
sorted_student_info_sid=dict(alistsid)
print("sorted dictionary based on sid-",sorted_student_info_sid)


#(d)
print("-----------------(d)-----------------")    
entered_sid=int(input("Please enter one of the sids you entered before-"))
print("The name of the student with the entered sid is-")    
print(student_info[entered_sid])

#QUES--> 7
def Fibonacci_series(n):
    if n==0 or n==1:
        return 1
    else:
        return Fibonacci_series(n-1)+Fibonacci_series(n-2)
N=int(input())
sum_of_numbers=0
for i in range(N):
    ith_term=Fibonacci_series(i)
    print(ith_term,end=" ")
    sum_of_numbers+=ith_term
print()
average=sum_of_numbers/N
print(average)

#Ques 8

Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#(a)
print("-------------(a)------------")
required_Set=Set1^Set2
print(required_Set)

#(b)
print("-------------(b)------------")
required_Set=Set1^(Set2^Set3)
print(required_Set)


#(c)
print("-------------(c)------------")
required_Set=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(required_Set)


#(d)
print("-------------(d)------------")
new_Set={1,2,3,4,5,6,7,8,9,10}
required_Set=new_Set-Set1
print(required_Set)


#(e)
print("-------------(e)------------")
required_Set=new_Set-(Set1|Set2|Set3)
print(required_Set)