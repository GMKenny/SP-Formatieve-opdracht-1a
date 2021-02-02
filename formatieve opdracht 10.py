def fibonaci(num, first_num=0, second_num=1):
    # Num wordt gebruikt als counter voor de aantal keer dat de functie moet lopen
    # First en second num worden gebruikt om de fibonaci te berekenen
    # Als het nummer groter is dan 1
    if num > 1:
        # return fibonaci num min 1 om de loop bij te houden.
        # First_num wordt second num en second_num word first_num + second_num
        return fibonaci(num - 1, second_num, first_num + second_num)
    # return het laaste fibonaci nummer.
    return second_num

print(fibonaci(100))
