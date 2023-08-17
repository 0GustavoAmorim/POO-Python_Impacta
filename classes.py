class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.editora = 'Nome da editora'

    def identidade(self):
        return (f'Sou o livro {self.nome}, e estou salvo'
                f'no endereço de mamória: {id(self)}')

if __name__ == '__main__':
    livro_1 = Livro('A Revolução dos Bichos', 'George Orwell');
    livro_2 = Livro('O Senhor dos Anéis', 'J. R. R. Tolkien');


    print(livro_1.nome)
    print(livro_1.autor)

    # print('Livro 1:', vars(livro_1))
    # print('Livro 2:', vars(livro_2))
