n_terms = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b