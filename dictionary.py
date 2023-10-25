duplicate_student={}
student={"vasanth":80,"hari":60,"bharathi":90,"anandaraj":20}
for key,value in student.items():
    if  int(value)>30:
        duplicate_student[key] = value
print(duplicate_student)
    

    
