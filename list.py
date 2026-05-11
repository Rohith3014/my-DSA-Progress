# 1. Reverse a List
nums = [1, 2, 3, 4, 5]
print("Reverse:", nums[::-1])


# 2. Find Second Largest Number
nums = [10, 20, 4, 45, 99]
nums.sort()
print("Second Largest:", nums[-2])


# 3. Remove Duplicates from List
nums = [1, 2, 2, 3, 4, 4, 5]
print("Without Duplicates:", list(set(nums)))


# 4. Rotate List Left
nums = [1, 2, 3, 4, 5]
left_rotate = nums[1:] + [nums[0]]
print("Left Rotate:", left_rotate)

# Rotate List Right
right_rotate = [nums[-1]] + nums[:-1]
print("Right Rotate:", right_rotate)


# 5. Find All Pairs with Given Sum
nums = [1, 2, 3, 4, 5]
target = 6

print("Pairs with Sum =", target)

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])


# 6. Merge Two Sorted Lists
a = [1, 3, 5]
b = [2, 4, 6]

merged = sorted(a + b)

print("Merged List:", merged)


# 7. Move All Zeros to End
nums = [0, 1, 0, 3, 12]

result = []

for num in nums:
    if num != 0:
        result.append(num)

for num in nums:
    if num == 0:
        result.append(num)

print("Zeros at End:", result)


# 8. Find Missing Number in List
nums = [1, 2, 3, 5]

n = 5

expected = sum(range(1, n + 1))
actual = sum(nums)

print("Missing Number:", expected - actual)


# 9. Check if List is Palindrome
nums = [1, 2, 3, 2, 1]

if nums == nums[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 10. Flatten a Nested List
nums = [[1, 2], [3, 4], [5]]

flat = []

for sublist in nums:
    for item in sublist:
        flat.append(item)

print("Flattened List:", flat)