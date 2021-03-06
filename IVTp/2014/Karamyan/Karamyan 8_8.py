# Задача 8, Вариант 8.
# Доработайте игру "Анаграммы" так, чтобы к каждому
# слову полагалась подсказка. Игрок должен получать
# право на подсказку в том случае, если у него нет
# никаких предположений. Разработайте систему начисления
# очков, по которой бы игроки, отгадавшие слово без подсказки,
# получали больше тех, кто запросил подсказку.

# Карамня Н.Г.
# 26.05.2016

import random

# WORDS -- константа
WORDS = ("питон",
         "анаграмма",
         "просто",
         "сложно",
         "ответ",
         "вопрос")

# Выбираем один из элементов WORDS, записывам в word
word = random.choice(WORDS)

# Копируем значение word в "корректную" переменную для последующего сравнения
correct = word
 
i_dont_know = "Не знаю"
podskazka = word[0] + word[1] + word[2]
 
jumble = ""
while word:
    # Изымаем из ворд букву и переводим в джамп
    position = random.randrange(len(word))
    # Обновляем джамбл с добовлением буквы
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
 
score = int(10)
 
print(
    '''
    Добро пожаловать в игру "Анаграммы"!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    Если вам нужна подсказка введите: "Не знаю".
    Но учтите, если вы не будете использовать подсказку, 
    количество заработанных очков будет больше.
    '''
)


print ("У вас", score, "очков")
print("Вот анаграмма: ", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")


while guess != "" and guess != correct:
    
    if guess != correct and not guess == i_dont_know:
        print ("Ноуп")
        print ("У вас осталось")
        score -= 1
        print (score)
        
    if guess == i_dont_know:
        score -= 2
        print (score)
        print("\nПодсказка! Первые три буквы слова!", podskazka)
    guess = input("Попробуйте отгадать исходное слово: ")
    
    if guess == correct:
        print("Йес!\n")
 
    if score == 1:
        score = int(0)
        break

print("Спасибо за игру! У вас", score, "очков!")

input("\n\nНажмите Enter, чтобы выйти...")
