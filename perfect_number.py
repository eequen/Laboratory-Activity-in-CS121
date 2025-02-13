num_enter = int(input("Enter a number: "))

divisors_sum = 0

for i in range(1, num_enter):
    if num_enter % i == 0:
        divisors_sum += i
        
if divisors_sum == num_enter:
    print(f"{num_enter} is a perfect number.")
    
else:
    print(f"{num_enter} is not a perfect number.")