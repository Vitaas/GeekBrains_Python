# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

replace = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

out_f = open("out_file.txt", "r")
in_f = open("in_file.txt", "w", encoding="utf-8")

for line in out_f:
    for key, value in replace.items():
        line = line.replace(key, value)
    in_f.write(line)
in_f.close()

