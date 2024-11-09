correct_number = 3

for _ in range(0,3):
    chose_number = int(input("Kick a number: "))
    if chose_number == correct_number:
        print("VOCÊ ACERTOU, PARABÉNS")
        break

    print("VOCÊ ERROU, TEM MAIS: ", _ , " tentativas.")