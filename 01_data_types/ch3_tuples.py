# Tuples : () paranthesis are used to create tuples. They are immutable, they cannot be changed once created. They are used to store multiple items of different data types in a single variable.They are ordered and allow duplicate items. They are faster than lists and are used when we want to store data that should not be changed.

spices = ("cardomom","cinamon","cloves")
print(spices)

# unpacking
spice1,spice2,spice3 = spices
print(f"{spice1}, {spice2}, {spice3}")

# tuples works behind the scenes when we assign multiple values to multiple variables. It creates a tuple and unpacks it into the variables.
a, b = 1,2
print(f"a:{a}, b:{b}")

# flip : swapping values of a and b
a,b = b,a
print(f"a:{a}, b:{b}")

# membership testing
print(f"Is cardomom in spices? {"cardomom" in spices}")

# You cannot change the tuple's elements/references. But if a tuple contains a mutable object, you can modify that object.