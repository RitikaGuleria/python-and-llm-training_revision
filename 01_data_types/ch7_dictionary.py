names = dict(type="boys", count = 3, grade = "A")
print(names)

# another way of creating dictionary
meals = {}
meals['Pre '] = "coffee"
meals["Breafast"] = "home food"
meals["drinks"] = "shake with whey protein"
print(meals)
print(meals["drinks"])

del meals["drinks"]
print(meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())


last_item = meals.popitem() # removed last element
print(f"last item removed is {last_item}")

drinks = {"chai":"yes","coffee":"yes"}
meals.update(drinks)
print(meals)

# everything like union etc supported in dict as well like set