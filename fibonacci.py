n1, n2 = 0, 1
count = 0
terms=int(input("Enter the number of terms:"))

while count < terms:
    print(n1,end="  ")
    n = n1 + n2
    n1 = n2
    n2 = n
    count += 1
