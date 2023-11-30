Autor: Artur Rodrigues Loreto ;
RM: 552851 ;
Curso: Enhenharia de Software, 1S23.

Dando início ao Documentação Projeto HaVi, DANELISE.

Detalhes do Projeto:


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
    

Instruções de Uso:

    -É recomendado utilizar o programa em modo janela, setado para monitores de no mínimo 1280x1080;
    -É recomendado após utilização do programa utilizar o botão "Sair" para encerrar sua sessão;

Dependências e informações relevantes:

    -O progrma é dependente como citado acima à presença de Python 3.11.0 uma conexão à internet e um Banco de Dados MYSQL com servidor online.
    
    -O programa é rápido e intuitivo, primiordial diminuição do tempo de espera na hora de cadastrar um paciente.

    -O programa é executado via .exe não necessitando o conhecimento prévio do usuário em programação.




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

Foi criado a função fetch_data():
    
    Esta funçã tem como objetivo de pegar as informações do banco e representa-las no quadro da aplicação em tempo real.

            É setado no inicio da função a conexão com o banco de dados.
            Com a conexão estabelecida, é executado a query (SELECT * FROM paciente).
            É atribuído também à uma variável rows a função fetchall(), com a função de localizar todas as linhas dessa tabela.

                Com a condicional len(rows) != 0 o código verifica a quantidade se a quantidade de linhas for diferente de 0 ela executará:
                    - É concatenado a variável table (Setada depois no código com informações das variáveis de input) e a function delete, resultando os id dessa query (utilizando depois da funcão deletar).
                
                    - Com a condicional, para cada item nessas rows:
                        Irá inserir os respctivos dados na tabela para visualização apenas.
                
                    Após é utilizado a função con.commit() para commitar 

                Após é utilizado a função con.close() para encerrar a sessão de consulta.


Foi criada a função get_data():

    Esta função tem como objetivo de pegar as informações onclick na tabela que representa a o banco "table" e adicionar os valores no campos de input:
        
        Primeiro é setado a função concatenando table.focus() com o intuito de trazer a forma literal da info.
        
        Após é setado uma variável "row" com os valor "values" do dicionario "data".

        Após isso é setado a os respectivos index de input de informações com as valores dessa informações em si.


Foi criada a função completo():

    Esta função tem como objetivo de exibir os valores cadastrados onclick no button "Observações Do Paciente", exibindo elas no canto superior direito da tela, no quadro definido como "Observações do Paciente"
    
        É utilizado a variável atribuida no código "txt_frame" com a função Insert() pegando os valores e exibindo eles da forma desejada.


Foi criada a função deletar():

    Esta função tem como objetivo deletar a registro do paciente.

        Primeiro é atrui