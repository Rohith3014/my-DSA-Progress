# 1. Remove duplicates from list
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print("1. Remove duplicates:", unique_nums)


# 2. Find intersection of two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersection = list(set(a) & set(b))
print("2. Intersection:", intersection)


# 3. Find union of two lists
union = list(set(a) | set(b))
print("3. Union:", union)


# 4. Check if two lists have common elements
has_common = bool(set(a) & set(b))
print("4. Common elements exist:", has_common)


# 5. Find difference between two sets
difference = set(a) - set(b)
print("5. Difference (a - b):", difference)


# 6. Check subset/superset
x = {1, 2}
y = {1, 2, 3, 4}

print("6. Is subset:", x.issubset(y))
print("   Is superset:", y.issuperset(x))


# 7. Count unique words in sentence
sentence = "python is easy and python is powerful"
words = sentence.split()
unique_words = set(words)

print("7. Unique word count:", len(unique_words))
print("   Unique words:", unique_words)