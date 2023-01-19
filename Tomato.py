
from State import State


class Tomato:
    _state = State.NONE

    def __init__(self, index):
        self._index = index

    def grow(self):
        if self._state == State.RED:
            print('Tomato is already grown!')
            return
        self._state = State(self._state.value + 1)

    def get_state(self):
        return self._state

    def get_index(self):
        return self._index

    def is_ripe(self):
        return self.get_state() == State.RED
