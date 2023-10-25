duplicate_student={}
student={"Bharathi":"25","muthu":"100","siva":"90","bhabi":"50"}
for key,value in student.items():
    if  int(value)>35:
        duplicate_student[key] = value
print(duplicate_student)
    

    
