#1
'''
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('0 e 20:'))
    if 0 <= n <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'{numeros[n]}')'''
#2
'''
lista = []
for i in range(10):
    lista.append(int(input(f'Digite um valor: ')))
diferentes = len(set(lista))
print(f'Existem {diferentes} diferentes')'''
#3
'''
valores = []
for i in range(4):
    valores.append(int(input(f'Digite o {i+1}º valor: ')))
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro 3 foi digitado na posição {valores.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
for n in valores :
    if n % 2 == 0 :
       print(f'Números pares digitados: {n}')'''
#4
'''
import random
lancamentos = [random.randint(1, 6) for _ in range(50)]
percentual = (lancamentos.count(6) / 50) * 100
print(f'Percentual de face 6: {percentual:.1f}%')'
'''
#5
'''
tradutor = {'laranja': 'orange', 'musica': 'music', 'programa': 'program'}
palavra = input('Digite uma palavra em inglês: ').lower()
print(tradutor.get(palavra, 'Tradução não encontrada'))'''
#6
'''
estoque = {}
while True:
    produto = input('Nome do produto (ou "sair"): ')
    if produto.lower() == 'sair':
        break
    quantidade = int(input('Quantidade: '))
    estoque[produto] = estoque.get(produto, 0) + quantidade
print('Estoque atualizado:')
for prod, qtd in estoque.items():
    print(f'{prod}: {qtd}')'''
#7
'''
idades = []
alturas = []
for i in range(5):
    idades.append(int(input(f'Idade da {i+1}ª pessoa: ')))
    alturas.append(float(input(f'Altura da {i+1}ª pessoa: ')))
print('Idades na ordem inversa:', idades[::-1])
print('Alturas na ordem inversa:', alturas[::-1])'''
#8
'''
texto = input('Digite um texto: ').lower()
frequencia = {}
for letra in texto:
    if letra.isalpha():
        frequencia[letra] = frequencia.get(letra, 0) + 1
print(frequencia)'''
#9
'''
def calcular_media(notas):
    return {'média': sum(notas.values()) / len(notas)}
alunos = {'João': 8.5, 'Maria': 9.0, 'Pedro': 7.5}
print(calcular_media(alunos))'''
#10
'''
texto = input('Digite um texto:')
palavras = texto.split( )
total_palavras = len(palavras)
print(f"Total de palavras: {total_palavras}")'''

#11
'''
n=(int(input('Digite um numero: ')))
def positivonegativo(n):
    if n<0:
        print('é negativo')
    else :
        print('é positivo')
positivonegativo(n)'''

#12
'''
n=(int(input('Digite um numero: ')))
def valorabs(n):
    print(abs(n))
valorabs(n)'''
#13
'''
a = (int(input('Digite um numero a: ')))
b = (int(input('Digite um numero b : ')))
lim = (int(input('Digite um numero: ')))
def soma_maior_que_limite(a, b, lim):
    if a + b > lim:
     return True
print({soma_maior_que_limite(a,b,lim)})'''
#14
'''
taxaImposto = (int(input('Digite uma taxa: ')))
custo = (int(input('Digite um custo : ')))
def somaImposto(taxaImposto, custo):
    return custo * (1 + taxaImposto / 100)
print({somaImposto(taxaImposto, custo)})'''
#15
n=(int(input('Digite um numero: ')))
def quantidade_digitos(n):
    print(len(str(abs(n))))
quantidade_digitos(n)