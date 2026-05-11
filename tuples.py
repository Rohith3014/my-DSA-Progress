# Tuple Programs – Single Full Code

print("===== 1. Swap Two Variables Using Tuple =====")

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)

print("\n===== 2. Count Occurrences of Element =====")

t1 = (1, 2, 2, 3, 4, 2, 5)

count_value = t1.count(2)

print("Tuple:", t1)
print("Occurrences of 2 =", count_value)

print("\n===== 3. Convert List → Tuple and Tuple → List =====")

# List to Tuple
my_list = [10, 20, 30, 40]

my_tuple = tuple(my_list)

print("Original List:", my_list)
print("Converted Tuple:", my_tuple)

# Tuple to List
t2 = (1, 2, 3, 4)

my_new_list = list(t2)

print("Original Tuple:", t2)
print("Converted List:", my_new_list)

print("\n===== 4. Find Max and Min in Tuple =====")

t3 = (10, 50, 20, 80, 5)

maximum = max(t3)
minimum = min(t3)

print("Tuple:", t3)
print("Maximum Element:", maximum)
print("Minimum Element:", minimum)

print("\n===== 5. Tuple Unpacking with Multiple Values =====")

student = ("Rohit", 21, "Python", "Bangalore")

name, age, course, city = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)

print("\n===== 6. Advanced Tuple Unpacking using * =====")

t4 = (1, 2, 3, 4, 5, 6)

a, *b, c = t4

print("First Value:", a)
print("Middle Values:", b)
print("Last Value:", c)