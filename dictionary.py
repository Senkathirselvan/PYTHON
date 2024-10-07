duplicate_student={}
student={"vasanth":80,"hari":60,"bharathi":90,"anandaraj":20}
for key,value in student.items():
    if  int(value)>30:
        duplicate_student[key] = value
print(duplicate_student)
    
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'prabha'
Dict[2] = 'karan'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Prabha'}}
print("\nAdding a Nested Key: ")
print(Dict)

    
