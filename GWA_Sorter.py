#GWA Sorter
#Creates a variable for the student's name and their corresponding GWAs
student_name=""
student_gwa=0
#Reads a file named 20 Students.txt
with open("D:\[CMPE103] OOP\GWA_Sorter\\20 Students") as source:
    lines=source.readlines()
#Since I created a CSV, I can now strip and split the name of the students and their GWAs of commas using the function:
for line in lines:
    name, gwa=line.strip().split(",")
    print(name, gwa)
#If loop comparing the values of the students' GWA
#Print output