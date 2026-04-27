# Take number of elements from user
n = int(input("Enter number of elements: "))

# Initialize empty list
arr = []

# Input elements
print("Enter elements:")
for i in range(n):
    val = int(input())
    arr.append(val)

# Check if list is not empty
if n > 0:
    # Assume first element is maximum
    max_val = arr[0]

    # Find maximum element
    for i in arr:
        if i > max_val:
            max_val = i

    # Print result
    print("Maximum element =", max_val)
else:
    print("List is empty. No maximum value.")