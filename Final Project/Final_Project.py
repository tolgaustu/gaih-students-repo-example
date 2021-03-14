point = 0
q1 = input('What will be the output of the following Python code? \n\nprint("5Yz&".lower())  ')
if q1 == "5yz&":
  point += 10 
q2 = input('What will be the output of the following Python code? \n\nprint("world",5,2,1)?  ')
if q2 == "world 5 2 1":
  point += 10 
q3 = input('What data type is the object below? \n\np= [1,111,"hello",1]  ')
if q3 == "list":
  point += 10 
q4 = input('What gets printed? \n\nprint(type(2/3))  ')
if q4 == "<class 'float'>":
  point += 10 
q5 = input('Let list1 = [3, 4, 5, 18, 5, 22, 1, 2], what is len(list1)?  ')
if q5 == "8":
  point += 10
q6 = input('What will be the output of the following Python code? \n\nx={"X":3, "Y":5, "Z":7}\nprint(sorted(x))  ')
if q6 == "['X', 'Y', 'Z']":
  point += 10 
q7 = input('What will be the output of the following Python code snippet? \n\nf= {"Ahmet":5, "Mehmet":55}\nprint(f["Ahmet"])  ')
if q7 == "5":
  point += 10 
q8 = input('What will be the output of the following Python code?\n\np=(2,3,4,5)\np[1:-1]  ')
if q8 == "(3, 4)":
  point += 10 
q9 = input('What is the data type of (1)?  ')
if q9 == "int":
  point += 10 
q10 = input('What is list("a#b#c#d".split("#"))?  ')
if q10 == "['a', 'b', 'c', 'd']":
  point += 10 

if point <= 50:
  print("UNSUCCESSFUL")
else: print("SUCCESSFUL")
