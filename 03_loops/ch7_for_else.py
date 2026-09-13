# for else , fallback logic if for loop is not executed

staff = [('Ritika',14),('Neha',15),('Hrithik',16)]

for name, age in staff:
    if age > 18:
        print(f'{name} is eligible for promotion')
        break
else:
    print('Not eligible')