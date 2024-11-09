list_1 = [3, "apple", 18, "banana", 42, "car", 56, "dog", 7, "city", 99, "tree", 10, "moon", 64, "sky"]
list_2 = ["dog", 18, "apple", 64, "house", 42, "city", 33, 7, "tree", 56, "star", 99, "moon", "sun"]


have_elements: bool = False
for elements in list_1:
    for element in list_2:
        if elements == element:
            have_elements = True

    if have_elements:
        print("TEM ELEMENTOS EM COMUM")
        break