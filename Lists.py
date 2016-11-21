fruitlist = ["apple", "orange","banana", "grape", "mango"]
print(fruitlist[0])
print(fruitlist[-2])

#Concatenation:
numberlist1 = [1,2,3,4,5,6]
numberlist2 = [7,8,9,10]

numberlist3 = numberlist1 + numberlist2
print(numberlist3)

#Multiplication:
numberlist=[1,2,3]
print(numberlist*3)

#Slicing:
fruitlist = ["apple", "orange","banana", "grape", "mango"]
print(fruitlist[2:4])
print(fruitlist[:4])
print(fruitlist[3:])

#Editing a List:
fruitlist = ["apple", "orange","banana", "grape", "mango"]
fruitlist[1] = "kiwi"
print(fruitlist)

#Lists of Lists:
olympiclist=[("London", 2012),("Beijing", 2008),("Athens", 2004)]
print(olympiclist)
print(olympiclist[1])
print(olympiclist[1][0])

#Append
inventorylist=["sword","armour","shield","healing potion"]
print(inventorylist)
inventorylist.append("cabbage")
print(inventorylist)

#Insert
inventorylist=["sword","armour","shield","healing potion"]
print(inventorylist)
inventorylist.insert(2,"cabbage")
print(inventorylist)

#Sort:
inventorylist=["sword","armour","shield","healing potion"]
print(inventorylist)
inventorylist.sort()
print(inventorylist)

#Count:
inventorylist1=["sword", "armour","shield","healing potion","sword"]
print(inventorylist1)
inventorylist1.count("sword")

#Extending a List
print(inventorylist1)
print(fruitlist)

inventorylist1.extend(fruitlist)
print(inventorylist1)
print(fruitlist)

#Pops:
print(fruitlist)
v_fruit = fruitlist.pop()
print(fruitlist)
print(v_fruit)
v_fruit = fruitlist.pop(0)
print(fruitlist)
print(v_fruit)

#Remove
print(fruitlist)
fruitlist.remove("banana")
print(fruitlist)

#Reverse
print(fruitlist)
fruitlist.reverse()
print(fruitlist)

#Index
v_index = fruitlist.index("kiwi")
print(v_index)

#Length
print(fruitlist)
print(len(fruitlist))

#In
print("dragonfruit"in fruitlist)

#Minimum:
print(fruitlist)
print(min(fruitlist))

#Maximum:
print(fruitlist)
print(max(fruitlist))
