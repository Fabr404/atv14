def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Receber as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = calcular_media(nota1, nota2, nota3)

# Exibir o resultado
print(f"A média do aluno é: {media:.2f}")
print(f"O aluno está: {verificar_situacao(media)}")
