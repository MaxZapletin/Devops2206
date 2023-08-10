from typing import List

name = "Max"
prefix = "my name is"
names = ["ofek", "idan", "eden", "aviran"]
for i in range(1, 8):
    print(f"{i}. {prefix} {name}")

prefix = "my name is"
names = ["ofek", "idan", "eden", "aviran"]
for name in names:
    print(f"{prefix} {name}")

prefix = "my name is"
names = ["ofek", "idan", "eden", "or", "aviran", "avidan", "daniel"]
for name in names:
        if name == "or":
            continue
        name = name + "Z"
        print(f"{prefix} {name}")

prefix = "my name is"
names = ["ofek", "idan", "eden",  "aviran", "avidan", "daniel"]

for i, name in enumerate(names):
    print(f"index = {i}, name = {name}")

for i in range(len(names)):
    print(f"index = {i}, name = {names[i]}")


for name in names:
    print(f"Looking for or currently is : {name}")
    if name == "or":
        print("Found Or")
        break
    print("Did not found or yet")
else:
    print("dont find or")

# names = ["ofek", "idan", "eden", "or", "aviran", "avidan", "daniel"]
# for name in names:
#     print(f"Looking for or currently is : {name}")
#     if name == "or":
#         pass
#     else:
#     print("Did not found or yet")
# else:
#     print("dont find or")






for i in range(len("names")):
    range(str())
    range(())

    names[i] = names[i] + "Z"
    print(f"{prefix} {names[i]}")
result = [1, 2, 3, 4, 5, 6]
for name in names:
    if name.find("dan") > -1:
        print(name)
        result.append()
        a = result
print(result)

result = []
for name in names:
    if name.find("dan") > -1:
        print(name)
        result.append(name)

my_other_result = [name for name in names if name.find("dan") > -1]
print(result)

names_with_z_contaiting_dan = [name for name in names if name.find("dan") > -1]
for name in names_with_z_contaiting_dan:
print(name)
print(names_with_z_contaiting_dan)


age = int(input("enter your age"))
while age < 50:
    print("You are young")
    age = age + 5
    age = int(input("enter your age"))

for i in range(len(names)):
    if names[i] == "or":
        names[i-1] = names[i-1] + "z"

