n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i)

#section B 2nd 
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#section B 3rd
n = int(input("Enter N: "))

sum = 0
for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

#section B 4th
num = int(input("Enter a number: "))
count = 0

while num != 0:
    count += 1
    num //= 10

print("Number of digits:", count)
