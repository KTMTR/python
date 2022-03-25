name = ("a", "b", "c", "d", "a")
print(len(name))

print(name.count("a"))

look_for = "c"
if look_for in name:
    pp = name.index(look_for)
else:
    pp = -1
    
print(pp)

 #Loop through and display each item in the tuple.
for n in name:
     print(f"{n}")

number = (1, 2, 3, 4, 5, 1, 2, 3, 900)

 #Loop through and display each item in the tuple.
for nn in number:
     print(f"{nn:.3f}")
