#3>CONDITIONS [if,else]

#1. check whether a no.is even or odd.
a=int(input("Enter a no.:"))
if (a%2==0):
    print("The no. is even",a)
else:
    print("The no. is odd",a)
#2.ask the user for age and check if they can vote.
a=int(input("Enter your age:"))
if (a>=18):
    print("Congratulations!!, YOU ARE ELIGIBLE TO VOTE.",a)
else:
    print("Sorry, YOU ARE NOT ELIGIBLE TO VOTE.",a)
  #in other wayy....
a=int(input("Enter your age:"))

if (a>=18):
    eligibility="Your are eligible to vote."
else:
    eligibility="You are not eligible to vote."
print(eligibility)
#3. check whether a no. is positive ,negative or zero.
a=int(input("ENter a no.:"))
if (a>0):
    num="a is positive."
elif (a<0):
    num="a is negative."
else:
    num="a is zero."
print(num)
#4. WAP to check if a no. is divisible by 5 and 11.
a=int(input("Enter a no.:"))
if (a%5==0 and a%11==0):
    num="No. is divisible by 5 and 11."
else:
    num="No. is not divisible by 5 and 11."
print(num)
#5. create a simple grade system. 
 #90+--->A
 #80-89--->b
 #70-79--->c
 #<70--->fail
a=int(input("Enter your mark:"))
if (a>=90):
    mark=" CONGRATS!!, YOUR GRADE IS A++."
elif (a>=80 and a<=89):
    mark="YOUR GRADE IS B."
elif (a>=70 and a<=79):
    mark="YOUR GRADE IS C."
else:
    mark="RESULT: FAIL!! , BETTER LUCK NEXT TIME."
print(mark)

#4.LOOPS
#1. PRINT THE NUMBERS FROM 1 TO 10.
for i in range(1,11):
    print(i)
  #in another wayy...
for i in range(1,11):
    print(i,end=" ")
  #PRINT THE NO.S FROM 1,10 IN REVERSE ORDER.
for i in range(10,0,-1):
    print(i)
  #MULTIPLICATION TABLE USING LOOPS.
a=int(input("Enter a no. for its multiplication table:"))
for i in range(1,11):
    print(a,"x",i,"=",a*i)
  #DRAW A STAR PATTERN USING LOOPS.[For Right triangle]
for i in range(1,6):
    print("*"* i)
#For reverse triangle...
for i in range(6,0,-1):
    print("*" *i)
  #For pyramid...
for i in range(1,6):
    print(" " * (5-i) + "*" * (2*i-1))
#2. Print even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)
  #in another way...
for i in range(2,21):
    if i%2==0:
        print(i)
  #print numbers from 5 to 15.
for i in range(5,16):
    print(i)
  #print all odd numbrs from 1 to 30.
for i in range(1,31,2):
    print(i)
    #in another wayy..
for i in range(1,31):
    if i%2!=0:
        print(i)
  #print multiplies of 3 from 3 to 30.
for i in range(3,31,3):
    print(i)
  #print all numbers from 1 to 20 expect multiples of 4.
for i in range(1,21):
    if i%4!=0:
        print(i)
    #to print the o/p in one line..
for i in range(1,21):
    if i %4!=0:
        print(i,end=" ")
  #Find the sum of even numbers from 1 to 50.
sum=0
for i in range(2,51,2):
    if (i % 2==0):
        print("The sum of even no.s from 1 to 51 is :",sum)