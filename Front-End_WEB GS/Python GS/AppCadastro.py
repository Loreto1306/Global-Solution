from tkinter import *
app= Tk()                   #Function Tk utilizada para configurar algumas info do conteúdo.
#app.state('zoomed')         #Utilizada para abrir em FullScreen.
app.config(bg='#F5DEB3')
app.geometry("1320x665")

#HEADER

Label(app, text="Sistema de Cadastro de Pacientes", font='impack 29 bold', bg='#FAFAD2', fg='black' ).pack(fill=X)   #Setando uma caixa para Título, com fonte, bg, fg com .pack para "executar" a label 

#FRAME1

frame1 = Frame(app, bd=15, relief=RIDGE )
frame1.place(x=20, y=60, width=1280, height=310)

#Label para Informações do Paciente.

lip1 = LabelFrame(frame1, text="Informações do Paciente", font="arial 12 bold", bd=10, bg='#FFDAB9')
lip1.place(x=8, y=4, width=700,  height=280)

#Label para informações do Paciente.

Label(lip1, text='Nome do Paciente:', bg='#FFFFE0', borderwidth=1).place(x=7, y=10)
Label(lip1, text='CPF:', bg='#FFFFE0', borderwidth=1).place(x=350, y=10)
Label(lip1, text='Registro Geral (RG):', bg='#FFFFE0', borderwidth=1).place(x=7, y=45)
Label(lip1, text='Data de Nascimento:', bg='#FFFFE0', borderwidth=1).place(x=350, y=45)
Label(lip1, text='Data de entrada:', bg='#FFFFE0', borderwidth=1).place(x=7, y=80)
Label(lip1, text='Data de Saída:', bg='#FFFFE0', borderwidth=1).place(x=350, y=80)
Label(lip1, text='Sexo:', bg='#FFFFE0', borderwidth=1).place(x=7, y=115)
Label(lip1, text='Estado Civil:', bg='#FFFFE0', borderwidth=1).place(x=350, y=115)
Label(lip1, text='N° Plano:', bg='#FFFFE0', borderwidth=1).place(x=7, y=150)
Label(lip1, text='Titular:', bg='#FFFFE0', borderwidth=1).place(x=350, y=150)
Label(lip1, text='Etnia:', bg='#FFFFE0', borderwidth=1).place(x=7, y=185)
Label(lip1, text='Tipo Sanguineo:', bg='#FFFFE0', borderwidth=1).place(x=7, y=220)
Label(lip1, text='Obervações:', bg='#FFFFE0', borderwidth=1).place(x=350, y=185)

#Campos para as Labels.

e1 = Entry(lip1, bd=4)
e1.place(x=130, y=7, width=200)

e2 = Entry(lip1, bd=4)
e2.place(x=130, y=41, width=200)

e3 = Entry(lip1, bd=4)
e3.place(x=130, y=78, width=200)

e4 = Entry(lip1, bd=4)
e4.place(x=130, y=113, width=200)

e5 = Entry(lip1, bd=4)
e5.place(x=130, y=148, width=200)

e5 = Entry(lip1, bd=4)
e5.place(x=130, y=183, width=200)

e6 = Entry(lip1, bd=4)
e6.place(x=130, y=218, width=200)

e7 = Entry(lip1, bd=4)
e7.place(x=470, y=7, width=200)

e8 = Entry(lip1, bd=4)
e8.place(x=470, y=41, width=200)

e9 = Entry(lip1, bd=4)
e9.place(x=470, y=78, width=200)

e10 = Entry(lip1, bd=4)
e10.place(x=470, y=113, width=200)

e11= Entry(lip1, bd=4)
e11.place(x=470, y=148, width=200)

e12 = Entry(lip1, bd=4)
e12.place(x=470, y=183, width=200, height=60)

#Label para Observações/Histórico sobre o paciente.
lip2 = LabelFrame(frame1, text="Observações sobre o Paciente", font="arial 12 bold", bd=10, bg='#F0FFF0')
lip2.place(x=710, y=4, width=540,  height=275)

#Text box para Observações.

txt_frme = Text(lip2,font ='arial 9 bold', width=40, height=30, bg='#F0FFF0' )
txt_frme.pack(fill=BOTH)

#FRAME 2

frame2 = Frame(app, bd=12, relief=RIDGE )
frame2.place(x=20, y=370, width=1280, height=250)


#Salvar Cadastro

s_btn = Button(app, text="Salvar Cadastro", font='arial 11 bold', bg='#228B22', fg='#000009', bd=5, cursor='hand2')
s_btn.place(x=20, y=622, width=270, height=40)

#Dados do Paciente

dp_btn = Button(app, text="Observações sobre Paciente", font='arial 11 bold', bg='#DAA520', fg='#000009', bd=5, cursor='hand2')
dp_btn.place(x=300, y=622, width=270, height=40)

#BOTÃO LIMPAR

d_btn = Button(app, text="Limpar Campos", font='arial 11 bold', bg='#4682B4', fg='#000009', bd=5, cursor='hand2')
d_btn.place(x=580, y=622, width=260, height=40)

#BOTÃO EXCLUIR

d_btn = Button(app, text="Excluir", font='arial 11 bold', bg='#FF6347', fg='#000009', bd=5, cursor='hand2')
d_btn.place(x=850, y=622, width=240, height=40)

#BOTÃO SAIR

d_btn = Button(app, text="Sair", font='arial 11 bold', bg='brown', fg='#000009', bd=5, cursor='hand2')
d_btn.place(x=1100, y=622, width=200, height=40)

mainloop()                  #Executa o código.
