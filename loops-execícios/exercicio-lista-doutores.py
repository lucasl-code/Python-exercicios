# Utilizando append e for coloque todos os nomes da lista de pessoas 
# com o prefixo "Dr. {nome da pessoa}", antes do nome na lista de doutores


# lista de pessoa
pessoas = ["Pedro", "Gustavo", "Gabriel", "Mário"]
doutores = []

for pessoa in pessoas:
    doutores.append(f"Dr. {pessoa}")
print(doutores)





