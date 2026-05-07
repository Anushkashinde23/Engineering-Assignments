# 1 creating a tuple
f = ("apple", "banana", "mango")

# length
print("length:", len(f))
# concatenation
a = ("pineapple", "grapes")
c = f + a 
print("concatenation:", c)
# repetition
s = f * 2 
print("Repeated:", s)
# membership
print("Is apple in f?", "apple" in f)

# 2 specific items
n = (10, 20, 30, 40, 50)
# indexing
print("first item:", n[0])
# negative indexing
print("last item:", n[-1])
# slicing 
print("middle three:", n[1:4])
# iteration
print("looping through items:") 
for num in n: print(num)

# 3
colors = ("red", "green", "blue")
print("Attempting to change index 0...")
try:
    colors[0] = "Yellow"
except TypeError:
    print("Error: You cannot change a tuple!")
#deletion
del colors
print("Tuple deleted successfully.")

# 4 sequence 
list = [15, 3, 27, 67,7]
tuple = tuple(list)
print("converted Tuple:", tuple)
# using built in 
print("count (len):", len(tuple))
print("highest (max):", max(tuple))
print("lowest (min):", min(tuple))