from datetime import datetime, date

class Pessoa:
    def __init__(self, nome, data_nascimento,cpf,cidade, salario=0,  trabalhando=True,estudando=True, dirigindo=True): #int começa o objeto # self se cria
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self._dirigindo = dirigindo
        self._cidade = cidade
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def get_nome(self):
        return self.__nome

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_cpf(self):
        return self.__cpf

    def get_cidade(self):
        return self._cidade

    def get_salario(self):
        return self._salario




    def set_salario(self, salario):
        if salario >= 0:
            self._salario = salario
        else:
            print('salario invalido')





    def is_trabalhando(self):
        return self._trabalhando

    def is_estudando(self):
        return self._estudando

    def is_dirigindo(self):
        return self._dirigindo





    def set_trabalhando(self, status):
        if self._trabalhando and status:
            print('Já esta trabalhando')

        elif not self._trabalhando and not status:
            print('Que vida boa')

        elif not self._trabalhando and status:
            self._trabalhando = status
            self.set_salario(1300)
            print(f'seu salario atual: {self.get_salario()}')

        else:
            self._trabalhando = status
            self.set_salario(0)




    def set_dirigindo(self, status):
        if self._dirigindo and status:
            print('Já esta dirigindo')

        elif not self._dirigindo and not status:
            print('Essa pessoa não tem carteira de motorista')

        elif not self._dirigindo and status:
            print('ela esta indo dirigindo')
            self._dirigindo = status






    def set_estudando(self, status):
        self._estudando = status
        if self.is_trabalhando() and status:
            self.set_salario(self.get_salario() + 400)
            print(f'Seu novo salario é esse{self.get_salario()} ')


        elif not self._estudando and not status:
            print('Tomara que pelo menos trabalhe')

        elif not self._estudando and status:
            self._estudando = status
            print('vai estudar')

        else:
            self._estudando = status




    def idade(self):
        dataFormatada = datetime.strptime(self.__data_nascimento, '%d/%m/%Y')
        dataAtual = datetime.today()
        idadeAtual = dataAtual.year - dataFormatada.year
        print(f'Idade: {idadeAtual}')





    def apresentar(self):
        print(f'Ola sou {self.get_nome()}\n'
              f' minha data de nascimento é {self.get_data_nascimento()}\n'
              f' meu cpf é {self.get_cpf()}\n'
              f'minha cidade é {self.get_cidade()}\n'
              f'minha idade é {self.idade()}\n')
        print(f'Estudando: {'sim' if self.is_estudando() else 'nao'}')
        print(f'Trabalhando: {'Sim' if self.is_trabalhando() else 'Nao'}')
        print(f'Digindo: {'Sim' if self.is_dirigindo() else 'Nao'}')









p1 = Pessoa('Bruna', '02/04/2008', '999', 'guararapes', dirigindo=False, trabalhando= False, estudando=True)
p2 = Pessoa('Laura', '16/02/2008', '888', 'Rio preto',   dirigindo=True, trabalhando= True, estudando= False)
p3 = Pessoa('Julia', '10/10/2007', '777','São Paulo', dirigindo=True, trabalhando= True, estudando=True)


class Adolecente(Pessoa): #herda a clase pessoa
    def __init__(self, nome, data_nascimento,cpf,cidade, estudando=True, trabalhando=False,dirigindo=False):
        super().__init__(nome, data_nascimento,cpf,cidade, estudando, trabalhando, dirigindo)
        self._jogando = True
        self._celular = True
        self._dormindo = False



    def apresentacao(self):
        print(f'Ola sou {self.get_nome()}\n'
              f' minha data de nascimento é {self.get_data_nascimento()}\n'
              f' meu cpf é {self.get_cpf()}\n'
              f'minha cidade é {self.get_cidade()}\n')
        print(f'Estudando: {'sim' if self.is_estudando() else 'nao'}')
        print(f'Trabalhando: {'Sim' if self.is_trabalhando() else 'Nao'}')
        print(f'Jogando: {'Sim' if self.is_jogando() else 'Nao'}')
        print(f'Celular: {'Sim' if self.is_celular() else 'Nao'}')
        print(f'Dormindo: {'Sim' if self.is_celular() else 'Nao'}')



    def is_jogando(self):
        return self._jogando

    def is_celular(self):
        return self._celular

    def is_dormindo(self):
        return self._dirigindo



    def set_jogar(self, status):
        if self._jogando and status:
            print('O adolecente já esta jogando')

        elif not self._jogando and status:
            print("ele esta indo jogar")
            self._jogando = True
        elif  self._jogando and not status:
            print('O adolecente vai parar de jogar')
            self._jogando = False





    def set_dormir(self, status):
        if self._jogando :
            if not self._dormindo and status:
                print('Ele não esta dormindo pois esta jogando')
                self._jogando = False
                self._dormindo = True


            elif self._dormindo and status :
                print(f'O  adolecente esta dormindo')
        else:
             if not self._dormindo and status:
                print("ele esta indo dormir")
                dormindo = True



    def set_acordar(self, status):
        if self._dormindo and status :  #
            print('ele esta acordando')
            self._dormindo = False


        elif self.is_dormindo() and not status:
            print('ele ainda esta dormindo')


        elif not self._dormindo and status:
            print('ele já esta acordando')

        print('-' * 28)



a1 = Adolecente('lili', '02/04/2008', 'ags', 'guararapes')



a2 = Adolecente('Gui', '02/04/2008', 'ags', 'São paulo')





a3 = Adolecente('Bruna', '02/04/2008', 'ags','Guarulhos')











