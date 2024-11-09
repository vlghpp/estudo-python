list_1 = [3, "apple", 7, "book", 15, "city", 22]

list_2 = ["book", 7, "garden", 22, "dream", 36]

for element in list_1:
    for x in list_2:
        if element == x:
            print(x)
