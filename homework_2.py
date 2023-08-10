#A
# x = int(input("Insert Variables for x: "))
# y = int(input("Insert Variables for y: "))
# if x > y:
#      print("BIG")
# else:
#      print("small")

#B

# for i in range(1, 6):
#     print(i)

#C
 prefix = "Season is: -"
 seasons = ["Summer", "Winter", "Fall", "Spring"]
 for name in seasons:
         if name == "Summer":
             print(f"{prefix} {name}")
         elif name == "Winter":
             print(f"{prefix} {name}")
         elif name == "Fall":
             print(f"{prefix} {name}")
         elif name == "Spring":
             print(f"{prefix} {name}")

#D The loop will run 10 times until loop will rich 11: while count<11, and will print at the end.
 count = 1
 while count<11:
     print(count)
     count = count+1

#E
 age = int(input("Insert your current age: "))
 lastname = str(input("Insert the first letter of your last name: "))
 currency = 0.27
 abroad = str(input("Did you flew abroad? yes/no "))
 if abroad == "yes":
     abroad = "true"
 else:
     abroad = "false"
 flat = 17
 print("The age is: ", age)
 print(f"The first letter of the Lastname is: ", lastname)
 print("The currency is: ", currency)
 print("Did you flew abroad: ", abroad)
 print("Apartmanet number is: ", flat)
 print("Curency + Age = ", age + currency)

#F
# phone = int(input("Insert your phone: "))
# print("Your phone number is", phone)
#G
# def printHello():
#     print("Hello")
# def calculate():
#     print(5+3.2)
# print(printHello())
# print(calculate())
#H

def devidenumber(number):
    print("The result is: ", devide)
def printname(name):
    print("Your name is: " name)

devide = number / 2

name = str(input("Enter your name: "))
number = int(input("Enter the number that you want to devide by 2: "))

