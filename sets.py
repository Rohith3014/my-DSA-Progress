# Python program for set operations

# Input lists
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [3, 4, 5, 6, 7]

# 1. Remove duplicates
print("1. Remove duplicates:")
print(list(set(list1)))

# 2. Intersection
print("\n2. Intersection of two lists:")
print(list(set(list1) & set(list2)))

# 3. Union
print("\n3. Union of two lists:")
print(list(set(list1) | set(list2)))

# 4. Check common elements
print("\n4. Common elements exist?")
if set(list1) & set(list2):
    print("Yes")
else:
    print("No")

# 5. Difference between two sets
print("\n5. Difference (list1 - list2):")
print(set(list1) - set(list2))

# 6. Subset / Superset
a = {1, 2}
b = {1, 2, 3, 4}

print("\n6. Subset / Superset Check:")
print("a is subset of b:", a.issubset(b))
print("b is superset of a:", b.issuperset(a))

# 7. Count unique words
sentence = "python is easy and python is powerful"

words = sentence.split()
unique_words = set(words)

print("\n7. Count unique words:")
print("Unique words:", unique_words)
print("Count:", len(unique_words))