num = int(input("Hoe groot moet de piramide?"))

# Opdracht 1
def print_pyramid_up(index):
    for index in range(index):
        for item in range(index + 1):
            print("*", end="")
        print("")
    print_pyramid_down(index - 1)


def print_pyramid_down(index):
    for index in range(index, 0, -1):
        for item in range(index, 0, -1):
            print("*", end="")
        print("")


def print_pyramid_up_while(index):
    num = 1
    while num <= index:
        num2 = 1
        while num2 <= num:
            print("*", end="")
            num2 += 1
        print("")
        num += 1
    print_pyramid_down_while(index - 1)


def print_pyramid_down_while(index):
    num = index
    while num > 0:
        num2 = num
        while num2 > 0:
            num2 -= 1
            print("*", end="")
        print("")
        num -= 1

print_pyramid_up(num)
print_pyramid_up_while(num)