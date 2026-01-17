#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#STUDENT MANAGER
class Student:
    def __init__(self):
        self.student={}
    def add(self):
        name=input("ENTER NAME")
        marks=int(input("ENTER MARKS"))
        self.student[name]=marks
    def display(self):
        print(self.student)
    def topper(self):
        topper=max(self.student,keys=self.student.get)
        print("TOPPER ",topper,"MARKS",self.student[topper])
s1=Student()
while True:
    print("\n___MENU___")
    print("1. Add student")
    print("2. Display students")
    print("3. Find topper")
    print("4. Exit")
    choice=int(input("ENTER CHOICE.."))
    if choice == 1:
        s1.add()
    elif choice == 2:
        s1.display()
    elif choice == 3:
        s1.topper()
    elif choice == 4:
        print("EXITING......")
        break
    else:
        print("INVALID CHOICE")

