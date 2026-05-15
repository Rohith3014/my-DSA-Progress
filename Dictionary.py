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
# 5. Sort Dictionary By Value

data = {
    "a": 3,
    "b": 1,
    "c": 2
}

sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

print("Sorted Dictionary:")
print(sorted_data)



# 6. Find Duplicate Elements Using Dictionary

nums = [1, 2, 3, 2, 4, 1]

dup = {}

for n in nums:
    dup[n] = nums.count(n)

print("\nDuplicate Elements:")

for k, v in dup.items():
    if v > 1:
        print(k)



# 7. Word Count In Sentence

text = "apple banana apple"

count = {}

for word in text.split():
    count[word] = text.split().count(word)

print("\nWord Count:")
print(count)



# 8. Invert Dictionary

data = {
    "a": 1,
    "b": 2
}

invert = {}

for k, v in data.items():
    invert[v] = k

print("\nInverted Dictionary:")
print(invert)