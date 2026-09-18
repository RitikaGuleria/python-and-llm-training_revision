# Generator Comprehensions are used for memory optimization. 
# (expression for item in iterable if condition)
# [x for x in items]: it makes entire list in the memory and (x for x in items): gives one item at a time like a stream, we can use in-built func in it for memory optimization.

numbers = [1,2,3,4,5,5,5,6,6]

# case 1
total = (sale for sale in numbers if sale>5)
print(total) #<generator object <genexpr> at 0x10508d700> //this generator object is not usuable right now, it needs to be consumed as they are streaming one by one

total1 = sum(sale for sale in numbers if sale>5)
print(total1) #memory efficient operation  #12

# case 2
total2 = [sale for sale in numbers if sale>5]
print(total2) #[6, 6]