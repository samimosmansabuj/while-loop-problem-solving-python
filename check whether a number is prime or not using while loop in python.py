# Write a program to check whether a number is prime or not using while loop in python

num = int(input("Enter a number: "))
verifyprimenumber = 0

if num==1 and num==0:
    print(f"{num} is not a prime number.")
else:
    devided_number = 2
    while devided_number<num:
        if num%devided_number==0:
            verifyprimenumber+=1
        devided_number+=1
        
    if verifyprimenumber==0:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    

