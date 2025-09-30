#questão 3
soma_par = 0
soma_impar = 0
par = []
impar = []
for i in range(10):
    n = int(input(f"digite {i + 1}° numero: "))
    if n % 2 == 0:
        par.append(n)
        soma_par += n
    else:
        impar.append(n)
        soma_impar += n
print(f"lista dos pares: {par}")
print(f"lista dos impares: {impar}")
print(f"soma dos pares: {soma_par}")
print(f"soma dos impares: {soma_impar}")


