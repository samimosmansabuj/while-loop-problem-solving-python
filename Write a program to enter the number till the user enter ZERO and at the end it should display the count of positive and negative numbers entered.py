# Write a program to enter the number till the user enter ZERO and at the end it should display the count of positive and negative numbers entered

sum_positive = 0
sum_negetive = 0
num = 1
while num!=0:
    num = int(input("Enter a Number: "))
    if num>0:
        sum_positive+=num
    elif num<0:
        sum_negetive+=num
    else:
        print("Wrong Input")

print("Sum of all positive number: ", sum_positive)
print("Sum of all Negetive number: ", sum_negetive)
