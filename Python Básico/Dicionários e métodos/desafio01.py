text_content = """
A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.
"""


text_content = text_content.lower()

counter = 0

def counter_vowels(text, counter):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in text:
        for letters in vowels:
            if letter == letters:
                counter += 1

    return counter


print(text_content)
print(f"O número de vogais dentro do texto é de : {counter_vowels(text_content, counter)}")