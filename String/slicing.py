str = "Hello World Welcome"


print("string is",str)
print("index 0 is",str[0])
print("index 6 is",str[6])
print(str[10])
print("last value",str[-1])
print(str[-5])

# slicing
str1 = str[:3]
print("str1",str1)

str2 = str[1 : 5 : 2]
print("str2",str2)

print("slice 2 ", str[0 : 5 : 2])

str3 = str[-1 : -12 : -2]
str = "Hello World Welcome"

print("reverse slice 1", str3)

print("reverse slice 2",str[-1 : -12 : -2])


# modify methods

str5 = "HeLLo"
print("upper ",str5.upper())
print("lower ",str5.lower())
print("swapcase ",str5.swapcase())

a = "Hello, World!"
print("replaced string ",a.replace("l", "J"))

#string concatenation
concatStr = str3 + str5
print("concatStr ",concatStr)

# escape characters
txt = "We are the so-called \"Vikings\" from the north."

print("escape char ",txt)

print(len(str))
str1 = ""
for i in range(len(str)-1,-1, -1):
    str1 = str1 + str[i]
    print(str[i])
print(str1)

# string format
age = 36
txt = f"My name is John, I am {age}"
print(txt)

age = 10
print("hello ", 1,"world ", 2)
print("hello {} world {} ".format(1,2))

s1 = "hello"
s2 = "hello"
s3 = "hello1"

#to compare values inside the string
print("s1 eq s2 ", s1.__eq__(s2))

#to compare the values of the strings
print("s1 == s2 ", s1 == s2)

#to compare the memory location of the strings
print("s1 is s2",s1 is s2)

print("s1 eq s3 ", s1.__eq__(s3))

print("s1 == s3 ", s1 == s3)


splitstr = str.split( ' ')
print(splitstr)