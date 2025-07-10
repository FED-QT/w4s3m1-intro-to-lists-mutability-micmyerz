# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

a += 1
print("After a += 1:", a, b, id(a), id(b))

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))

# Predict: Before  The value of 'a' vs 'b' will stay the same as no data has been manipulated
# Predict: After   After, the value of 'a' will be changed giving it a new space in memory with a new identifier, and the value of 'b' will stay 100 because the data position in b was not altered. 
# Predict: Before  The vale of x and y will be identical.
# Predict: After   The list will include another position making it 1,2,3,4. The memory position for x will not change 
# 
# Run: Before: 100 100 140733166661640 140733166661640
# Answer: After a += 1: 101 100 140733166661672 140733166661640
    #Before: [1, 2, 3] [1, 2, 3] 1304791376064 1304791376064
    #After x.append(4): [1, 2, 3, 4] [1, 2, 3, 4] 1304791376064 1304791376064

    ## Part 2: Lists, `for`‑loops, `enumerate`, and Methods (≈10 min)

#1. **Extend `exercise.py` with:**

#   ```python
   # Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

   # Task A: Upper‑case each name and store in new list
upper_names = []
for n in names:
    upper_names.append(n.capitalize())  # Capitalize the first letter

   # Task B: Use enumerate to print index + 1 alongside name
   # Expected output:
   # 1. Alice
   # 2. Bob
   # ...
for idx, name in enumerate(upper_names, start=1):
       print(f"{idx}. {name}")
    # Output the upper_names list

   # Task C: Demonstrate at least two list methods (e.g., insert, pop, remove, sort)
upper_names.insert(1, "Kenneth")
print("After inserting 'Kenneth' at position 2:", upper_names)
   #   1. Insert a new name at position 2
upper_names.remove("Charlie")
   #   2. Remove "charlie"
   #   3. Sort the list
   # Print the list after each operation.
#   ```

#2. **Tasks:**

 #  * **Fill in** Task A to build `upper_names`.
  # * **Implement** Task B using `enumerate`.
   #* **Choose** and apply two list methods in Task C; print after each.
   #* **Discuss**: What’s the difference between modifying `names` vs. creating a new list?

#3. **Deliverable:**

 #  * Completed code in `exercise.py` with printed output demonstrating each step
names = ["alice", "bob", "charlie", "dana"]

# Task A: Upper-case each name and store in new list
upper_names = []
for n in names:
    upper_names.append(n.capitalize())
    


# Task B: Use enumerate to print index + 1 alongside name
# Expected output:
# 1. Alice
# 2. Bob
# ...
for idx, name in enumerate(upper_names, start=1):
    print(f"{idx}. {name}")

# Task C: Demonstrate at least two list methods

# 1. Insert a new name at position 2
upper_names.insert(1, "Ken")
print("\nAfter insert at position 2:", upper_names)

# 2. Remove "Charlie"
upper_names.remove("Charlie")
print("After removing 'Charlie':", upper_names)

# 3. Sort the list alphabetically
upper_names.sort()
print("After sorting:", upper_names)