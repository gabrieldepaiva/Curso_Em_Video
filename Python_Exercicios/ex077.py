palavra = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
vogal = ('a','e','i','o','u')
for cadapalavra in range(0,len(palavra)):
    print(f'\nNa palavra {palavra[cadapalavra]} temos as seguintes vogais - ',end='')
    for cadavogal in range(0, len(vogal)):
        if vogal[cadavogal] in palavra[cadapalavra]:
            print(palavra[cadapalavra][palavra[cadapalavra].index(vogal[cadavogal])],end=' ')