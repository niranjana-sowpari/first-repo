# python list comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an "existing list".
# not necessarily to be just a list, it can be any iterable object TO FORM A LIST****


l1 = ["apple","mango","orange","kiwi","apricot","avocado"]
l2 = [i if "a" not in i else "aaaa" for i in l1 ]
print("l2  ", l2)

l3 = [x for x in range(10)]
print("l3  ", l3)

l4 = "1","2","3","4","5","6"
l5 = [x for x in l4 if int(x)>3]
print("l4  ", l5)
