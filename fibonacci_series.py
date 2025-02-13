n_terms = int(input("Enter the number of terms: "))

firstnum = 0
secondnum = 1

for i in range(n_terms):
    print(firstnum, end=" ")
    firstnum, secondnum = secondnum, firstnum + secondnum