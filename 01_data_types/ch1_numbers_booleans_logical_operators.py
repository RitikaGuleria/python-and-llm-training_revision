#Mutability and Immutability
#Mutable:The same object can be modified without creating a new object. Mutable = same object, changed value.
#Immutable: The same object cannot be modified. If you try to change its value, Python creates/uses a different object, and the variable refers to that new object. Immutable = new object, new value.

# Numbers
a = 4
b = 2
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# boolean
is_hot = False #0
count = 5
total = count + is_hot #upcasting //0 
print(f"Total: {total}") 

is_cold = True #1
count = 5
total_cold = count + is_cold #upcasting //1
print(f"Total: {total_cold}")

# bool method
is_credited = 0 #None
print(f"Is it credited? {bool(is_credited)}")

is_debited = 1
print(f"Is it debited? {bool(is_debited)}")

# Logical Operators
x= True
y= False
z = None

ans = x and y
print(ans)

ans1 = x or y
print(ans1)

ans2 = not x
print(ans2)

ans3 = x and z
print(ans3)

ans4 = y and z
print(ans4)