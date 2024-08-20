from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        num_of_enemy = 100
        print(f'{self.name}, на нас напали!')
        days = 0
        while num_of_enemy > 0:
            days += 1
            time.sleep(1)
            num_of_enemy -= self.power
            print(f'{self.name}, сражается {days} день(дня)..., осталось {num_of_enemy} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились')
