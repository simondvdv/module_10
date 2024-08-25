from random import randint
from threading import Thread
import queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep_time = randint(3, 5)
        print(sleep_time)
        sleep(sleep_time)


class Cafe:
    def __init__(self, *table):
        self.queue = queue.Queue()
        self.tables = table

    def guest_arrival(self, *guests):
        if len(guests) <= len(self.tables):
            for i, guest in enumerate(guests):
                self.tables[i].guest = guest.name
                print(f'{guest.name} сел(-а) за стол номер {self.tables[i].number}')
                guest.start()
        else:
            for i, guest in enumerate(guests):
                try:
                    self.tables[i].guest = guest.name
                    print(f'{guest.name} сел(-а) за стол номер {self.tables[i].number}')
                    guest.start()
                except IndexError:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        def table_check():
            flag = 0
            for i in self.tables:
                if i.guest is not None:
                    flag += 1
            if flag != 0:
                # print('eto flag', flag)
                return True
            else:
                return False

        while not self.queue.empty() or table_check():
            for i in self.tables:
                if i.guest is not None and not i.guest.is_alive():
                    print(f'{i.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {i.number} свободен')
                    i.guest = None
                if not self.queue.empty():
                    next_guest = self.queue.get()
                    i.guest = next_guest
                    print(
                        f'{next_guest} имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
                    i.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

# t1 = Table(1)
# t2 = Table(2)
# t3 = Table(3)
# g1 = Guest('John')
# g2 = Guest('Denis')
# g3 = Guest('Kevin')
# g4 = Guest('Mike')
# c1 = Cafe(t1, t2)
# c1.guest_arrival(g1, g2, g3, g4)
# c1.discuss_guests()


# def guest_arrival(self, *guests):
#     for k in guests:
#         for i in self.tables:
#             if i.guest is None:
#                 print(f'{k.name} сел(-а) за стол номер {i.number}')
#                 i.guest = k.name
#                 break
#             else:
#                 print(f'{k.name} в очереди')


# def guest_arrival(self, *guests):
#     if len(guests) <= len(self.tables):
#         for i in range(len(guests)):
#             self.tables[i].guest = guests[i].name
#             print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
#             guests[i].start()
#     else:
#         for i in range(len(guests)):
#             try:
#                 self.tables[i].guest = guests[i].name
#                 print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
#                 guests[i].start()
#             except IndexError:
#                 self.queue.put(guests)
#                 print(f'{guests[i].name} в очереди')

# def discuss_guests(self):
#     def table_check():
#         flag = 0
#         for i in self.tables:
#             if i.guest is not None:
#                 flag += 1
#         if flag != 0:
#             # print('eto flag', flag)
#             return True
#         else:
#             return False
#
#     while not self.queue.empty() or table_check():
#         for i in self.tables:
#             if not i.guest is None and not i.guest.is_alive():
#                 print(f'{i.guest} покушал(-а) и ушёл(ушла)')
#                 print(f'Стол номер {i.number} свободен')
#                 i.guest = None
#             if not self.queue.empty():
#                 next_guest = self.queue.get()
#                 i.guest = next_guest
#                 print(f'{next_guest} имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
#                 i.guest.start()
