n = int(input("Enter number of elements: "))


arr = []


print("Enter elements:")
for i in range(n):
    val = int(input())
    arr.append(val)


if n > 0:

    max_val = arr[0]


    for i in arr:
        if i > max_val:
            max_val = i


    print("Maximum element =", max_val)
else:
    print("List is empty. No maximum value.")