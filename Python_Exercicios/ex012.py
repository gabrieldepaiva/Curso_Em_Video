preco = float(input('Quanto custava o produto? R$ '))
desconto = float(input('Qual foi o desconto que o produto recebeu em porcentagem? Ex: 15 - '))
print (
    f"O produto que custava R$ {preco:.2f} com o desconto de {desconto}% passou a custar {preco - (preco * desconto / 100):.2f}.")