def second_highest(students):
    new_students = []
    for item in students:
        new_students.append([item[1],item[0]])
    new_students = sorted(new_students, reverse=True)
    print('studnet list after adjustment is(score is shown first, and name is shown secod)\n--->', new_students)

    second_num = new_students[1][0]
    print('Second highest score is', second_num)

    for i in new_students:
        if i[0] == second_num:
            print(i[1])

students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
second_highest(students)