#!/usr/bin/env python3
# -*- config: utf-8 -*-

# 20. Создать класс Pair (пара целых чисел); определить метод умножения на чис ло и операцию
# сложения пар (a,b) + (c,d) = (a + b, c + d) . Определить класс-наследник Money с полями:
# рубли и копейки. Переопределить операцию сло жения и определить методы вычитания и
# деления денежных сумм.

class Pair:
    def __init__(self, a=0, b=1):
        a = int(a)
        b = int(b)

        self.__first = abs(a)
        self.__second = abs(b)

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',', maxsplit=1)))

        self.__first = abs(parts[0])
        self.__second = abs(parts[1])

    def display(self):
        print(f"{self.__first}, {self.__second}")

    def mul(self, new):
        if isinstance(new, Pair):
            a = self.first * new.first
            b = self.second * new.second

            return Pair(a, b)
        else:
            raise ValueError()

    def add(self, new):
        if isinstance(new, Pair):
            a = self.first + new.first
            b = self.second + new.second

            return Pair(a, b)
        else:
            raise ValueError()


class Money(Pair):
    def __init__(self, rub, kop):
        super().__init__(rub, kop)
        self.__rub = rub
        self.__kop = kop

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',', maxsplit=1)))

        self.__rub = abs(parts[0])
        self.__kop = abs(parts[1])

    def display(self):
        print(f"{self.__rub} рублей,{self.__kop} копеек")

    def mul(self, new):
        if isinstance(new, Money):
            rub = self.__rub * new.__rub
            kop = self.__kop * new.__kop

            if kop >= 100:
                rub += kop // 100
                kop %= 100

            return Money(rub, kop)
        else:
            raise ValueError()

    def div(self, new):
        if isinstance(new, Money):
            rub = new.__rub / self.__rub
            kop = new.__kop / self.__kop

            if kop >= 100:
                rub += kop // 100
                kop %= 100

            return Money(rub, kop)
        else:
            raise ValueError()

    def add(self, new):
        if isinstance(new, Money):
            rub = self.__rub + new.__rub
            kop = self.__kop + new.__kop

            if kop >= 100:
                rub += kop // 100
                kop %= 100

            return Money(rub, kop)
        else:
            raise ValueError()

    def sub(self, new):
        if isinstance(new, Money):
            rub = new.__rub - self.__rub
            kop = new.__kop - self.__kop

            if kop >= 100:
                rub += kop // 100
                kop %= 100

            return Money(rub, kop)
        else:
            raise ValueError()


if __name__ == '__main__':
    p_1 = Pair(1, 2)
    p_1.display()

    p_2 = Pair()
    p_2.read("Введите пару чисел через запятую: ")
    p_2.display()

    p_3 = p_2.add(p_1)
    p_3.display()

    p_4 = p_2.mul(p_1)
    p_4.display()

    m_1 = Money(999, 99)
    m_1.display()

    m_2 = Money(0, 0)
    m_2.read("Введите рубли и копейки через запятую: ")
    m_2.display()

    m_3 = m_2.add(m_1)
    m_3.display()

    m_4 = m_2.sub(m_1)
    m_4.display()

    m_5 = m_2.mul(m_1)
    m_5.display()

    m_6 = m_2.div(m_1)
    m_6.display()