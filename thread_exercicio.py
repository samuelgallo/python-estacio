from time import sleep
from threading import Thread

def tarefa(tempo_espera, mensagem):
	print(f'\nIniciando a tarefa {mensagem}')
	sleep(tempo_espera)
	print(f'Conclusao da tarefa {mensagem}')

thread = Thread(target=tarefa, args=(3, 'Thread em execucao'))

thread2 = Thread(target=tarefa, args=(2, 'Thread em execucao 2'))

thread.start()
thread2.start()

print('\nAguardando pela execucao da Thread...')

thread.join()
thread2.join()

print('A execucao foi concluida')
