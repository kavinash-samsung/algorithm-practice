calculate = {}
def fibonicci(no):
    if no == 0:
        return 0
    if no == 1:
        return 1
    if no in calculate:
        return calculate[no]
    else:
        calculate[no] = fibonicci(no-1)+fibonicci(no-2)
        return calculate[no]

numbers = 10
print(fibonicci(numbers))
    