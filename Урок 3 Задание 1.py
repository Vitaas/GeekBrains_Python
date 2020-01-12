def s_calc():
    try:
        val_1 = int(input("Введите первое число: "))
        val_2 = int(input("Введите второе число: "))
        div_val = val_1 // val_2
    except ZeroDivisionError:
        return 0
    div_val = val_1 // val_2
    return div_val

print(s_calc())
