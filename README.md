
# DIO | Resumo Git & Github

Repositório para armazenar resumos sobre Git e Github do curso Versionamento de código.
[Curso](https://www.dio.me/)

## 📚 Documentação
- [Documentação Git](https://git-scm.com/doc)
- [Documentção GitHub](https://docs.github.com/pt)
## 👨‍💻 Resumos

| Branch | ramificações |
|--------|-------------|

```
Mkdir ‘’nome do diretorio’  → cria um novo diretório/pasta
```
```
CD ‘nome do diretório’ → acessa o diretório/pasta.
```
```
GIT INIT → comando que inicializa um repositório git  (comando usado dentro do repositório que quer ser usado)
```
```
GIT STATUS → área de preparação/visualização para criação de arquivos.
```
```
touch README.md → cria um arquivo texto em branco.
```

## Para salvar uma modificação
```
git add 'name' -> adicionar ao commit
```
```
git commit -m"nomedocommit" 
```
```
git log -> histórico
```
## Restauração de arquivos
```
 rm -rf .git-> remover um diretório recursivamente
```
```
git restore 'nomedoarquivo' -> recuperar arquivo
```
```
git commit --amend -m"novonome" -> altera o nome do commit
```
```
git reset --soft 'colar o commit (código acessado por git log)' -> voltar ao commit anterior
```
```
git reflog -> historico detalhado
```
# SUBIR UM COMMIT NO GITHUB

```

git remote add origin 'url do repositório'
```
```
git push -u origin main
```
```
git pull -> mesclar as alterações do repositório local e remoto
```
# BRANCHES
```
echo "nome do arquivo" > 'nomeEextensao'.txt -> cria um arquivo txt
```
```
git add . -> adiciona todos os arquivos da main a um commit novo
```
## Criar uma branch teste (ponteiro móvel)
```
git checkout -b 'nomeNovaBranch' -> cria uma nova branch
```
```
git checkout -b main -> retorna para a branch original 'main'
```
```
git branch -v -> mostra o último commit de cada branch
```
```
git merge 'nomeDaBranch' -> mescla a main com 'nomeDaBranch'
```
```
git branch -> listar as BRANCHES
```
```
git branch -d 'nomeDaBranch' -> excluir uma branch
```
```
git clone 'URL do repositorio' --branch "nomeDaBranch" --single-b (clonar uma branch)
```

