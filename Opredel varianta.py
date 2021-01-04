# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(input("Введите номер варианта:"))
    num = int(input("Введите номер задания:"))
    if num == 1:
        res_1 = ((N ** 2 + N + 1) % 15) + 1
        print(res_1)
    else:
        res_2 = ((N ** 2 + N + 7) % 20) + 1
        print(res_2)