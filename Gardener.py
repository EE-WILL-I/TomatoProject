class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(self.name, 'did work for', self._plant.get_tomato_count(), 'tomatoes at one bush')
        self._plant.grow()

    def check_plant(self):
        print('plant state: ', self._plant.get_state().name)
        return self._plant.is_ripe()

    def harvest(self):
        if self.check_plant():
            print(self._plant.get_tomato_count(), 'tomatoes were harvested with state:', self._plant.get_state().name)
            self._plant.give_away_all()
            return True
        else:
            print('Tomatoes aren\'t ripe yet. state:', self._plant.get_state().name)
            return False

    def get_plant(self):
        return self._plant

    @staticmethod
    def knowledge_base():
        print('Есть Помидор со следующими характеристиками:', '1. Индекс',
              '2. Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)',
              '\nПомидор может:',
              '1. Расти (переходить на следующую стадию созревания)',
              '2. Предоставлять информацию о своей зрелости',
              '\nЕсть Куст с помидорами, который:',
              '1. Содержит список томатов, которые на нем растут',
              '\nИ может:',
              '1. Расти вместе с томатами',
              '2. Предоставлять информацию о зрелости всех томатов',
              '3. Предоставлять урожай',
              '\nИ также есть Садовник, который имеет:',
              '1. Имя',
              '2. Растение, за которым он ухаживает',
              '\nИ может:'
              '1. Ухаживать за растением',
              '2. Собирать с него урожай\n',
              sep='\n')
