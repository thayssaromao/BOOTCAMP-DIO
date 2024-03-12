#.lower = all letters are lower case
#.upper = all letters are upper case
#.title = capital letter for the first letter of every word
#.capitalize = capital letter for the first letter of only the first word
#.strip() removes any spaces on either side of the word.
#.lstrip() = remover os espaços em branco do inicio da string
#.rstrip() = remover os espaços em branco do fim da string
#.center('10', '#') centralizar uma string dentro de uma largura especificada. Ele preenche os espaços em branco em ambos os lados da string para alcançar a largura desejada, colocando a string no centro.
#"-".join(list) =c oncatenar os elementos de um iterável (como uma lista, tupla, conjunto, ou até mesmo uma string) em uma única string, utilizando outra string como separador entre os elementos.
profissao = "  assistente administrativo"
idade = 19
nome = "thayssa"

#dicionarios -> chaves e valores
dicionario = {"nome": "thayssa", "idade": "19", "profissao": "assistente administrativo"}

print("olá, meu nome é %s tenho %d anos e trabalho como %s" %(nome.title(), idade, profissao.strip().title() ))
print(f"olá, meu nome é {nome.title()} tenho {idade} anos e trabalho como {profissao.strip().title()}") 
print("olá, meu nome é {nome} tenho {idade} anos e trabalho como {profissao}".format(**dicionario))

#fatiamento de strings
print()
string = "Recebidinhos das bonecas"
print(string[0:])
print(string[13:])
print(string[::-1])
print(string[0::2])