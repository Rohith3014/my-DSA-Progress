# 1. Range-based for loop
print("1. Range-based loop:")
for i in range(1, 6):
    print(i)

# 2. Sequence-based for loop (list)
print("\n2. Sequence-based loop (list):")
nums = [10, 20, 30]
for x in nums:
    print(x)

# 3. Sequence-based for loop (string)
print("\n3. Sequence-based loop (string):")
for ch in "hello":
    print(ch)

# 4. Index-based for loop
print("\n4. Index-based loop:")
for i in range(len(nums)):
    print("Index:", i, "Value:", nums[i])

# 5. Nested for loop
print("\n5. Nested loop:")
for i in range(2):
    for j in range(3):
        print(i, j)

# 6. For loop with break
print("\n6. Loop with break:")
for i in range(5):
    if i == 3:
        break
    print(i)

# 7. For loop with continue
print("\n7. Loop with continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# 8. For loop with else
print("\n8. Loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")

# 9. Infinite-like loop (manual stop)
print("\n9. Infinite-style loop (stopped manually):")
count = 0
for i in iter(int, 1):
    print("Hello")
    count += 1
    if count == 3:
        break