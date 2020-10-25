
upper_limit = int(input("Enter your number: "))

x = 0
y = 1
f = 1


while x <= upper_limit and y <= upper_limit:
    f = x + y
    x = y
    y = f
    if f > upper_limit:
        break
    else:
        print(f)



