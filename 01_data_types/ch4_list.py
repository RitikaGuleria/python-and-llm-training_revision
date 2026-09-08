#List: List is mutuable, ordered collection of items. It can contain duplicate values. It is defined using square brackets [].

ai = ["Python","AI","ML","DL"]
ai.append("NLP") #adding an item to the list
print(ai)

ai.remove("Python")
print(ai)

cs = ["C","Java"]
core = ["DSA","OS","DBMS","System design"]
cs.extend(core) #adding multiple items to the list
print(cs)

cs.insert(1,"C++")
print(cs)

last_item = cs.pop() #removes the last item from the list
print(f"Last item removed: {last_item}")
print(cs)

cs.reverse() #return none
print(cs)
cs.sort()
print(cs)

a = [1,2,3,4,5,0]
print(max(a))
print(min(a))
