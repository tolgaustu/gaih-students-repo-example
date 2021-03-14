students = dict()
passingGrade = dict()
studentList = []
for i in range(1,4):
  midterm = input("{}. öğrencinin vize notunu girin:".format(i))
  project = input("{}. öğrencinin proje notunu girin:".format(i))
  final = input("{}. öğrencinin final notunu girin:".format(i))
  students["{}. öğrenci".format(i)] = [midterm, project, final]
  passingGrade["{}. öğrenci".format(i)] = [int(midterm)*0.3 + int(project)*0.3 + int(final)*0.4]

print("Öğrenci notları: ", students)
print("Geçme notları: ", passingGrade)

for key, value in passingGrade.items():
    temp = [key, value]
    studentList.append(temp)

studentList.sort(key = lambda studentList: studentList[1], reverse=True) 
print("Not sıralaması: ", studentList)

