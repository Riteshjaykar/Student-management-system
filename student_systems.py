import mysql.connector 

def connect():
    return mysql.connector.connect(
    host="Select your host",
    user="Add your username like: root,xyz",
    password="Add your password",
    database="Add database name "
)

def menu():
        print('''\n<<< STUDENT RESULT MANAGEMENT SYSTEM >>>
      
        1. Add Student
        2. View All Student
        3. Search Student By name
        4. Update Student marks
        5. Delete Student
        6. Exit
            ''')

        choice=input('Enter your choice (1-6) : ')
        return choice

def add_student():
      conn=connect()
      c=conn.cursor()

      name=input('\nEnter Student Name : ')
      marks =input('\nEnter Student marks :')

      query="insert into student(name,marks) values(%s,%s)"
      data=(name,marks)

      c.execute(query,data)
      conn.commit()

      print('\nStudent Record added successfully !✅')
      conn.close()

def View_data():
      conn=connect()
      c=conn.cursor()

      query="select *from student"
      c.execute(query)
      print("\nAll Student record :")
      for i in c.fetchall():
            print(i)
      conn.commit()
      conn.close()

def search_student():
      conn=connect()
      c=conn.cursor()

      name=input('Search Student Name :')
      query="select *from student where name=%s "
      c.execute(query, (name, ))

      result=c.fetchall()
      if result:
            print('\nMatching student(s)🔍: ')
            for i in result:
                  print(i)
            print("\nStudent Search Successfully ✅")
      else:
            print('\nNo Student found with that name !❌ ')
      conn.close()

def update_marks():
      conn=connect()
      c=conn.cursor()

      name=input(('\nEnter Student name : '))
      marks=int(input('\nEnter the updated marks: '))

      query="update student set marks=%s where name=%s"
      c.execute(query,(marks,name))
      conn.commit()

      if c.rowcount>0:
            print(f'\nMarks Update successfully of {name} !✅')
      else:
            print('\nNo Student found with that name !❌')

      conn.close()

def delete_data():
      conn=connect()
      c=conn.cursor()
      print('\nAttention The name of student you are providing now is going to be deleted ')
      name=input('\nEnter Student name : ')
      query="delete from student where name=%s"
      c.execute(query, (name,))
      conn.commit()

      if c.rowcount>0:
            print(' \nStudent Record deleted successfully !✅')
      else:
            print('\nNo Student Found with That name ❌')

while True:
      choice=menu()
      if choice=='1':
            add_student()
      elif choice=='2':
            View_data()
      elif choice=='3':  
            search_student()
      elif choice=='4':
            update_marks()
      elif choice=='5':
            delete_data()
      elif choice=='6':
            print('Thank you !🙏 for Using STUDENT RESULT MANAGEMENT SYSTEM ')
            break
      else:
            print('\nInvalid input ! please Try again later !!❌')

