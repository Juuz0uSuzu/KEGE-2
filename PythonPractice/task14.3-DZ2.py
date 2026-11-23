student = [(19, 172, 94, "Анатолий"), (18, 181, 69, "Бронислав"), (19, 164, 128, "Вавилен"), (18, 175, 67, "Геннадий")]
a = sorted(student, key=lambda x: x[2] / (x[1]**2))
for abiturient in a:
    print(abiturient[3])