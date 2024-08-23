str = "welcome"
len = len(str)
print("len is ", len)
for i in range(0, len):

    print(i)
    if i == 3:
        continue
    print("str", str[i])

str1 = "welcome"
reverse = ""
for i in range(len - 1, -1, -1):
    print("index", str[i])
    reverse += str[i]
    print("revere", reverse)

for i in str:
    print("foreach loop", i)

