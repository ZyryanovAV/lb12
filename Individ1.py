# Создать класс Payment (зарплата). В классе должны быть представлены поля: фамилия-
# имя-отчество, оклад, год поступления на работу, процент надбавки, подоходный налог,
# количество отработанных дней в месяце, количество рабочих дней в месяце, начисленная и
# удержанная суммы. Реализовать методы:
# вычисления начисленной суммы,
# вычисления удержанной суммы,
# вычисления суммы, выдаваемой на руки,
# вычисления стажа. Стаж вычисляется как полное количество лет, прошедших от года
# поступления на работу, до текущего года.
# Начисления представляют собой сумму, начисленную за отработанные дни, и
# надбавки, то есть доли от первой суммы. Удержания представляют собой отчисления в
# пенсионный фонд (1% от начисленной суммы) и подоходный налог. Подоходный налог
# составляет 13% от начисленной суммы без отчислений в пенсионный фонд.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

class Payment:

    def __init__(self, Name=' ', year=0, oklad=0, percent=0, Worked_days=0, working_day=1):
        self.Name = str(Name)
        self.year = int(year)
        self.oklad = int(oklad)
        self.percent = float(percent)
        self.Worked_days = int(Worked_days)
        self.working_day = int(working_day)
        self.amount = 0
        self.heldAmount = 0
        self.handAmount = 0
        self.expir = 0

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def read(self):
        Name = input('Введите ФИО: ')
        oklad = input('Укажите оклад: ')
        year = input('Укажите год вашего поступления на работу: ')
        percent = input('Укажите процент надбавки: ')
        Worked_days = input('Укажите количество отработанных дней в месяце: ')
        working_day = input('Введите количество рабочих дней в месяце: ')

        self.Name = str(Name)
        self.oklad = int(oklad)
        self.year = int(year)
        self.percent = float(percent)
        self.Worked_days = int(Worked_days)
        self.working_day = int(working_day)

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def display(self):
        print(f"Начисленная зарплата: {round(self.amount)}")
        print(f"Сумма вычетов: {round(self.heldAmount)}")
        print(f"Выданная на руки заработная плата: {round(self.handAmount)}")
        print(f"Размер трудового стажа: {self.expir} год/года/лет")

    def accruedAmount(self):
        a = self.oklad / self.working_day
        b = a * self.Worked_days
        percent = self.percent / 100 + 1
        self.amount = b * percent

    def withheldAmount(self):
        plata = (self.oklad / self.working_day) * self.Worked_days
        self.heldAmount = (plata * 0.13) + (plata * 0.01)

    def handedAmount(self):
        self.handAmount = self.amount - self.heldAmount

    def experience(self):
        self.expir = 2020 - self.year


if __name__ == '__main__':
    s = Payment()
    s.read()
    s.display()