def chai_counter():
    order='lemon' #enclosing scope
    def inner():
        order='ginger'
        print(f'Inner: {order}')
    inner()
    print(f'Outer: {order}')

order= 'Tulsi' #global scope
chai_counter()
print(f'Global: {order}')    