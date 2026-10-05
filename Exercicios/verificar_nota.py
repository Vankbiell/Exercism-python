nota1 = int(input("Qual a primeira nota?"))
nota2 = int(input("Qual a segunda nota?"))
media = (nota1 + nota2) / 2
print("A media é",media)
if media > 6:
    print("Passou")
else:
    print("Não passou")