#1>
#1.[BASIC(PRINT,VARIABLES,INPUT)]

print("HELLO, I am learning python.")
#2. create a variable for your name,age,and college and print them.
name="Lipun\n"
age="21\n"
college="Jaya jagannath degree college"
print(name,age,college)
#3. ask the user to enter their name and print
name=input("Enter your name:")
print("HOLAA !!:",name)
#4. ask the user to enter two no.s and print their sum.
a=int(input("Enter the 1st no.:"))
b=int(input("Enter the 2nd no.:"))
sum=a + b
print(sum)
# using float variable in the above program.
a=float(input("Enter the 1st no.:"))
b=float(input("Enter the 2nd no.:"))
sum=a+b
print(sum)
# ask the user to enter two no.s and print their subtraction,multiplication,division,modular.
a=float(input("Enter the 1st no.:"))
b=float(input("Enter the 2nd no.:"))
sub=a-b
mul=a*b
div=a/b
mod=a%b
print(sub,"\n",mul,"\n",div,"\n",mod)
#5. ask the user for length ad width and print the area of the rectangle.
l=int(input("ENter the length of the rectangle:"))
b=int(input("Enter the width of the rectangle:"))
a=l*b
print(a)

#2[BASIC LOGIC(operators,calculations)]

#1. WAP to swap two numbers using third variable.
a=int(input("Enter the 1st no. a ="))
b=int(input("Enter the 2nd no. b ="))
print("Before swapping the 2 no.s \n a =",a,"\n b =",b)
c=a+b
a=c-a
b=c-b
print("After swapping of these two no.s are \n a =",a,"\n b =",b)

# swapping without using any third variable.
a=int(input("Enter the 1st no. a ="))
b=int(input("Enter the 2nd no. b ="))
print("Before swapping the 2 no.s \n a =",a,"\n b =",b)
b=a-b
a=a-b
b=a+b
print("After swpping the 2 no.s w/o using 3rd variable is \n a =",a,"\n b =",b)

#2. ask the user for a no. and print its square and cube.

A=int(input("Enter a no.:"))
squ=A*A
cube=A*A*A
print("The square of the no. is :",squ,"\n The cube of the no. is :",cube)

#3. converting celcius to fahrenheit

celsius=float(input("Enter temperature in celcius :"))
fahrenheit=(celsius * 9/5)+32
print(celsius,"°c=",fahrenheit,"°f")

#4. Ask the user to enter 3 no.s and print the largest no. among them.

a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
c=int(input("Enter 3rd no."))
if a>=b and a>=c:
   print("largest = a")
elif b>=a and b>=c:
    print("largest = b")
else:
    print("largest = c")

# in another way...
a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
c=int(input("Enter 3rd no."))
if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
print("The larget no. among these 3 no.s is :",largest)

#5. WAP to calculte the average of 5 no.s

a=int(input("Enter the 1st no.:"))
b=int(input("Enter the 2nd no.:"))
c=int(input("Enter the 3rd no.:"))
d=int(input("Enter the 4th no.:"))
e=int(input("Enter the 5th no.:"))
sum=a+b+c+d+e
avg=sum/5
print("The average of the 5 no.s is =",avg)