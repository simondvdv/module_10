from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:

    def __init__(self, balance=0, lock=Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            refill_number = randint(50, 500)
            self.balance += refill_number
            print(f'Пополнение: {refill_number}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(100):
            unrefill_number = randint(50, 500)
            print(f'Запрос на {unrefill_number}')
            if self.balance >= unrefill_number:
                self.balance -= unrefill_number
                print(f'Снятие {unrefill_number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')