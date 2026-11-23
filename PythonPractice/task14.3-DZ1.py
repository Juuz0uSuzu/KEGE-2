student = [("Анна", 16), ("Бронислав", 15), ("Федот", 18)]
print(max(student, key=lambda x: x[1],)[0])