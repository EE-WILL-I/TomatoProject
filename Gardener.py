
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow()

    def harvest(self):
        is_ripe = self._plant.is_ripe()
        print(is_ripe)