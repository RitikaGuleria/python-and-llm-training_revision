#set comprehension
# {expression for item in iterable if condition}

coffees = ['americano','latte','latte','espressso','americano']

ans = {coffee for coffee in coffees }
print(ans) #output: {'latte', 'americano', 'espressso'}

ans2 = {coffee for coffee in coffees if len(coffee) < 6}
print(ans2) #{'latte'}

# Complex example: how to remove duplicacy from this dictionary using set comprehensions?
hobbies = {
    "Riya": ['Gym','Sleeping','Health eating','Learning','Planting','Going outside and exploring cafes','Getting ready a lil','skincare'],
    "Megha": ['Gym','Speaking','Learning and curing patients','Going outside','Makeup','skincare'],
    "Amrit Vani": ['Makeup','skincare']
}

unique_ans = {item for valuesofonelist in hobbies.values() for item in valuesofonelist}
print(unique_ans)