#! /usr/bin/env python3

def fizzbuzz(n):
    """fizzbuzz
    引数が3の倍数のときは'Fizz'を出力
    引数が5の倍数のときは'Buzz'を出力
    引数が3と5の倍数のときは'FizzBuzz'を出力
    それ以外のときは引数をそのまま出力
    """
    answer = ''
    if n % 3 == 0:
        answer += "Fizz"
    if n % 5 == 0:
        answer += "Buzz"
    if n % 3 != 0 and n % 5 != 0:
        answer = str(n)
    print(answer)


if __name__ == '__main__':
    for i in range(1, 101):
        fizzbuzz(i)
