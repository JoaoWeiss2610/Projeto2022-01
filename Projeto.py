from cgitb import text
from distutils.cmd import Command
import tkinter as tk
import csv

# -----------JANELA PRINCIPAL-----------

janela = tk.Tk()
janela.geometry("300x200")
janela.title('Janela principal')

############################################################

# -----------LISTAS-----------

lista_Nome = []
lista_Email = []
lista_Numero = []

############################################################

# -----------DEF PARA DAR GET NA ENTRADA DO NOME,EMAIL E NÚMERO-----------

def addNome():
  global caixaNome
  lista_Nome.append(str(caixaNome.get()))

def addEmail():
  global caixaEmail
  lista_Email.append(str(caixaEmail.get()))

def addNumb():
  global caixaNumb
  lista_Numero.append(str(caixaNumb.get()))

def SalvarDados():
  with open("C:\\Users\\USER\\Desktop\\ProjetoSENAI2022\\arquivos.csv.csv","w") as arquivo:
    leitor = csv.writer(arquivo, delimiter=',')
    leitor.writerow(lista_Email)
    leitor.writerow(lista_Email)
    leitor.writerow(lista_Numero)

############################################################

  # -----------JANELA DO CADASTRAMENTO DE USUÁRIO-----------

def abrir_janela():
  janela2 = tk.Toplevel()
  janela2.geometry("400x200")
  janela2.title('Cadastramento de usuário')

  global caixaNome
  caixaNome = tk.Entry(janela2)
  caixaNome.place(x=100, y=30)
  label_nome = tk.Label(janela2, text= "Nome: ")
  label_nome.place(x=50, y=30)

  global caixaEmail
  caixaEmail = tk.Entry(janela2)
  caixaEmail.place(x= 100, y= 60)
  label_email = tk.Label(janela2, text= "E-mail: ")
  label_email.place(x=50, y=60)

  global caixaNumb
  caixaNumb = tk.Entry(janela2)
  caixaNumb.place(x=100, y=90)
  label_numero = tk.Label(janela2, text= "Número: ")
  label_numero.place(x=40, y=90)

  btn_salvar = tk.Button(janela2, text="Salvar", command=lambda: [addNome(), addEmail(), addNumb(), SalvarDados()])
  btn_salvar.place(x=100, y=130)


botao01 = tk.Button(janela, text= 'Cadastrar um usuário', command=abrir_janela)
botao01.place(x=70,y=50)


############################################################
# -----------JANELA PARA VISUALIZAR OS USUÁRIOS CADASTRADOS-----------


def abrir_janela3():
  global janela3
  janela3 = tk.Toplevel()
  janela3.geometry("600x400")
  janela3.title('Visualizador de usuário')

  label_Nom = tk.Label(janela3, text="Nome")
  label_Nom.place(x=110, y=20)
  global ListaNomes
  ListaNomes = tk.Listbox(janela3)
  ListaNomes.place(x=70, y=40 )
  

  label_Email = tk.Label(janela3, text="E-mail")
  label_Email.place(x=280, y=20)
  global ListaEmail
  ListaEmail = tk.Listbox(janela3)
  ListaEmail.place(x=240, y=40)

  label_Numb = tk.Label(janela3, text="Número")
  label_Numb.place(x=450, y=20)
  global ListaNum
  ListaNum = tk.Listbox(janela3)
  ListaNum.place(x=410, y=40 )

  for Nomes in lista_Nome:
    ListaNomes.insert(0, Nomes)

  for Email in lista_Email:
    ListaEmail.insert(0, Email)

  for Numb in lista_Numero:
    ListaNum.insert(0, Numb)

  janela3.mainloop()


botao02 = tk.Button(janela, text= 'Visualizar os usuários', command=abrir_janela3)
botao02.place(x=70, y=100)

############################################################


janela.mainloop()