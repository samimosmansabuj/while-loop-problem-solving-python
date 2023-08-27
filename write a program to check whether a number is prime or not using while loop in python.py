#write a program to check whether a number is prime or not using while loop in python
num = int(input("Enter a number: "))
diveded_num = 2
verifynumber = 0
while diveded_num<num:
    if num%diveded_num == 0:
        verifynumber+=1
    diveded_num+=1
if verifynumber==0:
    print("This is prime number")
else:
    print("This is not a prime number")
