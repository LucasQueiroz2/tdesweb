from tkinter import*
from tkinter import ttk

'''i = Tk()

label_numero =Label(i, text="Numero:", font=("Arial", 12))
label_numero.grid(row=0, column=0, padx=10, pady=10) 
entry_numero = Entry(i, font=("Arial", 12))
entry_numero.grid(row=0, column=1, padx=10, pady=10)
def neg_pos():
          
          numero = float(entry_numero.get())


          if numero>0:
            result=('positivo')
          else:
            result=('negativo')
          resultado_label.config(text=f"Numero:{result}")

button = Button(i, text="Mostrar", font=("Arial", 12),
command=neg_pos)
button.grid(row=2, column=0, columnspan=2, pady=20)

resultado_label = Label(i, font=("Arial", 12))
resultado_label.grid(row=3, column=0, columnspan=2)
i.mainloop()'''
'''
from tkinter import *
from tkinter import messagebox

def verificar_limite():
    try:
        lista_numeros = [float(num.strip()) for num in entrada_lista.get().split(',') if num.strip()]
        limite = float(entrada_limite.get())
        
        if lista_numeros != sorted(lista_numeros):
            messagebox.showwarning("Aviso", "A lista não está ordenada!")
            return
            
        indice = -1
        for i, num in enumerate(lista_numeros):
            if num > limite:
                indice = i
                break
                
        messagebox.showinfo("Resultado", f"Índice encontrado: {indice}")
        
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

root = Tk()
root.title("Verificador de Limite")
root.geometry("400x250")

Label(root, text="Lista de números ordenados (separados por vírgula):").pack(pady=5)
entrada_lista = Entry(root, width=50, font=('Arial', 12))
entrada_lista.pack(pady=5)

Label(root, text="Limite desejado:").pack(pady=5)
entrada_limite = Entry(root, font=('Arial', 12))
entrada_limite.pack(pady=5)

Button(root, text="Verificar", command=verificar_limite).pack(pady=15)

root.mainloop()'''
k=Tk()
label_ano =Label(k, text="ano:", font=("Arial", 12))
label_ano.grid(row=0, column=0, padx=10, pady=10) 
entry_ano = Entry(k, font=("Arial", 12))
entry_ano.grid(row=0, column=1, padx=10, pady=10)
def bisexto():
         ano = float(entry_ano.get())
         if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):   
                 resultado=('é ano bissexto')   
         else:
            resultado=('não é bissexto') 
         resultado_label.config(text=f"Numero:{resultado}")
button = Button(k, text="Mostrar", font=("Arial", 12),
command=bisexto)
button.grid(row=2, column=0, columnspan=2, pady=20)

resultado_label = Label(k, font=("Arial", 12))
resultado_label.grid(row=3, column=0, columnspan=2)

k.mainloop()


'''
Exercício 3: Verificar se o ano é bissexto
● Criar uma interface onde o usuário insere um ano, e ao pressionar um botão, a
aplicação verifica se o ano é bissexto ou não e exibe uma mensagem informando o
resultado.
● Crie um campo de entrada para o usuário inserir o ano.
● Crie um botão que, quando pressionado, verifica se o ano é bissexto.
● Exiba uma mensagem informando se o ano é bissexto ou não.

Exercício 4: Calculadora básica
● Criar uma calculadora simples onde o usuário pode inserir dois números e, ao
pressionar um botão, o resultado das operações de adição, subtração, multiplicação

e divisão será exibido.
● Crie dois campos de entrada para o usuário inserir os dois números.
● Crie um botão que, ao ser pressionado, realiza as operações matemáticas e exibe
os resultados no Label.

Exercício 5: Manipular uma lista de 4 números
● Criar uma interface onde o usuário insere 4 números. Depois, ao pressionar um
botão, a aplicação:
1. Mostra quantas vezes o número 9 aparece na lista.
2. Informa a posição do primeiro valor 3 na lista.
3. Exibe todos os números pares da lista.
● Crie quatro campos de entrada para os números.
● Crie um botão que, ao ser pressionado, executa as seguintes operações:
○ Conta quantas vezes o número 9 aparece.
○ Encontra a posição do primeiro número 3.
○ Exibe os números pares.'''