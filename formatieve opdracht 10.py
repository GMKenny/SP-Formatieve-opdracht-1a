def fibonaci(num):
    if num <= 1:
        print("Verkeerde input alles boven de 1")
    if num == 2:
        return [0, 1]
    eerste_fib = fibonaci(num - 1)
    volgende_fib = eerste_fib[-1] + eerste_fib[-2]
    return eerste_fib + [volgende_fib]

print(fibonaci(34))