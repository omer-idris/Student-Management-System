import time, os, pandas

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

data_loc = 'D:/Advanced Py/library/lesson 01/students_data.csv'
students = {}

 # تحميل الملف على القاموس للتحقق مباشرة
if os.path.exists(data_loc):
   ds = pandas.read_csv(data_loc)
   for _, row in ds.iterrows():
      students[str(row['student_id'])] = {
         'student_id': str(row['student_id']),
         'name': row['name'],
         'major': row['major'],
         'GPA': float(row['GPA']),
         'status': row['status'],
                                          }
      

clear()
print("""
Student Management System\n
This program manages student records using a CSV file as a database.
It allows the user to:
- Register new students
- Enroll registered students
- Graduate enrolled students
- Search for students by ID, name, or major
- Display all students\n
All student data is stored persistently in a CSV file.    """)


# --------- Displaying function
def display_student(id):
  s = students[id]
  print(f'\nStudent ID: {id}  Name: {s['name']}  Major: {s['major']}  GPA: {s['GPA']}  Status: {s['status']}')

# --------- Registering function
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
    
    with open(data_loc, 'a+') as file:
       file.write(f'\n{student_id},{name},{major},{GPA},registered')

    print(f'Student "{name}" with major "{major}" registered to system with ID "{student_id}".')
    if input('Add another student? y/n ').lower() != 'y':
      break

# --------- Enrolling function
def enroll_student():
    while True:
        clear()
        print('Enrolling a student.... \n')
        student_id = input("Enter the Student ID to enroll: ").strip()

        if student_id in students:
            sdd = students[student_id]
            if sdd['status'] == 'registered':

                sdd['status'] = 'enrolled'
                print(f'Student {sdd["name"]} enrolled successfully....')

                # reload dataframe fresh
                df = pandas.read_csv(data_loc)

                df.loc[df['student_id'] == student_id, 'status'] = 'enrolled'

                df.to_csv(data_loc, index=False)

            elif sdd['status'] == 'enrolled':
                print('Sorry! this student is already enrolled...')
            elif sdd['status'] == 'graduated':
                print('Sorry! this student has already graduated...')
        else:
            print('Student not found in the system.')

        if input('Enroll another student? y/n ').lower() != 'y':
            break

# --------- Graduating function        
def graduate_student():
  while True:
    clear()
    print('Graduating a student.... \n')
    student_id = input('Enter Student ID to graduate: ')

    if student_id in students:
      sdd = students[student_id]
      if sdd['status'] == 'enrolled':

        if input(f'Are you sure you want to graduate {sdd["name"]}? y/n: ') == 'y': # confirm serious actions
            print(f'Congratulations! 🌺 student {sdd["name"]} has graduated successfully')
            sdd['status'] = 'graduated'
        
            # reload dataframe fresh
            df = pandas.read_csv(data_loc)

            df.loc[df['student_id'] == student_id, 'status'] = 'graduated'

            df.to_csv(data_loc, index=False)
      
        else:
            continue
      
      elif sdd['status'] == 'graduated':
        print("Sorry! this student has already graduated.")
      else:
        print("This student hasn't enrolled yet.")

    else:
      print('Student not found in the system.')

    if input('Graduate another student? y/n ').lower() != 'y':
      break


# --------- Searching function
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

# ------ execution code
while True:
  entered = input('''
==== Menu: ====\n
1. Add Student
2. Enroll Student
3. Graduate Student
4. Dispaly all Students
5. Search for Student
6. Exit\n
Enter your choice from 1-6: ''')
  
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
  
  elif entered == '6':
    break
  clear()
