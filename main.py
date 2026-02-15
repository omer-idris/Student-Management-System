import time, os, random

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
clear()

print('*** Student Management System ***\n\nDescription:\nThis project is about a student management system, you will be able to add, enroll and graduate students.')

students = {}

def display_student(id):
  s = students[id]
  print(f'\nStudent ID: {id}  Name: {s['name']}  Major: {s['major']}  GPA: {s['GPA']}  Status: {s['status']}')
 
def register_student():
  clear()
  while True:
    print('Registering a student.... \n')
     # نتحقق من المدخل وعدم تكراره
    while True:
        student_id = input("Enter Student ID: ").strip()
        if student_id:
            if student_id in students:
                print('This student is already registered. Please.')
            else:
               break
        else:
           print('Input cannot be empty.')

    name = input('Enter name: ').title()
    while not name: name = input('Name is required!\nEnter name: ').title()
    major = input('Enter major: ').title()
    while not major: major = input('Major is required!\nEnter major: ').title()

      # Getting GPA...
    while True:
        try:
            GPA = float(input(f'What is {name} GPA? '))
            if 0 <= GPA <= 4:
              break # break the inner loop
            else:
               print('GPA must be between 0 and 4.')
        except ValueError:
            print('Please enter only numbers')

    students[student_id] = {
      'student_id': student_id,
      'name': name,
      'major': major,
      'GPA': round(GPA,2),
      'status': 'registered'}
    print(f'Student "{name}" with major "{major}" registered to system with ID "{student_id}".')
    if input('Add another student? y/n ').lower() != 'y':
      break

def enroll_student():
  while True:
    clear()
    print('Enrolling a student.... \n')
    student_id = input("Enter the Student ID to enroll: ")
    if student_id in students:
      if students[student_id]['status'] == 'registered':
        print(f'Student {students[student_id]["name"]} enrolled successfully....')
        students[student_id]['status'] = 'enrolled'
      elif students[student_id]['status'] == 'enrolled':
        print('Sorry! this student is already enrolled...')
      elif students[student_id]['status'] == 'graduated':
        print('Sorry! this student has already graduated...')

    else:
        print('Student not found in the system.')
    if input('Enroll another student? y/n ').lower() != 'y':
      break

def graduate_student():
  while True:
    clear()
    print('Graduating a student.... \n')
    student_id = input('Enter Student ID to graduate: ')
      # رحلة البحث عن عروس 🥳😂
    if student_id in students:
      sdd = students[student_id] # to make things shorter
      if sdd['status'] == 'graduated':
        print("Sorry! this student has already graduated.")
      elif sdd['status'] == 'enrolled':
        if input(f'Are you sure you want to graduate {sdd["name"]}? y/n: ') == 'y': # confirm serious actions
            print(f'Congratulations! 🌺 student {sdd["name"]} has graduated successfully')
            sdd['status'] = 'graduated'
        else:
            continue
      else:
        print("This student hasn't enrolled yet.")
    else:
      print('Student not found in the system.')

    if input('Graduate another student? y/n ').lower() != 'y':
      break


def search_student():
    while True:
        found = [] 
        Search_by = input('\nSearch by:\n1. ID\n2. Name\n3. Major\n\nEnter from 1-3: ')
        if Search_by == '1':
            Search_ID = input('Enter student ID to search please: ').strip()
            if Search_ID in students:
               found.append(Search_ID)

        elif Search_by == '2':
            Search_Name = input('Enter student name to search please: ').title()
            for i in students:
                if students[i]['name'] == Search_Name:
                   found.append(i)

        elif Search_by == '3':
            Search_Major = input('Enter student major to search please: ').title()
            for i in students:
                if students[i]['major'] == Search_Major:
                   found.append(i)
        else:
            print('Wrong input!')

        if found:
           print('Found Students:')
           for i in found:
              display_student(i)
           print('_'*29)
        else:
               print('No students found.')

        if input('Search for another student? y/n ').lower() != 'y':
            break

while True:
  clear()
  entered = input('''
==== Menu: ====\n
1. Add Student
2. Enroll Student
3. Graduate Student
4. Dispaly all Students
5. Search for Student
6. Edit Student Info
7. Exit\n
Enter your choice from 1-7: ''')
  
  if entered == '1':
    register_student()

  elif entered == '2':
    enroll_student()

  elif entered == '3':
    graduate_student()

  elif entered == '4':
    clear()
    for i in students:
      display_student(i)
    print('_'*29)
    input('\npress enter to see the menu....')
  
  elif entered == '5':
     search_student()

  # elif entered == '6':
  #    edit_student()
  
  elif entered == '7':
    break
  
