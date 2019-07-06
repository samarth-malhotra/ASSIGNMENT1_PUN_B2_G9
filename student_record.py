import student_hash_table as sh

StudentHashRecords = sh.StudentHashTable()
StudentHashRecords.initializeHash()

# Read student records from inputPS4.txt
input_file = open("inputPS4.txt")
for record in input_file.readlines():
    student = record.split(" / ")
    studentId = student[0]
    CGPA = float(student[1])
    StudentHashRecords.insertStudentRec(studentId, CGPA)

# Print HallOfFame list
prompt_file = open("promptPS4.txt")
for record in prompt_file.readlines():
    if "hallOfFame" in record:
        CGPA_hf = float(record.split(":")[1])
StudentHashRecords.hallOfFame(CGPA_hf)

# Print Course Offer list
prompt_file = open("promptPS4.txt")
for record in prompt_file.readlines():
    if "courseOffer" in record:
        CGPAFrom = float(record.split(":")[1])
        CGPATo = float(record.split(":")[2])
StudentHashRecords.newCourseList(CGPAFrom, CGPATo)


# Print average CGPA department wise
StudentHashRecords.depAvg()

StudentHashRecords.destroyHash()
