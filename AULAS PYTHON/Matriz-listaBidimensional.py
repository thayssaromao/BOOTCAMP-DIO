#[].clear() = limpar a lista
#[].copy() = copiar lista em outra estância (objetos diferentes)
#[].count('objeto') = quantas vezes um objeto aparece na lista
#[].extend() = merge de listas
#[].index() = retorna onde se encontra a primeira ocorrencia do objeto
#[].pop() = pilha de uma lista (tira o ultimo elemento da lista)
#[].reverse() = transpor a lista (inverter)
#[].sort() = ordenar lista
#[].sort(key=lambda x: len(x)) = ordenar lista
#len() = retorna tamanho da lista
h = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(h)
print()
matriz = [["0,0","0,1","0,2"], ["1,0","1,1","1,2"]]
for i in range(0,2):
    print("| ", end=" ")
    for j in range(0, 3):
        print(matriz[i][j], end=" ")
    print("| ")
#matriz de ordem (2x3)
print()
legumes = ["cenoura", "beterraba","abobrinha"]
for indice, elemento in enumerate(legumes):
    print(f"Indice:{indice} -> elemento:{elemento}.")
legumes.sort(key=lambda x: str(x))#str -> ordem alfabetica
print(legumes)    
legumes.sort(key=lambda x: len(x)) #len -> tamanho
print(legumes) 
    
#Compresao de listas -> filtro versao 1
#visibilidade e compreensao do código muito melhor
print()
list = [6,2,8]
aux = []

for i in list:
    if i == 2:
        aux.append(i)
print(aux)

#filtro versao 2
#menos linhas de código
aux =[i for i in list if i == 2]
print(aux)
print()
list.sort(key=lambda x: int(x))
print(list)
list.sort(key=lambda x: int(x), reverse=True)
print(list)
list.extend(legumes)
print(list)

