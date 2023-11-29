from tkinter import *           #######  UTILIZANDO PYTHON 3.11.0
from tkinter import ttk         #######  UTILIZANDO MYSQL-CONNECTOR 2. 
from tkinter import messagebox  #######  MYSQL 8.0.34
import mysql.connector          #######  MYSQL.CONNECTOR 2.2.9
                                #######  MYSQL-CONNECTOR-PYTHON 8.2  


app= Tk()                   #Function Tk utilizada para configurar algumas info do conteúdo.
#app.state('zoomed')         #Utilizada para abrir em FullScreen.
app.config(bg='#F5DEB3')
app.geometry("1280x665")

#-------------------Função do Botão---------------- 

#Atribuindo o nome das variáveis originais do código com o parâmetro self para pegar os valores do input atual.
class CadastroPacienteApp:
    def __init__(self,nome_do_paciente, cpf, rg, data_de_nascimento,data_de_entrada, data_de_saida, sexo, n_plano, titular, etnia, tp_sanguineo, obs):
        self.app = app  
        self.nome_do_paciente = nome_do_paciente
        self.cpf = cpf
        self.rg = rg
        self.data_de_nascimento = data_de_nascimento
        self.data_de_entrada = data_de_entrada
        self.data_de_saida = data_de_saida
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.n_plano = n_plano
        self.titular = titular
        self.etnia = etnia
        self.tp_sanguineo = tp_sanguineo
        self.obs = obs

                                                        
def pd():   # Atribuindo função de cadastro obritagóriamente com as 3 informações principais preenchidas para rodas o insert.
    if e1.get() == "" or e2.get() =="" or e7.get()=="": #É obrigatório preenchimento dos 3 campos para cadastrar, independentemente se o campo for preenchido com 000, xxx ou null.
        messagebox.showerror("Erro", "Preencha todos os campos")
    else:                                               #Se a condição primária for falsa o insert será rodado.
        variaveis = (nome_do_paciente.get() ,          
        cpf.get(),                                      #Atibuindo as variaveis originais com .get() para pegar as infos dos campos atuais.
        rg.get(), 
        data_de_nascimento.get(), 
        data_de_entrada.get(), 
        data_de_saida.get(), 
        sexo.get(),
        estado_civil.get(), 
        n_plano.get(),
        titular.get(),
        etnia.get(),
        tp_sanguineo.get(),
        obs.get())
        con = mysql.connector.connect(host="localhost", user = "root", password = "root", database = "cadastro_paciente")#Caso a primeira condição nao seja respeita cairá no else, inserindo os dados em tb no mysql.
        my_cursor = con.cursor()
        my_cursor.execute("INSERT INTO paciente VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )", (variaveis))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("Sucesso", "Paciente Cadastrado com Sucesso")


#-------------Função Query SQL----------:

#Função que representa a tb do banco em tempo real
def fetch_data():               
    con = mysql.connector.connect(host="localhost", user = "root", password = "root", database = "cadastro_paciente")#Caso a primeira condição nao seja respeita cairá no else, inserindo os dados em tb no mysql.
    my_cursor = con.cursor()
    my_cursor.execute('SELECT * FROM paciente')             #Executando conexão com o banco e rodando um Select *
    rows = my_cursor.fetchall()                             #Atribuindo a query do select à uma variável rows (linhas)
    if len(rows) != 0:                                      #Se o comprimento total de row for diferente de 0 executará a fetch_data() "com filhos" da tabalea.
        table.delete(* table.get_children())
        for items in rows:                                  #Para items nesse total de linhas 
            table.insert('', END, values=items)             #Para cada Linha que for diferente de 0 ele roda a Query e ao final commita e fecha a conexão
        con.commit()
    con.close()

#------------Função get_data-------------

#Tem o intuito onclick, na tabela, aparecer nos inputs os dados cadastrados anteriormente
def get_data(event=''):                                     #Foi setado os index valores anteriormente como items
    cursor_row = table.focus()                              #Assim recebendo em formato de lista, consequentemente com um index, sendo selecionados aqui.
    data = table.item(cursor_row)
    row = data['values']
    
    nome_do_paciente.set(row[0])
    cpf.set(row[1])
    rg.set(row[2])
    data_de_nascimento.set(row[3])
    data_de_entrada.set(row[4])
    data_de_saida.set(row[5])
    sexo.set(row[6])
    estado_civil.set(row[7])
    n_plano.set(row[8])
    titular.set(row[9])
    etnia.set(row[10])
    tp_sanguineo.set(row[11])
    obs.set(row[12])


#Função Para aparecer as informações do paciente completas na Tabela ao lado
def completo():
    txt_frme.insert(END, 'Nome do Paciente:\t\t\t\t\t'+nome_do_paciente.get()+ '\n')
    txt_frme.insert(END, 'CPF:\t\t\t\t\t'+cpf.get()+'\n')
    txt_frme.insert(END, 'RG:\t\t\t\t\t'+rg.get()+'\n')
    txt_frme.insert(END, 'Data de Nascimento:\t\t\t\t\t'+data_de_nascimento.get()+'\n')
    txt_frme.insert(END, 'Data de Entrada:\t\t\t\t\t'+data_de_entrada.get()+'\n')
    txt_frme.insert(END, 'Data de Saída:\t\t\t\t\t'+data_de_saida.get()+'\n')
    txt_frme.insert(END, 'Sexo:\t\t\t\t\t'+sexo.get()+'\n')
    txt_frme.insert(END, 'Estado Civil:\t\t\t\t\t'+estado_civil.get()+'\n')
    txt_frme.insert(END, 'N° do Plano:\t\t\t\t\t'+n_plano.get()+'\n')
    txt_frme.insert(END, 'Titular:\t\t\t\t\t'+titular.get()+'\n')
    txt_frme.insert(END, 'Etnia:\t\t\t\t\t'+etnia.get()+'\n')
    txt_frme.insert(END, 'Tipo Sanguineo:\t\t\t\t\t'+tp_sanguineo.get()+'\n')
    txt_frme.insert(END, 'Observações:\t\t\t\t\t'+obs.get()+'\n')

#-----------Função Delete----------
def deletar():
    con = mysql.connector.connect(host="localhost", user = "root", password = "root", database = "cadastro_paciente")
    my_cursor = con.cursor()
    querry = ('DELETE FROM paciente WHERE cpf=%s')  #Query para deletar o cadastro pelo CPF;
    value = [(cpf.get())]                           #Setando os dados retornados como listas;
    
    my_cursor.execute(querry, value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Excluído', 'Dados do Paciente foram Deletados')
    

#-------------Função Limpar---------------
def limpar():
    nome_do_paciente.set('')
    cpf.set('')
    rg.set('')
    data_de_nascimento.set('')
    data_de_entrada.set('')
    data_de_saida.set('')
    sexo.set('')
    estado_civil.set('')
    n_plano.set('')
    titular.set('')
    etnia.set('')
    tp_sanguineo.set('')
    obs.set('')
    
    txt_frme.delete(1.0, END)

#-------------Função para sair do App----------
def sair():
    confirm = messagebox.askyesno('Confirmação', 'Tem certeza que quer sair ?')
    if confirm>0:
        app.destroy()
        return
#-----------HEADER--------
Label(app, text="Sistema de Cadastro de Pacientes", font='impack 29 bold', bg='#FAFAD2', fg='black' ).pack(fill=X)   #Setando uma caixa para Título, com fonte, bg, fg com .pack para "executar" a label 


#----------FRAME1---------
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
obs = StringVar()


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
lip2 = LabelFrame(frame1, text="Informações Completas", font="arial 12 bold", bd=10, bg='#F0FFF0')
lip2.place(x=710, y=4, width=530,  height=275)


#Text box para Observações.
txt_frme = Text(lip2,font ='arial 9 bold', width=40, height=30, bg='#F0FFF0' )
txt_frme.pack(fill=BOTH)


#FRAME 2
frame2 = Frame(app, bd=12, relief=RIDGE )
frame2.place(x=5, y=370, width=1270, height=250)


#------------Salvar Cadastro------------
s_btn = Button(app, text="Salvar Cadastro", font='arial 11 bold', bg='#228B22', fg='#000009', bd=5, cursor='hand2', command=pd)
s_btn.place(x=10, y=622, width=270, height=40)


#------------Dados do Paciente------------
dp_btn = Button(app, text="Observações sobre Paciente", font='arial 11 bold', bg='#DAA520', fg='#000009', bd=5, cursor='hand2', command=completo)
dp_btn.place(x=290, y=622, width=270, height=40)


#------------BOTÃO LIMPAR------------
d_btn = Button(app, text="Limpar Campos", font='arial 11 bold', bg='#4682B4', fg='#000009', bd=5, cursor='hand2', command=limpar)
d_btn.place(x=570, y=622, width=260, height=40)


#------------BOTÃO EXCLUIR------------
d_btn = Button(app, text="Excluir", font='arial 11 bold', bg='#FF6347', fg='#000009', bd=5, cursor='hand2', command=deletar)
d_btn.place(x=837, y=622, width=240, height=40)


#------------BOTÃO SAIR------------
d_btn = Button(app, text="Sair", font='arial 11 bold', bg='brown', fg='#000009', bd=5, cursor='hand2', command=sair)
d_btn.place(x=1085, y=622, width=190, height=40)


#ScrollBar para Dados Frame2.
scroll_x = ttk.Scrollbar(frame2, orient=HORIZONTAL)
scroll_x.pack(side='bottom', fill='x')
scroll_y = ttk.Scrollbar(frame2, orient=VERTICAL)
scroll_y.pack(side='right', fill='y')

table = ttk.Treeview(frame2, columns=('nop', 'cpf', 'rg', 'ddn', 'dde', 'dds', 'sx', 'ec', 'ndp', 'et','tit', 'ts', 'obs'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x = ttk.Scrollbar(command=table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)


#Heading para Dados do paciente, Colocando o nome das variáveis dos inputs com as respectivas lables
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


#Comprimento das colunas da Tabela.
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


table.bind('<ButtonRelease-1>', get_data)
fetch_data()                #Sempre executa a Query de Select * para busca quando hover qualquer alteração no banco na sessão.
mainloop()                  #Executa o código.
