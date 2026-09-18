# List comprehension
# [expression for item in iterable if condition]

names = ['Riya','Megha','Amrit Vani','Vanshika','Suhani','Sumayiya']

ans = [name for name in names if len(name) > 6]
print(ans)

ans2 = [name for name in names if 'ritika' in names]
print(ans2)