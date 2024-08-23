str = "welcome"
for i in str:
    print(i)

# divisible by 2
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# divisible by 5
for i in range(1, 101):
    if i % 5 == 0:
        print(i)

# divisible by 10
for i in range(1, 101):
    if i % 10 == 0:
        print(i)

# not divisible by 3
for i in range(1, 101):
    if i % 3 != 0:
        print(i)

# not divisible by 7
for i in range(1, 101):
    if i % 7 != 0:
        print(i)

str1 = "HELLO"
n = 3
print(n)
if n == 3:
    pass
    print("pass")
print("str1", str1[n])