
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
