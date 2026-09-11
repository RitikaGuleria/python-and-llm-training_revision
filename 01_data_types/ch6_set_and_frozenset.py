# set : It is a collection of unique elements. It is defined using set() constructor.  set is similar like math, it is unordered and unindexed. 
# It is mutable but it can only contain immutable elements. But its elements must be hashable.
# SET
# {  10,  "hello",  (1,2)  }
#     ↑      ↑        ↑
#  immutable immutable immutable . but cannnot put list in it bcz its mutable.

# It has intersection, union, differece, symmetric difference operations.

essentials = {"water","food","oxygen","shelter","money"}
optional = {"luxury","job","money"}

# union : combine uniqueness of both sets , no element will be repeated in the final set.
all = essentials | optional 
print(all)

#intersection
common = essentials & optional
print(common)

#difference : returns the elements which are present in first set but not in second set.
only_in_esssentials = essentials - optional
print(only_in_esssentials)

#membership testing
print("job" in essentials)