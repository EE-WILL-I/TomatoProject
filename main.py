
from Tomato import Tomato
from TomatoBush import TomatoBush

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
if tomato.is_ripe():
    print('grown')
else:
    print('not grown yet')

for t in tomato.get_tomatoes():
    print(t.get_state())
