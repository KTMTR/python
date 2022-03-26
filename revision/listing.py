# Serach position number and show the item belong to that number
from sklearn.covariance import EllipticEnvelope


name = ["John", "Mary", "Susan", "William", "Dave"]
print(name[4])

# Replace variable name 
students = ["John", "Mary", "Susan", "William", "Dave"]
for s in students:
    print(s)

# -------------------

# Seeing if a list contains an item, reply in True or False
name = ["John", "Mary", "Susan", "William", "Dave"]
has_Susan = "Susan" in name
print(has_Susan)

# -------------------

# Getting the length of a list, reply in no.
name = ["John", "Mary", "Susan", "William", "Dave"]
print(len(name))

# -------------------

# Adding an item to the end of a list
name = ["John", "Mary", "Susan", "William", "Dave"]
name.append("Grace")
print(name)

name = ["John", "Mary", "Susan", "William", "Dave"]
add_grace = "Grace"
name.append(add_grace)
print(name)

if add_grace in name:
    print(add_grace + " is in the list.")
else:
    print(add_grace + " is out of the list.")

# -------------------

# Inserting an item into a list
name = ["John", "Mary", "Susan", "William", "Dave"]
name.insert(1, "Elle")
print(name)

pauline_add = "Pauline"
name.insert(2, pauline_add)
print(name)

# -------------------

# Changing an item in a list
name = ["John", "Mary", "Susan", "William", "Dave"]
name[3] = "Sally"
print(name)

sam_add = "Sam"
name[2] = sam_add
print(name)

# -------------------

# Combining lists
name = ["John", "Mary", "Susan", "William", "Dave"]
color =["White", "Blue", "Black", "Purple", "Green"]
name .extend(color)
print(name)

# Removing list items by using literal value & position
name = ["John", "Mary", "Susan", "William", "Dave", "Susan", "Susan"]
name.remove("Susan")
print(name)

name = ["John", "Mary", "Susan", "William", "Dave"] # remove the first item (0), remove the last item ()
name.pop(4)
print(name)

# Delete list, reply "name" is not defined
# name = ["John", "Mary", "Susan", "William", "Dave", "Susan", "Susan"]
# del name
# print(name)

# -------------------

# Clearing out a list
name = ["John", "Mary", "Susan", "William", "Dave", "Susan", "Susan"]
name.clear()
print(name)

# -------------------

# Counting how many times an item appears in a list
name = ["John", "Mary", "Susan", "William", "Dave", "Susan", "Susan"]
name_count = name.count("John")
print(name_count)

name = ["John", "Mary", "Mary", "William", "Dave", "Susan", "Susan"]
mary_count = "Mary"
name_count = name.count(mary_count)
print(name_count)

# -------------------

# Finding an list item’s index (position)
name = ["John", "Mary", "Susan", "William", "Dave", "Susan", "Susan"]
susan_index = name.index("Susan")

mary_index = "Mary"
look_for_mary = name.index(mary_index)

print("Susan is at " + str(susan_index))
print(mary_index + " is at index " + str(look_for_mary))

# -------------------

# Alphabetizing and sorting lists (1st to last)
name = ["John", "Mary", "Susan", "William", "Dave", "Susan", "Susan"]
name.sort()
print(name)

## When the list has both upper and lower case string, please use ".sort(key=lambda s:s.lower()" (1st to last)
name = ["john", "Mary", "susan", "william", "Dave", "Susan", "Susan"]
name.sort(key=lambda s:s.lower())
print(name)

# Number sorting (small to large)
number = [1,6, 8, 2, 3, 5, 9]
number.sort()
print(number)

# date sorting  (earlist to latest)
import datetime as dt
datelist = []
datelist.append(dt.date(2011, 1,9))
datelist.append(dt.date(2013, 8,10))
datelist.append(dt.date(2010, 9,10))
datelist.append(dt.date(2004, 9,9))

datelist.sort()
for date in datelist:
    print(f"{date: %Y / %m / %d}")

# reserve sorting by .sort(reverse=True)
name = ["John", "Mary", "Mary", "William", "Dave", "Susan", "Susan"]
name.sort(reverse=True)
print(name)

number = [1,6, 8, 2, 3, 5, 9]
number.sort(reverse=True)
print(number)

# -------------------

# Reversing a list
name = ["John", "Mary", "Mary", "William", "Dave", "Susan", "Susan"]
name.reverse()

print(name)

# -------------------

# Copying a list
name = ["John", "Mary", "Mary", "William", "Dave", "Susan", "Susan"]

# make a copy of a list
backward_name = name.copy()

# reverse a copy
backward_name.reverse()

print(name)
print(backward_name)
