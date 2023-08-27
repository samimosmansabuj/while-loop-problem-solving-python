# Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.

first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))
sum_even_number = 0

if first_num<second_num:
    while first_num<second_num:
        if first_num%2==0:
            print(first_num)
            sum_even_number+=first_num
        first_num+=1
    print(f"Sum of all even number: ",sum_even_number)
else:
    while second_num<first_num:
        if second_num%2==0:
            print(second_num)
            sum_even_number+=second_num
        second_num+=1
    print(f"Sum of all even number: ",sum_even_number)
