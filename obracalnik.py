
numbers = None
number_list = []

while numbers != "x":
    numbers = input("Enter your numbers. Once done, press x:\n")
    number_list.append(numbers)

number_list.pop()

for each_item in range(0, len(number_list)):
    number_list[each_item] = int(number_list[each_item])*-1

print(number_list)
