food = "Pizza"
# food = food.replace("z", "s")
food.replace("z", "s")
print(food)   # String are Immutable



#Mutable vs Immutable in Python
#🔒 1. Immutable (Change nahi hota)

#Immutable objects ko change nahi kar sakte. Agar change karoge to naya object banega.

#Examples:

# str

# int

# float

# tuple

#✅ String Example (Immutable)
text = "Hello"
print(id(text))   # memory address

text = text.replace("H", "Y")
print(text)
print(id(text))   # new memory address
#🔎 Kya hoga?

# "Hello" change nahi hua.

# replace() ne nayi string banayi.

# Memory address change ho gaya.

# 👉 Isliye strings immutable hoti hain.