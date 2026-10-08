# 1 - CRIE UM PROGRAMA QUE PARA CALCULAR O IMC DO USUÁRIO

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade Grau I")
elif imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")

# 2 - CRIE UM PROGRAMA QUE PEÇA UM NOME E UMA IDADE E MOSTRE A FRASE: "OLÁ, _______. DAQUI A 10 ANOS VOCÊ TERÁ X ANOS"

nome = input("Nome: ")
idade = int(input("Idade: "))
print(f"Olá, {nome}. Daqui a 10 anos você terá {idade + 10} anos.")

# 3 - FAÇA UM PROGRAMA QUE PEÇA UMA TEMPERATURA EM CELSIUS E CONVERTA PARA FAHRENHEIT (F = C * 9/5 + 32)

c = float(input("Temp em °C: "))
f = c * 9/5 + 32
print(f"Fahrenheit: {f}°F")

# 4 - FAÇA UM PROGRAMA QUE PEÇA 3 NOTAS E FAÇA A MÉDIA.

nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota:'))
nota3 = int(input('Digite a terceira nota:'))

print(f"Média:{(nota1 + nota2 + nota3) / 3:.2f}")


# 5 - FAÇA UM PROGRAMA QUE PEÇA A BASE E A ALTURA DE UM RETÂNGULO E MOSTRE A ÁREA E O PERÍMETRO.

base = float(input("Base: "))
altura = float(input("Altura: "))
print(f"Área: {base * altura}")
print(f"Perímetro: {2 * (base + altura)}")

# 6 MELHORE O PROGRAMA DE IMC CRIANDO CONDIÇÕES PARA:
#Menor que 18,5	Magreza / Abaixo do peso
#Entre 18,5 e 24,9	Peso normal (saudável)
#Entre 25,0 e 29,9	Sobrepeso
#Entre 30,0 e 34,9	Obesidade Grau I
#Entre 35,0 e 39,9	Obesidade Grau II
#Maior ou igual a 40,0	Obesidade Grau III (Grave)

