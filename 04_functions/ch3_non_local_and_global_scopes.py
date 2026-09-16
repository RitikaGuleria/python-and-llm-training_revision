# non local
def update_order():
    chai = 'Cinnamon'
    def inner():
        #non local refers to the variable of outer function or outside its scope and can change the same variable's value.
        #nonlocal is used inside a nested function when you want to modify a variable that belongs to the outer (enclosing) function.
        #nonlocal is designed in such a way that it should be looking just above its function ie outer function not globally
        nonlocal chai 
        chai = 'Kesar'
    inner()
    print(f'Chai: {chai}')    

update_order()    

#global
coffee = 'Black'

def coffee_order():
    def inner():
        global coffee
        coffee = 'Espresso'
    inner()

coffee_order()
print(f'coffee: {coffee}')