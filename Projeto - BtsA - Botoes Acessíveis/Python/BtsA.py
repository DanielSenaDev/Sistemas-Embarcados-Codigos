import serial
import time
import pyautogui

# Recebe o codigo do botão e aciona a tecla respectiva
def teclar (bti):

	tecla = ''
	# Atribui a variavel tecla o botao acionado
	if bti == "bt1":
		tecla = 'up'
	elif bti == "bt2":
		tecla = 'left'
	elif bti == "bt3":
		tecla = 'down'
	elif bti == "bt4":
		tecla = 'right'

	pyautogui.keyDown(tecla) # Aciona a tecla
	time.sleep(1)
	pyautogui.keyUp(tecla) # Desativa a tecla

# Configuracao Porta Serial
ser = serial.Serial('COM10', 9600) # alterar para a porta serial disponivel
time.sleep(1) # tempo necessario para configuração da porta


print("INICIADO")
while 1:
	
	botao = str(ser.readline().decode().strip('\r\n'))
	print(botao, flush=True)
	
	# Codigo usado para mover o mouse de janela, mas so esta sendo usado por ser um simulador que aciona o botao e nao usando hardware
	posInit = pyautogui.position() # Posicao Inicial de onde foi feito o clique
	posDest = (200, 200) # Posicao do lado esquerdo da tela
	pyautogui.moveTo(posDest) # Move o mouse para a posicao definida
	pyautogui.click() # Clica com o mouse para deixar a janela da aplicacao ativa

	# Funcao para acionar teclas
	teclar(botao)

	# Retornar mouse para posicao no momento que acionou o botao
	posReturn = posInit + (90,90) # Posicao de retorno
	pyautogui.moveTo(posReturn) # Move o mouse de volta ao simulador