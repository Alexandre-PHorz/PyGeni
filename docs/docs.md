# 🕹️Documentação do PyGeni

Bem-vindo ao PyGeni, sua engine para criação de jogos em Python. Esta documentação guiará você nos primeiros passos para configurar seu ambiente e colocar seu projeto para rodar.

## 📌Sumario

* [Inicialização](#inicialização)
  * [Passo 1](#passo-1---estrutura)
  * [Passo 2](#passo-2---importação-e-configuração)
  * [Passo 3](#passo-3---ciclo-do-pygeni)
* [Adicionar Elementos](#adicionar-elementos)
  * [Criação de um Jogador](#criação-do-jogador)

## Inicialização

Para começar a utilizar o PyGeni, siga o guia de configuração básica abaixo.

### Passo 1 - Estrutura

Crie um arquivo na raiz do seu projeto chamado ```main.py```. Este será o ponto de entrada principal da sua aplicação.

### Passo 2 - Importação e Configuração
Dentro do ```main.py```, você deve importar o núcleo da engine e instanciar a classe principal definindo o título e a resolução da janela:
```Python
from core import PyGeni

# Inicializa o objeto com Título e Resolução (Largura x Altura)
game = PyGeni('Meu primeiro PyGeni', '768x768')
```

### Passo 3 - Ciclo do PyGeni
Existem dois métodos essenciais para o funcionamento:
1. ```game.start()```: Prepara os recursos internos da engine.

2. ```game.run()```: Inicia o loop principal do jogo (Main Loop).
```python
game.start()

...

if __name__ == "__main__":
    game.run()
```
### Exemplo
Assim o seu arquivo ```main.py``` seria assim:
```Python
from core import PyGeni

game = PyGeni('Meu primeiro PyGeni', '768x768')

game.start()

... # Outras configurações

if __name__=='__main__':
    game.run()
```

---

## Adicionar elementos

Para que um jogo seja um jogo, ele precisa de elementos, e para adicionar eles é necessario crialos e adiciona-los ao jogo.
Para adicionar uma instancia, deve-se chamar a função ```AddInstance()``` do PyGeni
```python
game = PyGeni('Meu primeiro PyGeni', '768x768')
game.start()

game.AddInstance(object)

```
para configurar o objeto, usamos modelos, e cada item tem um modelo, veja a baixo como adicionalos

### Criação do Jogador
Para a criação de um jogador, precisa chamar um modelo de jogador,como ```Player()```, com

```python
from model import Player
```
E fazer a configuração desse Jogador para que adiciona-lo ao jogo
```python
jogador = Player(
    name='Alexandre',
    hp=100,
    lv=1,
    x=0,
    y=0,
    speed=4
)
```

