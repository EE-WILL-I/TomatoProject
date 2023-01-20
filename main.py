
from Tomato import Tomato
from TomatoBush import TomatoBush
from Gardener import Gardener

tomato = TomatoBush(10)
print(tomato.get_state())
tomato.grow()
if tomato.is_ripe():
    print('grown')
else:
    print('not grown yet')

print(tomato.get_state())
tomato.grow()
print(tomato.get_state())
tomato.grow()
print(tomato.get_state())
tomato.grow()
print(tomato.get_state())
print(tomato.get_tomato_count())
if tomato.is_ripe():
    print('grown')
else:
    print('not grown yet')

for t in tomato.get_tomatoes():
    print(t.get_state())
tomato.give_away_all()
print(tomato.get_tomato_count())
g = Gardener('john', tomato)
g.work()
g.knowledge_base()
g.harvest()
