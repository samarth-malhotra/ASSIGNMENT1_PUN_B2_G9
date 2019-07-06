# Hash table for students


# Create empty hash table
def initializeHash():
    size = 300
    global StudentHashRecords
    StudentHashRecords = [None] * size


# Function to create Hash Id
def HashId(studentId):
    hash_id = 0
    for char in str(studentId):
        hash_id += ord(char)
    return hash_id % len(StudentHashRecords)


initializeHash()


# Function to insert student record in hash table.
def insertStudentRec(StudentHashRecords, studentId, CGPA):
    hash_id = HashId(studentId)
    student = [studentId, CGPA]
    next_slot = 1

    while True:
        if StudentHashRecords[hash_id] is None:
            StudentHashRecords[hash_id] = list(student)
            break
        else:
            # quadratic probing
            hash_id += (next_slot ^ 2)


# Read student records from inputPS4.txt
input_file = open("inputPS4.txt")
for record in input_file.readlines():
    student = record.split(" / ")
    studentId = student[0]
    CGPA = float(student[1].rstrip("\n"))
    insertStudentRec(StudentHashRecords, studentId, CGPA)


def hallOfFame(StudentHashRecords, CGPA):
    qualified_students = []

    for student in StudentHashRecords:
        if (student is not None) and (student[1] > CGPA):
            qualified_students.append(student)

    output_file = open("outputPS4.txt", "w+")
    output_file.write("---------- hall of fame ----------")
    output_file.write("\nInput: " + str(CGPA))
    output_file.write("\nTotal eligible students: " + str(len(qualified_students)))
    output_file.write("\nQualified students:")
    for student in qualified_students:
        output_file.write("\n" + student[0] + " / " + str(student[1]))
    output_file.close()


hallOfFame(StudentHashRecords, 4)
