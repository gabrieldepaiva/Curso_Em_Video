def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a turma
    '''
    d = dict()
    d['qdadenotas'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['media'] = sum(num)/len(num)
    if sit == True:
        if d['media'] >= 5:
            d['sit'] = 'Aprovado'
        else:
            d['sit'] = 'Reprovado'
    print(d)
