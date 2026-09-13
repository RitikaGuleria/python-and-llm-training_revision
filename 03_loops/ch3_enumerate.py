menu = ['coffee','tea','milk','water']

for index,item in enumerate(menu,start=1):
    #print(index,item)
    print(f"{index} : {item}")


print(list(enumerate(menu,start=1)))

#enumerate() in Python is a simple way to get both the index (position) and the value of each item while looping.

# for i in range(len(fruits)):
#     print(i, fruits[i])

# with enumerate it becomes more easy and readable

for idx,val in enumerate(menu,start=1):
    print(idx,val)