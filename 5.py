isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
my_list = []
is_age_above_twentyfour = (a == 24 or strOne == "One")
is_not_max = not strThree != "max"
if isTrue and is_age_above_twentyfour and is_not_max:
    print("true and two")
elif is_age_above_twentyfour and b == 2.5:
    print("blabla2")
else:
    print("blabla")
print("Max")
print(1, 2, 3)

if len(my_list) > 3:
    print("I have items")
else:
    print("I dont have items")
