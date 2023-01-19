
from State import State


class Tomato:
    index = 0
    state = State.NONE

    def grow(self):
        if self.state == State.RED:
            print('Tomato is already grown!')
            return
        self.state = State(self.state.value + 1)

    def get_state(self):
        return self.state
