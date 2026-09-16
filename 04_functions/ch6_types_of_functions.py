# Pure and Impure functions
# Recursive functions
# Lambdas or Anonymous functions

# Pure function
def pure_fun(cups):
    return cups * 10

print(pure_fun(2))

# Impure function which are not recommeded bcz if more than one func will try to modify global variable, it will get very confusing
total = 0
def impure_func(cups):
    global total
    total += cups

print(impure_func(2))

# Recursive func
def recursive_func(n):
    if n==0:
        return 'all done!!'
    return recursive_func(n-1)

print(recursive_func(3))

# Lambda functions
coffees = ['Latte','Espresso','Capucinno','Latte']

answer = list(filter(lambda c: c!='Latte',coffees))

print(answer)

#Built in functions
def tea_flavor(flavor='ginger'):
    """Return the flavor of the tea"""
    return flavor

print(tea_flavor.__name__) #dunder
print(tea_flavor.__doc__)