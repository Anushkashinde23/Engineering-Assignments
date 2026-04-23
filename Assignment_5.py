# 1 calculate length of the string
text = "Hi how are you"
length = len(text)
print("The length of the string is:",length)

# 2 String from 1st two and last two char
text = "Apple"
if len(text) < 2:
    result = ""
else:
    result = text[:2] + text[-2:]
    print("Resulting string:", result)

# 3 concatenate two stings 
S1 = "Blue"
S2 = "Rose"
C  = S1 + S2
print("Concatenated string:", C)
