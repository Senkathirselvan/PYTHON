duplicate_student={}
student={"Bharathi":"25","Hari":"100","Muthu":"90","Ram":"50"}
for key,value in student.items():
    if  int(value)>40:
        duplicate_student[key] = value
print(duplicate_student)
    

    
