n = (1, 2, 3, 4, 5)
target = 6

found = False

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == target:
            print(n[i], "+", n[j], "=", target)
            found = True

if not found:
    print("It is not possible")