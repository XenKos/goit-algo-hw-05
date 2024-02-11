def caching_fibonacci():
    cache={}   # створюємо словник для кешування результатів
    def fibonacci (n): # визначаємо функцію фібоначчі в середині функції caching_fibonacci():
        # базові випадки 0 та 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # перевіряємо, чи є результат n в кеші
        elif n in cache:
            return cache[n]
        #обчислюємо результат n, якщо результату n нема в кеші 
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    #повертаємо функцію фібоначчі
    return fibonacci
# створюємо функцію fib, що буде посилатися на функцію caching_fibonacci
fib = caching_fibonacci()
#викликаємо функцію fib з різними аргументами
print (fib(10))
print (fib (15))
print (fib (-10))



