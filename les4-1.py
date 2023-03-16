#!/usr/bin/env python
import sys

def salary(hours, rate, bonus):
    payment = hours * rate + bonus
    return payment

if __name__ == '__main__':
    if not len(sys.argv) == 4:
        print('Wrong arguments')
        sys.exit(1)

    payment = salary(sys.argv[1], sys.argv[2], sys.argv[3])
    print('Salary is', payment)