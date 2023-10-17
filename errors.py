#estorando um Erro
try: 
    raise ZeroDivisionError("ocorreu um erro")
except Exception as e:
    print(e)
try:
    with open("users.txt", "r") as file:
        file = file.readlines()
    print(file)
    #retry todo
except FileNotFoundError as e:
    print(e)

finally:
    print("executa isso sempre")
