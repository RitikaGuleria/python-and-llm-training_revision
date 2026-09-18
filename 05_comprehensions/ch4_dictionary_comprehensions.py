inr = {
    'Latte': 250,
    "Espresso": 300,
    "Americano": 400,
}

dollar = { coffee : price/80 for coffee,price in inr.items()} #items() gives both key and value
print(dollar)

# output: {'Latte': 3.125, 'Espresso': 3.75, 'Americano': 5.0}