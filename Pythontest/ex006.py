salario = float(input("digite o salario do funcionario:"))
if salario > 1250.00:
    salario = salario * 0.10 + salario
else:
    salario = salario * 0.15 + salario
print("o salario do funcionario com aumento é de R${salario}")



