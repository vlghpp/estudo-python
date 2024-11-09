from array import array


number_sequence = array("i", [1,3,5,7,8,9])
sum = 0
for element in number_sequence:
    sum += element


average = sum / len(number_sequence)

print(f"Average is {average}")