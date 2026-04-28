num = int(input("Enter number: "))
bits = []

if num < 0:
    print("Error, enter a positive number")
if num == 0:
    print("0")
else:
    while num > 0:
        x = num % 2
        bits.append(x)
        num = num // 2
    bits = reversed(bits)
    for i in bits:
        print(i, end='')
    print()