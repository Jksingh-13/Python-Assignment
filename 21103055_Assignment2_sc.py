#Ans 1
N = input("Enter the string")
#1a
print("The length of string is ",len(N))
#1b
print("The reversed string is ",N[::-1])
#1c
N1= N[10:26:]
print("The sliced string is ",N1)
#1d
N2=N[:10:]+"object oriented",N[26::]
print("The replaced string is ",N2)
#1e
x=N.index("a")
print("The index of substring A is ",x)
#1f
N3=N.replace(" ","")
print("The original string after removing whitespaces is ",N3)
print()


#Ans 2
Name="Jaskeerat Singh"
Sid=21103055
Department="CSE"
CGPA=9.8
print("Hey, %s Here!"%Name)
print("My SID is %d"%Sid)
print("I am from %s department and my CGPA is %.2f"%(Department,CGPA))
print()

#Ans 3
a=56 
b=10
print("a&b= " ,a&b)
print("a|b= " ,a|b)
print("a^b= " ,a^b)
print("Left shift both a and b with 2 bits respectively are :",a<<2 , b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are : " ,a>>2 , b>>4)
print()

#Ans 4
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
arr=[a,b,c]
arr.sort()
print(arr[-1])
print()

#Ans 5
string=input("Enter a string")
res=False
for i in range(len(string)):
	if string[i]=="n":
		if string[i:i+4]=="name":
			print("yes")
			res=True
if not res:
	print("no")
print()

#Ans 6
length1=input("Enter first side of triangle")
length2=input("Enter second side of triangle")
length3=input("Enter third side of triangle")
length1,length2,length3=int(length1),int(length2),int(length3)
if length1+length2<length3:
	print("NO")
elif length2+length3<length1:
	print("NO")
elif length1+length3<length2:
	print("NO")
else:
	print("YES")
