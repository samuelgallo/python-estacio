from time import sleep
from threading import Thread

def tarefa(tempo_espera, mensagem):
	print(f'\nIniciando a tarefa {mensagem}')
	sleep(tempo_espera)
	print(f'Conclusao da tarefa {mensagem}')

thread = Thread(target=tarefa, args=(2, 'Thread em execucao'))
thread.start()
print('\nAguardando pela execucao da Thread...')
thread.join()
print('A execucao foi concluida')
