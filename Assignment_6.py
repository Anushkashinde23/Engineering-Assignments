# 1 membership operators
Fruits = ["apple", "banana", "strawberry", "mango"]
# using in
print("Is 'mango' in the list?","mango" in Fruits)
# using 'not in'
print("Is 'orange' not in the list?","orange" not in Fruits)

# 2 indexing 
numbers = [10, 20, 30, 40, 50]
print("Origenal list:", numbers)
print("First element (Index 0):", numbers[0])
print("Last element (Negative Index -1):", numbers[-1])
print("Slicing (First three elements):", numbers[0:3])

# 3 update,append, insert, delete elements
colors = ["Red", "Blue", "Green", "Grey"]
# update
colors[1] = "Yellow"
# append
colors.append("Purple")
# insert 
colors.insert(1, "Orange")
# Delete
colors.remove("Green")
print("Modified list:", colors)

# 4 basic operations
list1 = [1, 2, 3]
list2 = [4,5]
# Concatenate 
c = list1 + list2
print("Concatenation:", c)
# Repetition
repeat = list1 * 2
print("Repetition:", repeat)
# length , max, min
nums = [10, 5, 100, 2]
print("Length:", len(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))