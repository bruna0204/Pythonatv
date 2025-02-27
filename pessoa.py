from datetime import datetime, date

class Pessoa:
    def __init__(self, nome, data_nascimento,cpf,cidade, salario=1518,  trabalhando=True,estudando=True, dirigindo=True): #int começa o objeto # self se cria
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.dirigindo = dirigindo
        self.cidade = cidade
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = salario

    def apresentar(self):
        print("**************")
        print(f'Ola sou {self.nome}\n'
               f' minha data de nascimento é {self.data_nascimento}\n'
              f' seu cpf é {self.cpf}\n'
              f' cidade: {self.cidade}\n'
              f' Idade: {self.idade()}\n'
              )

        if self.trabalhando:
            print(f'Trabalhando')
        else:
            print(f'Nao trabalhando')

        if self.dirigindo:
            print(f'dirige')
        else:
            print(f'Nao dirige')

        if self.estudando:
            print(f'Estudando')
        else:
            print(f'Nao estudando')


    def estudar(self):
        if self.trabalhando and self.estudando:
            aumento = (self.salario + 100 )

            print(f'Voce teve um aumento pois trabalha e estuda\n salario antigo {self.salario}\n'
                  f'salario novo {aumento}')
        elif self.estudando:
            print('Voce estuda')

        else:
            print('Não esta estudando')




    def idade(self):
        dataFormatada = datetime.strptime(self.data_nascimento, '%d/%m/%Y')
        dataAtual = datetime.today()
        idadeAtual = dataAtual.year - dataFormatada.year
        print(f'Idade: {idadeAtual}')


    def dirigir(self):
        if self.dirigindo:
            print(f'Voce dirige, tem carteira de motorista')
        else:
            print('Voce não dirige')



    def trabalhar(self):
        if self.trabalhando:
            print(f'Voce esta trabalhando')
            print(f'salario: {self.salario}')


        else:
            print('Não esta trabalhando')

        print('-' * 28)



p1 = Pessoa('Bruna', '02/04/2008', '999', 'guararapes', dirigindo=True, trabalhando= False)
p2 = Pessoa('Laura', '16/02/2008', '888', 'Rio preto',   dirigindo=True, trabalhando= False)
p3 = Pessoa('Julia', '10/10/2007', '777','São Paulo', dirigindo=True, trabalhando= True)


class Adolecente(Pessoa): #herda a clase pessoa
    def __init__(self, nome, data_nascimento,cpf,cidade, estudando=True, trabalhando=False,dirigindo=False):
        super().__init__(nome, data_nascimento,cpf,cidade, estudando, trabalhando, dirigindo)
        self.jogando = True
        self.celular = True
        self.dormindo = False

    def apresentacao(self):
        print(f'Ola sou {self.nome}'
              f' minha data de nascimento é {self.data_nascimento}'
              f' seu codigo é {self.cpf}')
        if self.jogando:
            print(f'estou jogando')

        else:
            print(f'Não estou jogando')

        if self.celular:
            print(f'estou mexendo no celular')
        else:
            print(f'Não estou mexendo no celular')

        if self.dormindo:
            print(f'estou dormindo')
        else:
            print(f'não estou dormindo')

    def jogar(self):
        if self.jogando and self.celular:
            print(f'O adolecente esta jogando um jogo no celular')
            self.dormindo = False
            self.estudando = False

        elif self.jogando:
            print('O adolecente esta jogando')

        else:
            print('o adolecente não esta jogando')



    def mexendo_celular(self):
        if self.celular:
            print(f'ele esta no celular')

        elif self.celular and self.estudando:
            print('ele esta estudando no celular')

        else:
            print('não esta mexendo no celular')


    def dormir(self):
        if self.estudando:
            print('Ele não esta dormindo')

        else:
            print('ele esta  dormindo')



    def acordar(self):
        if self.dormindo:
            print('ele esta acordando')
            self.estudando = True

        else:
            print('ele ja esta acordado')

        print('-' * 28)



a1 = Adolecente('lili', '02/04/2008', 'ags', 'guararapes')



a2 = Adolecente('Gui', '02/04/2008', 'ags', 'São paulo')





a3 = Adolecente('Bruna', '02/04/2008', 'ags','Guarulhos')











