def calculate_porcentage(correct_answers: int) :
    return (correct_answers * 100) / len(capital_state)


capital_state = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Goiás": "Goiânia",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Pernambuco": "Recife",
    "São Paulo": "São Paulo",
    "Santa Catarina": "Florianópolis"
}

correct_answers = 0
response_user_continue = ""
for state, capital in capital_state.items():
    response_user_state = input(f"What is the state capital of {state}? ")
    if response_user_state == capital:
        correct_answers += 1

    response_user_continue = input("Do you want to continue? [S/N]")
    if response_user_continue == "S":
        continue
    else:
        break


result_porcentage = calculate_porcentage(correct_answers)
print(f"Number correct answers {correct_answers} and your porcentage: {result_porcentage}")
