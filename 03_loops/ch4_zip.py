# zip can combine lists,tuples or any iterable objects together. It returns an iterator of tuples, where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together, and so on.
# zip() in Python is used to combine two or more sequences item-by-item.

names = ['Anshi','Riyansh','Ansh','Samridhi']
grades = [1,2,3,4]

for name, grade in zip(names,grades):
    print(f"{name} studies in {grade} grade")