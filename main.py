from core import PyGeni
from model import Player, Block

jogo = PyGeni('MEU JOGI','768x768')

jogo.start()
per = Player('Meu Nome')
bloco = Block(x=120,y=120)
jogo.AddInstance(per)
jogo.AddInstance(bloco)


jogo.run()
