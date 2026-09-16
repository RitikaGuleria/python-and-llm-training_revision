def status(cups):
    if cups == 0 :
        return 'Sorry, No cups left'
    return 'Your order is ready'
    print('not get executed bcz after return nothing will get executed')

print(status(0))
print(status(2))

#returning multiple values
def report():
    return 1,2,3

a,b,_ = report()
print(a,b)
