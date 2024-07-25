#!/usr/bin/python
#coding: utf-8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
count_ = 0

for i in numbers:
    for j in range(1, i):
        if i%j == 0:
            count_ +=1
        elif count_ >1:
            not_primes.append(i)
            break

    if count_ == 0:
        pass 
    elif count_ <= 1 :
        primes.append(i)

    count_ = 0

print(primes)
print(not_primes)

