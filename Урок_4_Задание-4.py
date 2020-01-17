# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.

my_list = [10, 25, 30, 45, 50, 25, 10]
print(my_list)
new_list = {el for el in my_list}
print(new_list)


def unique(*args):


    my_list = [10, 25, 30, 45, 50, 25, 10]
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            yield new_list


print(list(unique(my_list)))
