
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


app= Tk()                   #Function Tk utilizada para configurar algumas info do conteúdo.
#app.state('zoomed')         #Utilizada para abrir em FullScreen.
app.config(bg='#F5DEB3')
app.geometry("1280x665")

#-------------------Função do Botão
def pd():
    if e1.get() == "" or e2.get() =="" or e7.get()=="": #É obrigatório preenchimento dos 3 campos para cadastrar, independentemente se o campo for preenchido com 000, xxx ou null.
        messagebox.showerror("Erro", "Preencha todos os campos")
    else:
        con = mysql.connector.connect(host="localhost", username = "root", password = "root", database = "cadastro_hapvida")#Caso a primeira condição nao seja respeita cairá no else, inserindo os dados em tb no mysql.
        my_cursor = con.cursor()
        my_cursor.execute("insert into paciente value(s%, s%, s%, s%, s%, s%, s%, s%, s%, s%, s%, s%, s%)", (
            nome_do_paciente.get(),
            cpf.get(),
            rg.get(), 
            data_de_nascimento.get(), 
            data_de_entrada.get(), 
            data_de_saida.get(), 
            sexo.get(),
            estado_civil.get(), 
            n_plano.get(),
            titular.get(),
            etnia.get(),
            obs.get()
        ))
        con.commit()
        con.close()
        messagebox.showinfo("Sucesso", "Paciente Cadastrado com Sucesso")

def fetch_data():
    con = mysql.connector.connect(host="localhost", username = "root", password = "root", database = "mydata")#Caso a primeira condição nao seja respeita cairá no else, inserindo os dados em tb no mysql.
    my_cursor = con.cursor()
    my_cursor.execute('select * from Hapvida')
    rows = my_cursor.fetchall()
    #if len(rows)!=0:
        #table.

#HEADER
Label(app, text="Sistema de Cadastro de Pacientes", font='impack 29 bold', bg='#FAFAD2', fg='black' ).pack(fill=X)   #Setando uma caixa para Título, com fonte, bg, fg com .pack para "executar" a label 


#FRAME1
frame1 = Frame(app, bd=15, relief=RIDGE )
frame1.place(x=5, y=60, width=1270, height=310) 


#Label para Informações do Paciente.
lip1 = LabelFrame(frame1, text="Informações do Paciente", font="arial 12 bold", bd=10, bg='#bdbebd')
lip1.place(x=8, y=4, width=700,  height=280)


#Label para informações do Paciente.
Label(lip1, text='Nome do Paciente:', bg='#bdbebd', borderwidth=1).place(x=7, y=10)
Label(lip1, text='CPF:', bg='#bdbebd', borderwidth=1).place(x=350, y=10)
Label(lip1, text='Registro Geral (RG):', bg='#bdbebd', borderwidth=1).place(x=7, y=45)
Label(lip1, text='Data de Nascimento:', bg='#bdbebd', borderwidth=1).place(x=350, y=45)
Label(lip1, text='Data de entrada:', bg='#bdbebd', borderwidth=1).place(x=7, y=80)
Label(lip1, text='Data de Saída:', bg='#bdbebd', borderwidth=1).place(x=350, y=80)
Label(lip1, text='Sexo:', bg='#bdbebd', borderwidth=1).place(x=7, y=115)
Label(lip1, text='Estado Civil:', bg='#bdbebd', borderwidth=1).place(x=350, y=115)
Label(lip1, text='N° Plano:', bg='#bdbebd', borderwidth=1).place(x=7, y=150)
Label(lip1, text='Titular:', bg='#bdbebd', borderwidth=1).place(x=350, y=150)
Label(lip1, text='Etnia:', bg='#bdbebd', borderwidth=1).place(x=7, y=185)
Label(lip1, text='Tipo Sanguineo:', bg='#bdbebd', borderwidth=1).place(x=7, y=220)
Label(lip1, text='Obervações:', bg='#bdbebd', borderwidth=1).place(x=350, y=185)


#Variaveis para os campos.
nome_do_paciente = StringVar()
cpf = StringVar()
rg = StringVar()
data_de_nascimento = StringVar()
data_de_entrada = StringVar()
data_de_saida = StringVar()
sexo = StringVar()
estado_civil = StringVar()
n_plano = StringVar()
titular = StringVar()
etnia = StringVar()
tp_sanguineo = StringVar()
obs = StringVar

#Campos para as Labels.
e1 = Entry(lip1, bd=4, textvariable=nome_do_paciente)
e1.place(x=130, y=7, width=200)

e2 = Entry(lip1, bd=4, textvariable=rg)
e2.place(x=130, y=41, width=200)

e3 = Entry(lip1, bd=4, textvariable=data_de_entrada)
e3.place(x=130, y=78, width=200)

e4 = Entry(lip1, bd=4, textvariable=sexo)
e4.place(x=130, y=113, width=200)

e5 = Entry(lip1, bd=4, textvariable=n_plano)
e5.place(x=130, y=148, width=200)

e5 = Entry(lip1, bd=4, textvariable=etnia)
e5.place(x=130, y=183, width=200)

e6 = Entry(lip1, bd=4, textvariable=tp_sanguineo)
e6.place(x=130, y=218, width=200)

e7 = Entry(lip1, bd=4, textvariable=cpf)
e7.place(x=470, y=7, width=200)

e8 = Entry(lip1, bd=4, textvariable=data_de_nascimento)
e8.place(x=470, y=41, width=200)

e9 = Entry(lip1, bd=4, textvariable=data_de_saida)
e9.place(x=470, y=78, width=200)

e10 = Entry(lip1, bd=4, textvariable=estado_civil)
e10.place(x=470, y=113, width=200)

e11= Entry(lip1, bd=4, textvariable=titular)
e11.place(x=470, y=148, width=200)

e12 = Entry(lip1, bd=4, textvariable=obs)
e12.place(x=470, y=183, width=200, height=60)


#Label para Observações/Histórico sobre o paciente.
lip2 = LabelFrame(frame1, text="Completo sobre o Paciente", font="arial 12 bold", bd=10, bg='#F0FFF0')
lip2.place(x=710, y=4, width=530,  height=275)


#Text box para Observações.
txt_frme = Text(lip2,font ='arial 9 bold', width=40, height=30, bg='#F0FFF0' )
txt_frme.pack(fill=BOTH)


#FRAME 2
frame2 = Frame(app, bd=12, relief=RIDGE )
frame2.place(x=5, y=370, width=1270, height=250)


#Salvar Cadastro
s_btn = Button(app, text="Salvar Cadastro", font='arial 11 bold', bg='#228B22', fg='#000009', bd=5, cursor='hand2', command=pd)
s_btn.place(x=10, y=622, width=270, height=40)


#Dados do Paciente
dp_btn = Button(app, text="Observações sobre Paciente", font='arial 11 bold', bg='#DAA520', fg='#000009', bd=5, cursor='hand2')
dp_btn.place(x=290, y=622, width=270, height=40)


#BOTÃO LIMPAR
d_btn = Button(app, text="Limpar Campos", font='arial 11 bold', bg='#4682B4', fg='#000009', bd=5, cursor='hand2')
d_btn.place(x=570, y=622, width=260, height=40)


#BOTÃO EXCLUIR
d_btn = Button(app, text="Excluir", font='arial 11 bold', bg='#FF6347', fg='#000009', bd=5, cursor='hand2')
d_btn.place(x=837, y=622, width=240, height=40)


#BOTÃO SAIR
d_btn = Button(app, text="Sair", font='arial 11 bold', bg='brown', fg='#000009', bd=5, cursor='hand2')
d_btn.place(x=1085, y=622, width=190, height=40)


#Scroll para Dados Frame2.
scroll_x = ttk.Scrollbar(frame2, orient=HORIZONTAL)
scroll_x.pack(side='bottom', fill='x')
scroll_y = ttk.Scrollbar(frame2, orient=VERTICAL)
scroll_y.pack(side='right', fill='y')

table = ttk.Treeview(frame2, columns=('nop', 'cpf', 'rg', 'ddn', 'dde', 'dds', 'sx', 'ec', 'ndp', 'et','tit', 'ts', 'obs'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x = ttk.Scrollbar(command=table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)


#Heading para Dados do paciente
table.heading('nop', text='Nome do Paciente')
table.heading('cpf', text='CPF')
table.heading('rg', text='RG')
table.heading('ddn', text='Data de Nascimento')
table.heading('dde', text='Data de Entrada')
table.heading('dds', text='Data de Saída')
table.heading('sx', text='Sexo')
table.heading('ec', text='Estado Civil')
table.heading('ndp', text='N° do Plano')
table.heading('tit', text='Titular')
table.heading('et', text='Etnia')
table.heading('ts', text='Tipo Sanguíneo')
table.heading('obs', text='Observações')

table['show'] = 'headings'
table.pack(fill=BOTH, expand=1)


#Linhas da Tabela.
#-----------------------------------
table.column('nop', width=110)
table.column('cpf', width=70)
table.column('rg', width=50)
table.column('ddn', width=120)
table.column('dde', width=100)
table.column('dds', width=100)
table.column('sx', width=70)
table.column('ec', width=100)
table.column('ndp', width=100)
table.column('tit', width=80)
table.column('et', width=70)
table.column('ts', width=100)
table.column('obs', width=100)


mainloop()                  #Executa o código.
