class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Óla, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatio():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos} '


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    Eduarda = Mutante(nome='Eduarda')
    Lucianna = Homem(Eduarda, nome = 'Lucianna')
    print(Pessoa.cumprimentar(Lucianna))
    print(id(Lucianna))
    print(Lucianna.cumprimentar())
    print(Lucianna.idade)
    for filho in Lucianna.filhos:
        print(filho.nome)
    Lucianna.sobrenome = 'Freitas'
    del Lucianna.filhos
    Lucianna.olhos = 1
    del Lucianna.olhos
    print(Lucianna.__dict__)
    print(Eduarda.__dict__)
    print(Pessoa.olhos)
    print(Lucianna.olhos)
    print(Eduarda.olhos)
    print(id(Pessoa.olhos), id(Lucianna.olhos), id (Eduarda.olhos))
    print(Pessoa.metodo_estatio(), Lucianna.metodo_estatio())
    print(Pessoa.nome_e_atributos_de_classe(), Lucianna.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Eduarda, Pessoa))
    print(isinstance(Eduarda, Homem))
    print(Eduarda.olhos)
    print(Lucianna.cumprimentar())
    print(Eduarda.cumprimentar())
