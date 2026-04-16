# Sum of digits
n = 1234
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n //= 10
print("Sum of digits:", total)

# Armstrong number check
n = 123
original = n
total = 0
while n > 0:
    digit = n % 10
    total += digit ** 3
    n //= 10
if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")

# Palindrome check
n = 121
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
if rev == original:
    print("Palindrome")
else:
    print("Not Palindrome")

# Prime number check
n = 25
is_prime = True
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
if n < 0:
    print("Not prime")
elif is_prime:
    print("Prime")
else:
    print("Not prime")

# Count numbers greater than 5
arr = [2, 8, 1, 10, 3, 7]
count = 0
for num in arr:
    if num > 5:
        count += 1
print("Count > 5:", count)

# Find maximum in array
arr = [3, 7, 2, 9, 5]
max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num
print("Max value:", max_val)

# Count numbers greater than 10
arr = [5, 12, 17, 3, 9, 21]
count = 0
for num in arr:
    if num > 10:
        count += 1
print("Count > 10:", count)

# Print numbers divisible by 3 or 5
arr = [3, 5, 15, 20, 30, 7]
print("Divisible by 3 or 5:")
for num in arr:
    if num % 5 == 0 or num % 3 == 0:
        print(num)
