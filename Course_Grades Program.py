#GradeAvg Application
#25 Sep 2020

def getGrade(num_students, num_grades):
    mark_book = []
    for student in range(num_students):
        grade = []
        user_name = input("{:} {:} {:}".format("Name of Student", student+1, ": "))
        grade.append(user_name)
        for g in range(num_grades):
            first_grade = int(input("Grade: "))
            grade.append(first_grade)
        mark_book.append(grade)
    return(mark_book)

def Average(mark_book, student):
    studentavg = 0
    for i in range(1,len(mark_book[student-1])):
        studentavg += mark_book[student-1][i]
    return(studentavg/(len(mark_book[student-1])-1))

def testsAverage(mark_book, test):
    testavg = 0
    for i in mark_book:
        testavg += i[test+1]
    return(testavg/len(mark_book))

def showgrades(mark_book):
    grades = []
    for i in mark_book:
        for item in i:
            grades.append(item)
    return(grades)

num_students = int(input("Enter the Number of Students: "))
num_grades = int(input("Enter the Number of Grades per Student: "))
mark_book = getGrade(num_students, num_grades)
studentavg = int(input("Enter the Student Number to check the average of that student: "))
test_num = int(input("Enter the Test number: "))
print(Average(mark_book, studentavg))
print(testsAverage(mark_book, test_num))
for i in showgrades(mark_book):
    print(i)
