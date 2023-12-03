
#Break Statement

#=>EX:-1

fruits = ["apple", "banana", "cherry"]
for i in fruits:
  if i == "banana":
    break
  print(i)

#=>EX:-2

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Continue Statement

fruits = ["apple", "banana", "cherry"]
for i in fruits:
  if i == "banana":
    continue
  print(i)

#Else in for loop 

for i in range(6):
  print(i)
else:
  print("Finally finished!")

#Nested Loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#While Loop

i = 1
while i < 6:
  print(i)
  i += 1
