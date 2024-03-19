#Uma tupla é uma sequência imutável de elementos, o que significa que uma vez criada,
# ela não pode ser modificada. Os elementos de uma tupla são indexados por números
# inteiros, semelhante a listas, e podem conter diferentes tipos de dados, incluindo
# outras tuplas. As tuplas são definidas utilizando parênteses ( ).

def chamaTupla(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    dicio = "\n".join(f"{chave.title()}: {valor}" for chave, valor in kwargs.items())

    print(f"{data_extenso}\n\n{texto}\n\n{dicio}")
    
#tuplas sao separadas com 'virgula'
chamaTupla("20 de Marco de 2024",
           "isso eh uma tupla", 
           "another tupla", 
           "terceira tupla", 
           chave = "valor",
           outraChave = "outroValor")

#*args(tupla) & **kwargs(dicionario)
# '/' numa função, divide os anteriores apenas como parâmetros por posição(sem keyWords)
# ' * ' apenas parâmetros nomeados (chave:valor)

def testeNomeados(*, nome, idade, cidade):
    print(nome, idade, cidade)
    
testeNomeados(nome="dani", idade="19", cidade="Curitiba") #NOTA-SE QUE A ORDEM DECLARADA NA
#CHAMADA DE FUNÇÃO NÃO IMPORTA!!!

def testeHibridos(texto1, texto2, /, texto_qualquer, *, nome, idade, sexo ):
    print(f"{texto1}\n{texto2}\n{texto_qualquer}\n{nome}\n{idade}\n{sexo}")
    
testeHibridos("oi!", "tudo bem?", teste ="teste de parametro", nome= "dani",idade= "19",sexo="feminino" )


#objetos de primeira classe -> string(argumento, variavel, retorno)