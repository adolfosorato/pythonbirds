class Pessoa:
    olhos = 2

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
