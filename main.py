from core import PyGeni
from model import Player

jogo = PyGeni('MEU JOGI','1200x760')

jogo.start()
per = Player('Meu Nome')
jogo.AddInstance(per)



jogo.run()

