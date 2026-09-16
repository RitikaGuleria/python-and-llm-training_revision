# args ,parameters
# *args = returns tuple of its parameters, **kwargs returns dictionary of its elements
# default trap

coffee = "latte"
def prepare(order):
    print(f'Preparing: {order}')

prepare(coffee)


# list : is mutuable
coffee_cup = [1,2,3]
def edit(cup): #parameter
    cup[1]=42
edit(coffee_cup)    #arguement
print(coffee_cup)

#positional arguments and keywords
def drinks(coffee,tea,water):
    print(coffee,tea,water)

drinks('dafodill','cinnamon','still water')    
drinks(tea='ginger',coffee='latte',water='')

# *args and **kwargs
def coffee_and_tea(*args, **kwargs):
    print(f'Coffee types: {args}')
    print(f'Tea types: {kwargs}')

coffee_and_tea('Americano','Espresso',chai1='Cinnamon',chai2='Cardomom')

#psssing value to parameter
def names(name='Riya'):
    pass

#List example
def orders(order=[]):
    order.append('Italian')
    print(order)

# accidentally called it teice, it will generate default trap and give result as ['Italian', 'Italian']
orders()
orders()    

# To avoid above, use NONE
def orderss(order=None):
    if order is None:
        order=[]
    print(order)    

orderss()
orderss()
