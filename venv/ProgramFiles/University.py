from ProgramFiles import Student
import csv
records=[]
def addRecord():
    name=input("Enter name:")
    reg=input("Enter registration number:")
    contact=input("Enter contact number:")
    cgpa=input("Enter cgpa:")
    student=Student.Student(name,reg,contact,cgpa)
    records.append(student)
    print("Record added successfully")
def checkRecord():
    reg=input("Enter registration number:")
    for record in records:
        if record.regNo==reg:
            print(record.name)
def exit():
    with open("StudentRecord.csv","w") as file:
        writer=csv.writer(file)
        for i in range(0,len(records)):
            writer.writerow([records[i].name,records[i].regNo,records[i].contact,records[i].cgpa])
    print("Thank you")