# Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
# Напишите функцию, которая принимает список, из списка выдает случайное значение из списка и записывает результат в txt файл. Список language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# names = [“azat”, “zina”, “kuma”, “anna”, “sas”] Вывести с помощью lambda функции имена палиндромы 



#1 задача
def print_zero():
    for i in range(0,6):
        print(f"Строка {i}: {'0' * 5}")

print_zero()

#2 задача
import random
def srf(language_list):
    random_language = random.choice(language_list)
    with open("random_language.txt", "w") as file:
        file.write(random_language)
language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]
srf(language)

#3 задача
names = ["azat", "zina", "kuma", "anna", "sas"]
palindromes = list(filter(lambda x: x == x[::-1], names))
print("gалиндромы:", palindromes)



