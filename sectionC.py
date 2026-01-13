for i in range(1, 101):
    if i % 2 == 0:
        print(i)

#section c 2nd

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

#section C 3rd
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)