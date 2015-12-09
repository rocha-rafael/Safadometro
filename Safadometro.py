#Safadometro.py

def somatorio(mes):
	c = 0
	for i in range(mes):
		c += i+1
	return c

def WesleySafadao(dia, mes, ano):
	safadeza = somatorio(mes) + (ano/100) * (50-dia)
	anjo = 100 - safadeza
	print('%.2f anjo, mas aquele %.2f safado' %(anjo, safadeza))

def main():
	dia = int(input('Dia: '))
	mes = int(input('Mês: '))
	ano = int(input('Ano: '))
	WesleySafadao(dia, mes, ano)

if __name__ == '__main__':
	main()
