#conjunto é uma coleção não ordenada de elementos ÚNICOS.
#.symmetric_difference() -> retorna os elementos que são exclusivos de cada conjunto, eliminando aqueles que são comuns a ambos.
#.issubset() -> verificar se um conjunto é um subconjunto de outro conjunto.
#.issuperset() -> verificar se um conjunto contém todos os elementos de outro conjunto
#.isdisjoint() -> verifica se os conjuntos são disjuntos
#.add() -> adicionar um elemento ao conjunto
#.copy()
#.discard() -> descartar um valor do conjunto


conjunto_a = {1,2,3,4} #recebe um set 
conjunto_b = {2,6,7,8}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))