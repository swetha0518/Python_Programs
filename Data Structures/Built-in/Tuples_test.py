#TUPLE
t1 =[1,2,3,4,5]
print(t1)

t2 = ("a","b","c","d","e","f","g","h","i","j")
print(len(t2))

fruits = ("apple", "banana", "cherry", 10)

print(fruits)

#fruits.remove("Kiwi")
#fruits.insert(4,"Kiwi")

print(fruits)


fruits1 = ("apple")
print(fruits1)
print(type(fruits1))

fruits2 = ("apple",)
print(fruits2)
print(type(fruits2))

a = 10
print(type(a))

#convert list to tuples and vice versa
fruitlist = ["Mango","Cherry","Grapes"]
thistuple = tuple(fruitlist)
print(type(thistuple))

newlist = list(thistuple)
print(type(newlist))

len(thistuple)


#Adding a tuple to a tuple
y = ("orange",)
thistuple += y
print(thistuple)

#unpack tuples
(green, yellow, red, num) = fruits

print(green)
print(yellow)
print(red)
print("num ",num)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

#using asterisk
(green, yellow, *red) = fruits

print("green ",type(green))
print("red type ",type(red))
(green, *tropic, red) = fruits

print(green)
print("tropic ",tropic)
print(red)


#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#delete tuple
del thistuple
#print(thistuple)

#methods

print("count of apple",mytuple.count("apple"))
print("index of apple",mytuple.index("apple"))