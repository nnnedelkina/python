
n = 0
summa = 0
with open('file_3.txt') as my_fale:
    for line in my_fale:
        person = line.split()
        #print(person)
        person_salary = float(person[1])
        #print(person_salary)
        print(person[0]) if person_salary < 20000 else ''
        summa += person_salary
        n +=1

print('средняя зарплата: ', round((summa / n), 2))
