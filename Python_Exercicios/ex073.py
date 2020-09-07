times = ('Juventus','Inter','Atalanta','Lazio','Roma',
         'Milan','Napoli','Sassuolo','Fiorentina','Parma','Verona','Bologna','Udinese',
         'Cagliari','Sampdoria','Torino','Genoa','Lecce','Brescia','Spal')
print(f'Os cinco primeiros times são {times[0]}, {times[1]}, {times[2]}, {times[3]} e {times[4]}.')
print(f'Os quatro últimos colocados são {times[-4]}, {times[-3]}, {times[-2]} e {times[-1]}.')
print(sorted(times))
pos_milan = times.index("Milan")+1
print(f'A equipe do Milan está na {pos_milan}ª posição')
