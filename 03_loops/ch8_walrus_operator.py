# walrus operator:  expression will return value of the expression and assign it to the variable.

#1
val = 13

if remainder := val % 2:
    print(f'{remainder} is the remainder and val is not divisible by 2')

#2
sizes = ['XS','S','M','L','XL']

if (avl_size := input('Enter your size: ')) in sizes:
    print(f'{avl_size} is avl')
else:
    print(f'{avl_size} is not avl')    

#3
flavors = ['masala','ginger','cinnamon']
print('Available flavors: ',flavors)

while(flavor := input('choose your flavor: ')) not in flavors:
    print(f'Sorry, {flavor} is not avl')
print(f'You chose {flavor}')    