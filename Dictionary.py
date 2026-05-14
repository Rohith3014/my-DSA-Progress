# 1. Count Frequency
data = ["apple", "banana", "apple", "mango"]

count = {}

for item in data:
    count[item] = data.count(item)

print("Frequency:")
print(count)


# 2. First Non-Repeating Character
text = "abcdabde"

for ch in text:
    if text.count(ch) == 1:
        print("\nFirst Non-Repeating Character:")
        print(ch)
        break


# 3. Group Elements By Frequency
group = {}

for item in data:

    c = data.count(item)

    if c not in group:
        group[c] = []

    group[c].append(item)

print("\nGroup By Frequency:")
print(group)


# 4. Merge Two Dictionaries
dict1 = {"a": 1}
dict2 = {"b": 2}

dict1.update(dict2)

print("\nMerged Dictionary:")
print(dict1)