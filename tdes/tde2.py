'''num=int(input('digite um numero:'))
if num>0:
    print('numero positivo')
elif num<0:
    print('numero negativo')
else:
    print('numero é igual a zero')'''
'''
nota1=float(input('digite um nota:'))
nota2=float(input('digite um nota:'))
nota3=float(input('digite um nota:'))
media = (nota1+nota2+nota3)/3
if media >=7:
    print('aprovado')
elif media<5:
    print('reprovado')
elif media>5 and media<7:
    print('recuperação')
'''
'''
num1=int(input('digite um numero1:'))
num2=int(input('digite um numero2:'))

if num1 % num2 == 0 :
    print('sim')
else:
    print('nao')
'''
'''
num1=int(input('digite um numero:'))
num2=int(input('digite um numero:'))
num3=int(input('digite um numero:'))
if num1<num2 and num2<num3:
    print('sequencia correta')
else:
    print('sequencia incorreta')
'''
'''
num1=int(input('digite um numero:'))
qtdnumi=0
for numi in range (0,num1):
    if numi%2!=0:
        qtdnumi+=1
print(f'ha {qtdnumi} de numeros impares')
'''
'''
num1=int(input('digite um numero1:'))
fatorial=1
for num in range(1,num1+1):
   fatorial=fatorial*num
print(f'o fatorial é {fatorial}')
'''
'''
num1=input('digite um numero1:')
x=len(num1)
print(f'numero de digitos é {x}')
'''
'''
num1 = int(input('Digite um número: '))
y = int(input('Digite até qual número deseja verificar: '))
soma = 0
for x in range(1, y):  
    if num1 % x == 0:
        soma += x
if soma == num1:
    print(f'{num1} é um número perfeito')
else:
    print(f'{num1} não é um número perfeito')
'''

n1 = int(input('Digite quantos números da sequência de Fibonacci deseja calcular: '))

a, b = 0, 1

for _ in range(n1):
    print(a, end=' ')
    a, b = b, a + b

'''
num1 = int(input('Digite um número: '))
limite=int(input('digite um num limite'))
res=0

for x in range(0,limite):
    res=num1*x
    print(f'{res}')
'''