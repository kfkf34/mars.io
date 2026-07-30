
lines = int(input("what amount of lines do you want to print? "))
for y in range(lines):
    for z in range(lines - y - 1):
        print(" ", end=" ")
    for x in range(2 * y + 1):
        print("x", end=" ")
    for z in range(lines - y - 1):
        print(" ", end=" ")
    print()