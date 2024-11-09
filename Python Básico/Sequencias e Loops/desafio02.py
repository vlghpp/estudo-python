from array import array


number_sequence = array("i", [1,233,35,74,8,9])
maior = 0
for element in number_sequence:
    if element > maior:
        maior = element


print(f"The largest number in sequence is: {maior}")