correct_name = "admin"
correct_password = "admin"



user_name = input('Enter your name: ')
user_password = input('Enter your password: ')


if user_name == correct_name and user_password == correct_password:
    print("ACESSO PERMITIDO")
elif user_name != correct_name and user_password != correct_password:
    print("USUÁRIO E SENHA INCORRETOS!")
elif user_name != correct_name:
    print("ACESSO NEGADO. USUÁRIO INCORRETO!")
elif user_password != correct_password:
    print("ACESSO NEGADO. SENHA INCORRETA!")
