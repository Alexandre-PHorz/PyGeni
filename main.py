from core import PyGeni
from model import Player

jogo = PyGeni('MEU JOGI','768x768')

jogo.start()
per = Player('Meu Nome')
jogo.AddInstance(per)



jogo.run()

