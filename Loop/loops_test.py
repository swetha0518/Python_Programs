# for loop
list = ["apple", "banana", "cherry"]
for x in list:
  print(x)

list = ["apple", "banana", "cherry"]
for i in range(0, len(list)):
  print("list",list[i])

i = 1
while i < 101:
  print("while loop ",i)
  i += 1
else:
    print("break")


# Define the number of rows for the pattern
rows = 5

# Outer loop to iterate through each row
for i in range(1, rows + 1):
    # Inner loop to print the number 'i' i times
    for j in range(i):
        print(i, end=" ")
    # Move to the next line after each row is printed
    print()
