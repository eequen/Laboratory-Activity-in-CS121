num = (input("Enter a number: "))

reversed_num = num[::-1]

if reversed_num == num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")