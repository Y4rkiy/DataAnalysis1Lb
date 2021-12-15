from collections import Counter
from datetime import datetime

data = []
with open('student_info.txt', encoding='utf-8') as file:
    for line in file:
        data.extend(line.rstrip().split(', '))

marks1 = []
marks2 = []
count3 = 0
count4 = 0
marks3 = []
names = ""
marks4 = []
marks5 = 0
name2 = ""
marks6 = dict()
teachers2020 = ""
task2dictionary = {}

for i in range(0, len(data), 8):

    if data[i][1] == "1" or data[i][1] == "3":
        marks1.append(data[i + 4])
    else:
        marks2.append(data[i + 4])

    if data[i][1] == "1" or data[i][1] == "2" and data[i + 4] == "A":
        count3 += 1

    if data[i][1] == "2" and int(data[i + 5]) > 70:
        count4 += 1

    if data[i][1] == "3" or data[i][1] == "4":
        marks3.append(data[i + 4])

    if data[i + 3] == "задовільно" and data[i + 6][3:5] == "08":
        names += data[i + 2] + " "

    if data[i][1] == "2" or data[i][1] == "3":
        marks4.append(int(data[i + 5]))

    if data[i + 6][6:10] == "2019":
        mark = int(data[i + 5])
        if mark > marks5:
            marks5 = mark
            name2 = data[i + 2]

    if not (data[i + 6][7:11] in marks6):
        marks6[data[i + 6][7:11]] = []
    marks6[data[i + 6][7:11]].append({data[i + 5]: data[i + 1] + " " + data[i + 2]})

    if data[i + 6][6:10] == "2020":
        teachers2020 += data[i + 2] + " "

    task2dictionary[
        (data[i][0], data[i][1], data[i][2])] = {'Subject name': data[i + 1],
                                                 'Lecturer name': data[i + 2],
                                                 'Mark list': [data[i + 3], data[i + 4], data[i + 5]],
                                                 'Date': datetime(int(data[i + 6][7:11]), int(data[i + 6][3:5]),
                                                                  int(data[i + 6][:2]), 0, 0),
                                                 'Issignature': data[i + 7]}

count1 = Counter(marks1)
print(count1.most_common()[0][0], count1.most_common()[1][0])

count2 = Counter(marks2)
print(count2.most_common()[-1][0], count2.most_common()[-2][0])

print(count3)

print(count4)

count5 = Counter(marks3)
print(count5.most_common()[0][0])

print(names)

print(sum(marks4) / len(marks4))

print(marks5, " ", name2)

for year in list(marks6.keys()):
    min_mark = 100
    for discipline in marks6[year]:
        discipline_mark = int(list(discipline.keys())[0])
        if discipline_mark < min_mark:
            min_mark = discipline_mark
    for discipline in marks6[year]:
        strmark = " " + str(min_mark)
        if strmark in discipline:
            print(discipline[strmark])

print(teachers2020)

print(task2dictionary)
