# 1 sort value
d = {'a': 3, 'b': 1, 'c': 2}
asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
print(asc, desc)

# 2 
d = {'name': 'Alice', 'age': 25}
key = 'age'
print(key in d)

# 3 
d1  = {'a': 1}
d2  = {'b': 2}
merged = {**d1, **d2}
print(merged)

# 4 
t = (1, 2 ,3)
t = t + (4,)
print(t)

# 5
t = ("Hello", 10, 3.14, True)
print(t)

# 6 
nums = [10, 20, 30]
print(sum(nums))

# 7 
print(max(nums))

# 8
nums.append(35)
print(nums)

# 9
from array import array
arr = array('i', [1, 2, 3, 4, 5])
arr.reverse()
print(arr)

#10 
arr = array('i' , [10, 20, 30, 40, 50])
print("Array: {arr}")
print("elements at index 2: {arr[2]}")