
from Tomato import Tomato
from TomatoBush import TomatoBush
from Gardener import Gardener

Gardener.knowledge_base()

tomato_count = int(input("How much tomatoes?"))
bush = TomatoBush(tomato_count)

name = input('Who will work?')
gardener = Gardener(name, bush)

gardener.work()
gardener.harvest()

while not gardener.check_plant():
    gardener.work()

for tomato in gardener.get_plant().get_tomatoes():
    print(tomato.get_index(), tomato.get_state())

gardener.harvest()
