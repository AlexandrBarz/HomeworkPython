# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factors(n):
   i = 2
   primfact = []
   while i * i <= n:
       while n % i == 0:
           primfact.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfact.append(n)
   return primfact