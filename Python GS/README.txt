Autor: Artur Rodrigues Loreto ;
RM: 552851 ;
Curso: Enhenharia de Software, 1S23.

Dando início ao Documentação Projeto HaVi, DANELISE.

O projeto HaVi, da DANELISE, consiste em um ornganizador, controlador e armazém para fluxo de dados, com possibilidade de integração entre as filias ou não.
    
    Os Softwares utilizados para preparação do ambiente, programação e banco são, respectivamente:
        -  Visual Studio Code.
        -  Python (v 3.11.0);
        -  MySQL WorkBench (v 8.0.34);
        -  MySQL Server (v 8.0.34);
        


No projeto todo é utilizado as seguinte bibliotecas e módulos:
    
    -Biblioteca: 
        -  Tkinter (Nativo): Uma biblioteca que possibilita a criação de interfaces para aplicações python.
        -  mysql.connector (v 2.2.9): Uma biblioteca que possibilita a conexão do Banco de Dados Mysql com a aplicação.
        -  mysql-connector-python (v 8.2)

    -Módulos:
        -  tkk : Um módulo para Widgets do Tkinter, novos features, neste projeto, foi usado apenas a função Scrollbar() e a Treeview()"Agrupamento dos dados".
        -  messagebox: Um módulo para Pop-Ups, com informações contidas neles, utilizando as funções showerror(), showinfo() e askyesno().  
    


O código começa com importando todos as informações relatadas antes.


Foi setado o nome da aplicação, "tk()", como "App", juntamente com o Background e a janela fixa ao abrir a aplicação.
    
    Atribuí uma classe CadastroPacienteApp e dentro:    
        -  Foi criado uma função "__init__" com os parametros, self (Para pegar o valor das variáveis na Current session), juntamente com as variáveis em questão.
        -  Na função foi atribuido primeiramente o "self.app = app", com o intuito de relatar ao Software que os valores inputados são da sessão, trazendo os valores escritos na hora do cadastro.
        -  Foi feito isso com todas as variáveis de Input do código.


Foi criado a Função pd():

    Esta função tem como objetivo efetuar o Cadastro do Paciente em questão.

        Com a condicional " if e1.get() == "" or e2.get() =="" or e7.get()=="" ", o código passa em verificaçao se todos os campos obrigatórios estão preenchidos, nesse caso, o Nome do Paciente, CPF e RG.
            -  Caso a condicional seja respeitada o módulo messagebox exibirá um popup com erro.
    

            Caso a condicional não seja respeitada foi atribuido um else com todas as variáveis concatenadas com a função get(), servindo para pegar o valor dos inputs.
                -  Foi criado uma variável de nome "variaveis", para armazenar todos os gets e facilitar a query de Insert.
                -  Após pegar todas os valores é feito a tentativa de conexão com o DB em questão, com a função da biblioteca mysql.connector.connect().
                -  Caso a conexão obtenha êxito executará a query em SQL "INSERT INTO paciente (nome da tb) VALUES (%s)", (variaveis)"
                -  Caso esteja correto a inserscção e nao tenha outra contestação o con.commit() irá enviar a informação em si no DB.
                -  Após o cadastro ser efetuado a sessão encerrará com o con.close() e uma mensagem de Sucesso será exibida.
