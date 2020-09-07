def voto (year):
    from datetime import date
    i = date.today().year - year
    if i >= 18:
        v = f'Com {i} anos - Voto Obrigatório'
    elif i == 16 or 17:
        v = f'Com {i} anos - Voto Opcional'
    else:
        v = f'Com {i} anos - Voto Negado'
    return v