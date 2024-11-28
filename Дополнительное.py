hello = "Привет, путешественники! Застряли? Подсказка...."
print(hello)
import random

first_numb = random.randint(3, 20)
print("First_number: ",  first_numb)
x = int(first_numb)
sec_res = []
for i in range(1, 21):
    for j in range(1, 21):
        if j == i:
            break
        if j + i == x and i != j:
            sec_number = i, j
            #print('Second_nun: ', sec_number)

            sec_res.extend(sec_number)
print('Second_nun: ',sec_res)
