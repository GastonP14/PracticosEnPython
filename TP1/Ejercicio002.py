print('Programa que muestra todos los numeros pares positivos hasta el numero introducido por el usuario',end='\n')
numero = int(input('Ingrese N >>> '))

for i in range(numero):
    if i%2==0:
        print(i,end=' ')