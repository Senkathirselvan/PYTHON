duplicate_student={}
student={"Bharathi":"25","muthu":"100","siva":"90","bhabi":"50"}
for key,value in student.items():
    if  int(value)>30:
        duplicate_student[key] = value
print(duplicate_student)
    

    
