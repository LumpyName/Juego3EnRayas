
#Main.py
"""

"""

#Imprimiendo el plano carteseano
import os
from time import sleep

class ElCuadro:
	LA_X                      =  ['    _    _     ', r'    \\  //     ', r'     \\//      ',  '      ▼▼       ', r'     ▲0\\      ', r'    ▲/  \\     ', r'   //    \\    ']	
	LA_O                      =  ['     _____     ', r'    /----\\    ', r'   //     \0   ', '  |0      ||   ', '  ||      ||   ', r'   \\    //    ', r'    \0000▼     ']   
	_nulo                      =  lambda x: [f'{x}' + ' '*14, ' '*15, ' '*15, ' '*15, ' '*15, ' '*15, ' '*15]
	_listTresEnRayas  =  [
									[_nulo(1), _nulo(2), _nulo(3)],
									[_nulo(4), _nulo(5), _nulo(6)],
									[_nulo(7), _nulo(8), _nulo(9)]
								]
	
	def seterCuadro(self, laX_laO, numero):
		contador = 1
		for x in range(3):
			for y in range(3):
				if contador == numero:
					self._listTresEnRayas[x][y] = laX_laO
				contador += 1
		
	def imprimir(self):
		print('\n' + '-'*49)
		for contador, filasglobales in zip(range(3), self._listTresEnRayas):
			for op1, op2, op3 in zip(filasglobales[0], filasglobales[1], filasglobales[2]):
				print(f'|{op1}|{op2}|{op3}|')
			if contador == 2:
				break
			print('►'+ '-'*47 +'◄')
		print('-'*49 + '\n')

class Jugadores():
	listConfirmation = [
		[1, 2, 3], [3, 6, 9], [1, 5, 9], [3, 5, 7],
		[4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8]
	]
	def __init__(self, laXlaO, objElcuadro, name):
		self.objElcuadro = objElcuadro
		self.laXlaO = laXlaO
		self.name = name
		if laXlaO == objElcuadro.LA_X:
			self.varlistX = []
		else:
			self.varlistO = []
	
	def turno(self, NumCasilla, contador):
		if self.laXlaO == self.objElcuadro.LA_X:
			self.varlistX.append(NumCasilla)
			if contador >= 5:
				if self._is_Ganador(self.varlistX):
					self.objElcuadro.seterCuadro(self.laXlaO, NumCasilla)
					self._victory()
				
		else:
			self.varlistO.append(NumCasilla)
			if contador > 5:
				self.varlistO.append(NumCasilla)
				if self._is_Ganador(self.varlistO):
					self.objElcuadro.seterCuadro(self.laXlaO, NumCasilla)
					self._victory()
				
			
		self.objElcuadro.seterCuadro(self.laXlaO, NumCasilla)
		
	
	def _is_Ganador(self, varList):
		for liste in self.listConfirmation:
			varL = []
			for elements in liste:
				if elements in varList:
					varL.append(True)
			if varL == [True, True, True]:
				return True
	
	def _victory(self):
		os.system('clear')
		self.objElcuadro.imprimir()
		for x in range(5):
			print(f"VICTORIA PARA EL -> {self.name} <-")
			sleep(0.5)
		exit()
		
						
def errorDetectado(turn, lista = None):
	borrar = os.system("clear")
	message = """
ERROR :
TIPO: """
	if lista is not None:
		if turn in lista:
			borrar
			print(message, end="")
			print('	SABOTAJE')
			print('		No puedes quitarle la casilla de tu adversario')
			return True
		else:
			return False
	if turn.isnumeric() is False:
		borrar
		print(message, end="")
		print('	VALOR ERROR')
		print(f'		Tu respuesta tiene que ser un numero, pero escribiste [{turn}]')
		return True
	if (int(turn) > 0 and int(turn) <= 9) is False:
		borrar
		print(message, end="")
		print('	NUMERO ERROR')
		print(f'		Tu respuesta tiene que ser un numero entre 1 y 9, pero escribiste [{turn}]')
		return True
	else:
		return False

def intentalo():
	sleep(7)
	os.system('clear')
	print('Intentalo de nuevo')
	sleep(2)
	os.system('clear')


objCuadro = ElCuadro()
jug1 = Jugadores(ElCuadro().LA_X, objCuadro, "JUGADOR 1")
jug2 = Jugadores(ElCuadro().LA_O, objCuadro, "JUGADOR 2")

os.system('clear')

for contador in range(1, 10):
	if 1 == abs(contador%2):
		while True:
			objCuadro.imprimir()
			print("TURNO DEL JUGADOR 1")
			turno = input("Numero de casilla -> ")
			if errorDetectado(turno):
				intentalo()
				continue
			elif errorDetectado(turno, lista = jug2.varlistO):
				intentalo()
				continue
			else:
				break
		jug1.turno(int(turno), contador)
		
	elif (1 == abs(contador%2)) is False:
		while True:
			objCuadro.imprimir()
			print("TURNO DEL JUGADOR 2")
			turno = input("Numero de casilla -> ")
			if errorDetectado(turno):
				intentalo()
				continue
			elif errorDetectado(turno, jug1.varlistX):
				intentalo()
				continue
			break
		jug2.turno(int(turno), contador)
		
	os.system('clear')



