#
# for i in range(1, 101):
#     print(f"{i}")
#     if i == 7:
#
for i in range(1, 101):
    devided_by_seven = i % 7 != 0
    no_seven = "7" not in str(i)
    if devided_by_seven and no_seven:
        print(i)
