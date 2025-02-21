'''
8. Um número perfeito é um número que é igual à soma de seus divisores,
excluindo ele mesmo. Crie um programa que verifique se um número
informado pelo usuário é perfeito.
9. Crie um programa que gere a sequência de Fibonacci até o n-ésimo termo,
onde o primeiro e o segundo termo são 0 e 1, e os termos seguintes são a
soma dos dois termos anteriores.
10.Peça ao usuário para inserir dois números: um número base e um limite. Em
seguida, multiplique o número base por 1, 2, 3 até o limite e mostre a
tabuada.'''
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
