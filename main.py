n = int(input())
if 0 <= n <= 1000:
    a = n % 100
    b = a % 10
    if b == 0 or 5 <= b <= 9 or 5 <= n <= 19 or n == 1000 or 11 <= n <= 14 or 111 <= n <= 114 or 211 <= n <= 214 or 311 <= n <= 314 or 411 <= n <= 414 or 511 <= n <= 514 or 611 <= n <= 614 or 711 <= n <= 714 or 811 <= n <= 814 or 911 <= n <= 914:
        n = str(n)
        print(n + ' программистов')
    elif 2 <= b <= 4:
        n = str(n)
        print(n + ' программиста')
    else:
        n = str(n)
        print(n + ' программист')
else:
    print('Введи число от 0 до 1000')
    