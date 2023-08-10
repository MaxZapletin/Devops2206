# first = 7
# second = 44.3
# print(first + second)
# print(first * second)
# print(first / second)
#
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8

print(f"a: {a} b: {b} c: {c}")
print(a, b, c)



# my_number = 5 + 5
#
# print("result is: " + str(my_number))
#
# x = 5
#
# y = 2.36
#
# print(x + int(y))
# a = 8
#
# b = "123"
#
# print(a + int(b))

a = 8
b = "1"
if b.isnumeric():
  print(a + int(b))
else:
  print("Variable b must be an integer as a string.")
x = "Hello"
y = "World"
print(x + y)

num = int(input("Enter a number: "))
sum_total = 0

for i in range(1, num + 1):
    sum_total += i

print("The sum of numbers from 1 to", num, "is:", sum_total)

