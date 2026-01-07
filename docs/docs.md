# Documentação do PyGeni

Siga as instrução e os topicos a baixo para fazer corretamente.

## Sumario

* [Inicialização](#inicialização)
  * [Passo 1](#passo-1)
  * [Passo 2](#passo-2)
  * [Passo 3](#passo-3)

## Inicialização

Bem-vindo ao **PyGeni**, para começar seus primeiros passos precisamos iniciar o PyGeni.
### Passo 1
Primeiro crie um arquivo na raiz do projeto chamado _main.py_, ele será o arquivo principal do projeto.
### Passo 2
Após isso, dentro do _main.py_, chame o nucleo da engine, importando:
```Python
from core import PyGeni
```
e crie um Objeto trazendo todas as configurações iniciais do jogo.
```python
game = PyGeni('Meu primeiro PyGeni','768x768')
```
### Passo 3
Para iniciar mesmo o jogo temos dois comandos, o primeiro será logo após criar o PyGeni, com: 
```python
game.start()
```
E outro para rodar o jogo, que é recomendado colocar ao fim do codigo:
```python
if __name__ == "__main__":
    game.run()
```

