class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Óla {id(self)}'

if __name__ == '__main__':
    Eduarda = Pessoa(nome='Eduarda')
    Lucianna = Pessoa(Eduarda, nome = 'Lucianna')
    print(Pessoa.cumprimentar('Lucianna'))
    print(id(Lucianna))
    print(Lucianna.cumprimentar())
    print(Lucianna.idade)
    for filho in Lucianna.filhos:
        print(filho.nome)