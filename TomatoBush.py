
from Tomato import Tomato

class TomatoBush(Tomato):
    _tomatoes = []

    def __init__(self, tomato_count):
        self._tomato_count = tomato_count
        for i in range(tomato_count):
            self._tomatoes.append(Tomato(i))

    def grow(self):
        super().grow()
        for tomato in self._tomatoes:
            tomato.grow()

    def get_tomato_count(self):
        return self._tomato_count

    def get_tomatoes(self):
        return self._tomatoes

    def give_away_all(self):
        self._tomatoes = []
        self._tomato_count = 0