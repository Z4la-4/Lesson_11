
upper_limit = int(input("Please enter your number: "))
x = 0
y = 1
z = x+y

print(x)
print(y)
print(z)

while y < (upper_limit-y):
    x = z
    y = y+z
    z = x+y

    print(y)
    print(z)
