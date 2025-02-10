# 1.1
for i in range(3):
    print("Ishtpreet Singh")

#2.1
a = 10
b = 20
c = 30
sum = a + b + c
print(f"Sum of three numbers if {c}")

# 2.2
print("\nIshtpreet" + " Singh " + "Ahuja")

# 4.1
print("\nTable of 7")
for i in range(10):
    print(f"7 X {i} = {7*i}")

print("\nTable of 9")
for i in range(10):
    print(f"9 X {i} = {9*i}")
    
# 4.2
table = int(input("Enter the number you want a table of: "))
print(f"\nTable of {table}")
for i in range(10):
    print(f"{table} X {i} = {table*i}")

# 4.3
sum = int(input("\nEnter number 'n' to get sum of all digits till 'n': "))
ans = sum([i for i in range(sum)])
print(f"Sum of numbers upto {sum} is {ans}")
    
# 5.1
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print(f"\nMax number out the three numbers from input is {max(x, y, z)}")

# 5.2
divisible = int(input("Enter number upto which you want sum of numbers divisible by 7 and 9"))
sum2 = sum([i for i in range(divisible) if i % 7 == 0 and i % 9 == 0])
print(f"\nSum of all number divisible by 7 and 9 between 1 and {divisible}: {sum2}")

# 5.3
def isPrime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num**0.5, 1):
        if num % i == 0:
            return False
    return True

prime = int(input("Enter a number to find prime numbers upto it: "))
answer = [i for i in range(prime) if isPrime(i)]
print(f"\nPrime numbers upto {prime} are {answer}")

# 6.1
n = int(input("Enter number upto which you want sum of all odd numbers: "))
sum_odd = sum([i for i in range(n) if i % 2 != 0])
print(f"\nSum of all odd numbers between 1 and {n}: {sum_odd}")

# 6.2
primesum = int(input("Enter a number to find the sum of prime numbers upto it: "))
answersum = sum([i for i in range(prime) if isPrime(i)])
print(f"\nSum of prime numbers upto {primesum} are {answersum}")
