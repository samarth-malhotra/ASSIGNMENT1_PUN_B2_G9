import datetime

# Hash table for students


class StudentHashTable:

    # Create empty hash table
    def initializeHash(self):
        self.size = 301
        self.students = [None] * self.size

    # Method to create Hash Id
    def HashId(self, studentId, next_slot):
        hash_id = 0
        for char in str(studentId):
            hash_id += ord(char)
        return (hash_id + (next_slot ^ 2)) % self.size

    # define string for the object
    def __str__(self):
        students_List = ""
        for student in self.students:
            if student is not None:
                students_List += str(self.students.index(student)
                                     ) + str(student) + "\n"
        return students_List

# Function to insert student record in hash table.
def insertStudentRec(StudentHashRecords, studentId, CGPA):
    next_slot = 0
    student = [studentId, CGPA]
    for count in range(StudentHashRecords.size):
        hash_id = StudentHashRecords.HashId(studentId, next_slot)
        if StudentHashRecords.students[hash_id] is None:
            StudentHashRecords.students[hash_id] = list(student)
            break
        else:
            # quadratic probing
            next_slot += 1

# Function to create HallofFame output file
def hallOfFame(StudentHashRecords, CGPA):
    qualified_students = []
    for student in StudentHashRecords.students:
        if (student is not None) and (student[1] > CGPA):
            qualified_students.append(student)
    hall_of_fame = "\n---------- hall of fame ----------"
    hall_of_fame += "\nInput: " + str(CGPA)
    hall_of_fame += "\nTotal eligible students: " + \
        str(len(qualified_students))
    hall_of_fame += "\nQualified students:"
    for student in qualified_students:
        hall_of_fame += "\n" + student[0] + " / " + str(student[1])
    hall_of_fame += "\n-------------------------------------\n"
    return hall_of_fame

# Function to create the New Course List
def newCourseList(StudentHashRecords, CGPAFrom, CGPATo):
    qualified_students = []
    for student in StudentHashRecords.students:
        if (student is not None) and (student[1] > CGPAFrom) and (student[1] < CGPATo) and ((int(student[0][:4]) + 4) > (datetime.datetime.now().year - 5)):
            qualified_students.append(student)
    new_course_list = "\n---------- New Course Candidates ----------"
    new_course_list += "\nInput: " + str(CGPAFrom) + " to " + str(CGPATo)
    new_course_list += "\nTotal eligible students: " + \
        str(len(qualified_students))
    new_course_list += "\nQualified students:"
    for student in qualified_students:
        new_course_list += "\n" + student[0] + " / " + str(student[1])
    new_course_list += "\n-------------------------------------\n"
    return new_course_list

# Function to create department list with average and max
def depAvg(StudentHashRecords):
    department_list = []
    for student in StudentHashRecords.students:
        if student is not None:
            department = student[0][4:7]
            if department in department_list:
                department_list[department_list.index(
                    department) + 1].append(student[1])
            else:
                department_list.append(department)
                department_list.append([student[1]])
    dep_avg = "\n---------- Department CGPA ----------"
    for department in department_list:
        if isinstance(department, str):
            list_index = department_list.index(department) + 1
            marks = department_list[list_index]
            dep_avg += f"\n{department},: max: {max(marks)}, avg: {sum(marks) / len(marks):.2f}"
    dep_avg += "\n-------------------------------------\n"
    return dep_avg

# Function to destroy the hash table
def destroyHash(StudentHashRecords):
    StudentHashRecords.students = [None] * StudentHashRecords.size
