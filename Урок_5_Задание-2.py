# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

out_f = "out_file.txt"

num_lines = 0
num_words = 0

with open(out_f, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
print(num_lines, num_words)