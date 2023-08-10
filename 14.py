#Divide by 0
try:
    a = int(input("enter number"))
    b = int(input("enter number"))
    print(a / b)

except ZeroDivisionError as e:
    print("YOu tried divide by zero")
    print(e.args)
# except ValueError as e:
#     print("Bad input")
#     print(e.args)
except BaseException as e:
    print(e.args)
print("Aviel")