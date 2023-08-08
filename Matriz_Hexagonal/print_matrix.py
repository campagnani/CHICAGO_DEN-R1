for y in range(23):
    row = []
    for x in range(23):
        if (x < 9 and y < 7) or (x > 13 and y < 7) or (y > 12):
            print("7 ", end="")
        elif (y < 7 and x >= 9 and x <= 13) or (y >= 7 and y <= 12 and (x == 10 or x == 12)):
            print("0 ", end="")
        else:
            print("1 ", end="")
    print("\n")
