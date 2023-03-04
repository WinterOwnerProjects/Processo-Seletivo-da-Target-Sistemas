verificar_num = int(input('Insira o número e verifique se ele existe na sequência de Fibonacci : '))

num_1 = 1
num_2 = 1
contador = 0
loop_num = 900

for _ in range(0, loop_num):
    contador = num_1 + num_2
    num_1 = contador
    num_2 = (contador - num_2)
    
    if contador == verificar_num:
        print('O número {} foi encontrado na sequência de Fibonacci'.format(verificar_num))
        break
    else:
        print('O número {} não foi encontrado na sequência de Fibonacci'.format(verificar_num))
        break
