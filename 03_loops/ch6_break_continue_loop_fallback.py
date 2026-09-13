flavours = ['Ginger','Out of stock','Discontinued','Tulsi']

for flavour in flavours:
    if flavour == 'Out of stock':
        print(f'{flavour} is not available')
        continue
    if flavour == 'Discontinued':
        print(f'{flavour} item found')
        break
    print(f'{flavour} is available')

print('Out of loop')    

#Output:
# Ginger is available
# Out of stock is not aviable
# Discontinued item found
# Out of loop
