import mysql.connector


def get_mark():
    student_marks = [input("Enter your English Mark: "),
                     input("Enter your Tamil Mark: "),
                     input("Enter your Maths Mark: "),
                     input("Enter your Science Mark: "),
                     input("Enter your History Mark: ")]

    return student_marks


def calculate_total(student_marks):
    return str(sum(list(map(int, student_marks))))


def calculate_average(student_marks):
    return str(sum(list(map(int, student_marks))) / len(student_marks))


def calculate_grade(student_marks):
    if float(sum(list(map(int, student_marks))) / len(student_marks)) >= 80:
        return "A"
    elif float(sum(list(map(int, student_marks))) / len(student_marks)) >= 60:
        return "B"
    elif float(sum(list(map(int, student_marks))) / len(student_marks)) >= 40:
        return "C"
    else:
        return "D"


if __name__ == '__main__':

    connection = mysql.connector.connect(host="localhost", user="root", password="", database="assignment")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE student (student_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(15),"
                   "dept VARCHAR(25), english INT, tamil INT, maths INT, science INT, history INT, total INT,"
                   "average DECIMAL(3,1), grade VARCHAR(1))")

    program = True

    while program:

        print("""Student Database: 
        1. Add a student to the database
        2. Edit a student data in the database
        3. Delete a student data from the database
        4. View a student's data
        5. View all student's data
        6. Exit database
        \n
        """)

        option = input("Enter a number to choose: ")

        if not option.isdigit():

            print("Print a number\n")

        elif int(option) == 1:

            student_name = input("Enter the name of the student: ")
            dept = input("Enter the department to which the student belongs: ")
            mark_list = get_mark()
            total_mark = calculate_total(mark_list)
            total_average = calculate_average(mark_list)
            student_grade = calculate_grade(mark_list)

            sql = f'INSERT INTO student(name, dept, english, tamil, maths, science, history, total, average,' \
                  'grade)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            values = (student_name, dept, mark_list[0], mark_list[1], mark_list[2], mark_list[3], mark_list[4],
                      total_mark, total_average, student_grade)
            cursor.execute(sql, values)
            connection.commit()

            print("Student Data added successfully!")

        elif int(option) == 2:

            stud_id = input("Enter student ID: ")
            column_select = input("Enter the column name you want to update: ")
            update_data = input("Enter the data you want to update: ")
            val_list = [update_data, stud_id]
            sql = f'UPDATE student SET {column_select} = %s WHERE student_id = %s'
            val = tuple(val_list)
            cursor.execute(sql, val)
            connection.commit()
            print(val)
            print("Data updated successfully!")

        elif int(option) == 3:

            val = tuple(input("Enter the student ID: "))
            sql = 'DELETE FROM student WHERE student_id = %s'
            cursor.execute(sql, val)
            connection.commit()
            print('Record deleted successfully!')

        elif int(option) == 4:

            val = tuple(input("Enter the student ID: "))
            sql = 'SELECT * FROM student WHERE student_id = %s'
            cursor.execute(sql, val)
            result = cursor.fetchall()
            for row in result:
                print(list(map(str, row)))
                print('\n')

        elif int(option) == 5:

            sql = "SELECT * FROM student"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(list(map(str, row)))
                print('\n')

        elif int(option) == 6:

            print("Goodbye")
            cursor.execute('DROP TABLE student')
            program = False
            break

        else:

            print("Incorrect Input!\n")
