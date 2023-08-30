from heranca import Mae, Filha, Neta

print('Criando objeto de Mae...')
mae = Mae(1)

print('\n\nCriando objeto de Filha...')
filha = Filha(1, 2)

print('\n\nCriando objeto de Neta..')
neta = Neta(1, 2, 3)

print('\nVisualizando os objetos')
print('mae', vars(mae))
print('filha', vars(filha))
print('mae', vars(neta))