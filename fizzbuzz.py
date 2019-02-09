def fizzbuzz(x):
    result = ''

    if x % 3 == 0: result += 'fizz'
    if x % 5 == 0: result += 'buzz'
    if result == '': result = x
    return result

def run_fizzbuzz(i, n):
    while i <= n:
        fizzbuzz(i)
        i += 1
