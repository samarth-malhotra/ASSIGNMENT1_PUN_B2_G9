import student_hash_table as sh

StudentHashRecords = sh.StudentHashTable()
StudentHashRecords.initializeHash()

# Read student records from inputPS4.txt
try:
    input_file = open("../inputPS4.txt")
    for record in input_file.readlines():
        student = record.split(" / ")
        studentId = student[0]
        CGPA = float(student[1])
        StudentHashRecords.insertStudentRec(studentId, CGPA)
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
finally:
    input_file.close()

# Print HallOfFame list
try:
    prompt_file = open("../promptPS4.txt")
    for record in prompt_file.readlines():
        if "hallOfFame" in record:
            CGPA_hf = float(record.split(":")[1])
    hall_of_fame = StudentHashRecords.hallOfFame(CGPA_hf)
    output_file = open("../outputPS4.txt", "w+")
    output_file.write(hall_of_fame)
    output_file.close()
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
finally:
    prompt_file.close()
    output_file.close()

# Print Course Offer list
try:
    prompt_file = open("../promptPS4.txt")
    for record in prompt_file.readlines():
        if "courseOffer" in record:
            CGPAFrom = float(record.split(":")[1])
            CGPATo = float(record.split(":")[2])
    new_course_list = StudentHashRecords.newCourseList(CGPAFrom, CGPATo)
    output_file = open("../outputPS4.txt", "a+")
    output_file.write(new_course_list)
    output_file.close()
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
finally:
    prompt_file.close()

# Print average CGPA department wise
try:
    output_file = open("../outputPS4.txt", "a+")
    output_file.write(StudentHashRecords.depAvg())
    output_file.close()
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
finally:
    output_file.close()

StudentHashRecords.destroyHash()
