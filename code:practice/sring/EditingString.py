#EditingString .py
#
# @ author: Amy
# date: 11.11.22

 
class_size = int(input("Please put your class size\n"))

student =[]

for count in range (0, class_size): #range(0,3) is [0],[1],[2]
    student_name = input("please enter {0} names.".format(count+1))
    student.append(student_name)


                         
    
result_students = ",".join(student)
print(result_students)

swapped_names = result_students.swapcase()
print(swapped_names)

'''
#assertion1.
input:
Please put your class size
3
please enter 1 names."Amy:
please enter 2 names."Jk"
please enter 3 names."Liam"
output:
"Amy:,"Jk","Liam"
"aMY:,"jK","lIAM"
