hello = "Привет, путешественники! Застряли? Подсказка...."
print(hello)
import random

first_numb = random.randint(3, 20)
print("First_number: ",  first_numb)
x = int(first_numb)
for i in range(1, 21):
    for j in range(1, 21):
        if j + i == x and i != j:
            print('Second_nun: ', i,"and", j)


