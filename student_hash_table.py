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
                students_List+= str(self.students.index(student)) + str(student) + "\n"
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
        output_file.write("\nTotal eligible students: " + str(len(qualified_students)))
        output_file.write("\nQualified students:")
        for student in qualified_students:
            output_file.write("\n" + student[0] + " / " + str(student[1]))
        output_file.write("\n-------------------------------------\n")
        output_file.close()


    # Method to create the New Course List
    def newCourseList(StudentHashRecords, CGPAFrom, CGPATo):
        qualified_students = []

        for student in StudentHashRecords.students:
            if (student is not None) and (student[1] > CGPAFrom) and (student[1] < CGPATo) :
                qualified_students.append(student)

        output_file = open("outputPS4.txt", "a+")
        output_file.write("\n---------- New Course Candidates ----------")
        output_file.write("\nInput: " + str(CGPAFrom))
        output_file.write(" to " + str(CGPATo))
        output_file.write("\nTotal eligible students: " + str(len(qualified_students)))
        output_file.write("\nQualified students:")
        for student in qualified_students:
            output_file.write("\n" + student[0] + " / " + str(student[1]))
        output_file.write("\n-------------------------------------\n")
        output_file.close()


    def depAvg(StudentHashRecords):
        #department_list = [['CSE'], ['MEC'], ['ECE'], ['ARC']]
        CSE_count, MEC_count, ECE_count, ARC_count = 1,1,1,1
        CSE_Max, MEC_Max, ECE_Max, ARC_Max = 0,0,0,0
        CSE_Sum, MEC_Sum, ECE_Sum, ARC_Sum = 0,0,0,0
        for student in StudentHashRecords.students:
            if (student is not None):
                department = student[4:7]
                if department == 'CSE':
                    CSE_count += 1
                    CSE_Max = CSE_Max if CSE_Max > student[1] else student[1]
                    CSE_Sum += CSE_Sum
                elif department == 'MEC':
                    MEC_count += 1
                    MEC_Max = MEC_Max if MEC_Max > student[1] else student[1]
                    MEC_Sum += MEC_Sum
                    #department_list[1].append(student[1])
                elif department == 'ECE':
                    ECE_count += 1
                    ECE_Max = ECE_Max if ECE_Max > student[1] else student[1]
                    ECE_Sum += ECE_Sum
                    #department_list[2].append(student[1])
                elif department == 'ARC':
                    ARC_count += 1
                    ARC_Max = ARC_Max if ARC_Max > student[1] else student[1]
                    ARC_Sum += ARC_Sum
                    #department_list[3].append(student[1])

        output_file = open("outputPS4.txt", "a+")
        output_file.write("\n---------- Department CGPA ----------")
        output_file.write(f"\nCSE: max: {CSE_Max}, avg: {CSE_Sum/(CSE_count if CSE_count !=0 else 1):.2f}")
        output_file.write(f"\nMEC: max: {MEC_Max}, avg: {MEC_Sum/(MEC_count if MEC_count !=0 else 1):.2f}")
        output_file.write(f"\nECE: max: {ECE_Max}, avg: {ECE_Sum/(ECE_count if ECE_count !=0 else 1):.2f}")
        output_file.write(f"\nARC: max: {ARC_Max}, avg: {ARC_Sum/(ARC_count if ARC_count !=0 else 1):.2f}")
        output_file.write("\n-------------------------------------\n")
        output_file.close()


    def destroyHash(self):
        self.students = [None] * self.size
