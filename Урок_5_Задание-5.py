# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

out_f = open("out_file.txt", "w")
str_list = input('Введите число: ').split()
out_f.writelines(str_list)
out_f.close()

with open('out_file.txt', 'r') as f:
    result = sum(map(int, f))
print(result)
