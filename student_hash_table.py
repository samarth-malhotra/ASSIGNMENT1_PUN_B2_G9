# Hash table for students
class StudentHashTable:

    # Create empty hash table
    def initializeHash(self):
        self.size = 300
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

    # Method to insert student record in hash table.
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

    # Method to create HallofFame output file
    def hallOfFame(StudentHashRecords, CGPA):
        qualified_students = []

        for student in StudentHashRecords.students:
            if (student is not None) and (student[1] > CGPA):
                qualified_students.append(student)

        output_file = open("outputPS4.txt", "a+")
        output_file.write("\n---------- hall of fame ----------")
        output_file.write("\nInput: " + str(CGPA))
        output_file.write("\nTotal eligible students: " +
                          str(len(qualified_students)))
        output_file.write("\nQualified students:")
        for student in qualified_students:
            output_file.write("\n" + student[0] + " / " + str(student[1]))
        output_file.write("\n-------------------------------------\n")
        output_file.close()

    # Method to create the New Course List
    def newCourseList(StudentHashRecords, CGPAFrom, CGPATo):
        qualified_students = []

        for student in StudentHashRecords.students:
            if (student is not None) and (student[1] > CGPAFrom) and (student[1] < CGPATo):
                qualified_students.append(student)

        output_file = open("outputPS4.txt", "a+")
        output_file.write("\n---------- New Course Candidates ----------")
        output_file.write("\nInput: " + str(CGPAFrom))
        output_file.write(" to " + str(CGPATo))
        output_file.write("\nTotal eligible students: " +
                          str(len(qualified_students)))
        output_file.write("\nQualified students:")
        for student in qualified_students:
            output_file.write("\n" + student[0] + " / " + str(student[1]))
        output_file.write("\n-------------------------------------\n")
        output_file.close()

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
        output_file = open("outputPS4.txt", "a+")
        output_file.write(
            "\n---------- Department CGPA this is new stuff----------")
        for department in department_list:
            if isinstance(department, str):
                list_index = department_list.index(department) + 1
                marks = department_list[list_index]
                output_file.write(
                    f"\n{department},: max: {max(marks)}, avg: {sum(marks) / len(marks):.2f}")
        output_file.write("\n-------------------------------------\n")
        output_file.close()

    def destroyHash(self):
        self.students = [None] * self.size
