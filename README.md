
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
cd ‘nome do diretório’ → acessa o diretório/pasta.
```
```
git init → comando que inicializa um repositório git(diretório já existente)
```
```
git status -> área de preparação/visualização para criação de arquivos.
```
```
touch "README".md -> cria um arquivo texto em branco.(para criar outros tipos de arquivos basta mudar a extensão)
```
```
git diff -> mostra alterações feitas no arquivo modificado
```
```
git diff --staged -> mostra alterações feitas no arquivo na área de staged
```
```
git reset --hard codigo do commit  -> voltar a branch principal (ex: main) para esse commit
```
```
git push --force -> atualizar repositório remoto
```


## Para salvar uma modificação
```
git add 'name' -> adicionar ao commit('git add .' adiciona todas as alterações não rastreadas)
```
```
git commit -m"nomedocommit" (adicionar um novo commit/atualização)
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
git remote set-url origin <nova_URL_do_repositório>
```
```
git remote -v --> visualizar as URLs dos repositórios remotos associados ao seu repositório Git local
```
```
git push -u origin main -> enviar commits locais para um repositório remoto (repo no github) 
```
```
git pull -> obter alterações do repositório remoto e mesclar com o repositório local
```
```
git remote add upstream -> " é um nome comum dado ao repositório remoto original a partir do qual o seu repositório local foi bifurcado (forked)
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

