a = {1, 3, 34, 1} # it's a set 
# print(a)
# print(type(a))

b = {} # it's not set, it's dictionary.
# print(b)
# print(type(b))


#for empyt set need to do

c = set()
print(type(c))
c.add(2)
c.add(2)
c.add(3)
c.add(6)
c.add(345)
c.add(2)
c.add((23,34,43))
# c.add([213,34,23]) # it'll return error
c.remove(2)

print(c)
print(len(c))
print(c.union({2,3,5,6}))
print(c.intersection({2,3,5,6}))