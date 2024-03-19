#DICIONARIOS SAO IMUTÁVEIS
#.update() -> adiciona um dicioanario a um dicionario existente

contatos = {"romao@gmail.com": {"nome": "dani","numero": "2345"}, 
            "camile@gmail.com": {"nome":"camile", "numero": "8564"}}

nome = contatos["romao@gmail.com"]["numero"]
print(nome)

print()

for chave, valor in contatos.items():
    print(chave, valor)
   
print()
contatos2 = contatos.copy()
contatos2["jertrudes@gmail.com"] = {"nome": "jertrudes"}
print(contatos2)
#retorna e elimina o primeiro elemento 
print()
returno = contatos2.pop("jertrudes@gmail.com", "não encontrado")
print(contatos2)
returno = contatos2.pop("jertrudes@gmail.com", "nao encontrado")
print(returno)
contatos.clear()   