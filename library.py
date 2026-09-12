import mysql.connector

# Establish connection with MySQL database
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='HIMANIDHAWAN10846',
    database='library'
)
mycursor = con.cursor()

def donatebook():
    bookname = input('enter name of book you want to donate:')
    authorname = input('enter name of author:')
    bookcode = input('enter code of book:')
    total = int(input('how many copies of the book you want to donate:'))
    print('what to make more donation?')
    a = input('enter your choice y for yes and n for no :')
    if a == 'y':
        donatebook()
    if a == 'n':
        mycursor = con.cursor()
        sql = "INSERT INTO books (bookname, authorname, bookcode, total) VALUES(%s, %s, %s, %s)"
        val = (bookname, authorname, bookcode, total)
        mycursor.execute(sql, val)
        con.commit()
        print('THANKS FOR YOUR SUPPORT')

def deletebook():
    bookcode = int(input('enter book code:'))
    a = 'delete from books where bookcode = %s;'
    data = (bookcode,)
    c = con.cursor()
    c.execute(a, data)
    con.commit()
    print('book deleted successfully')

def issuebook():
    bookname = input('enter name of the book:')
    studentname = input('enter name of the student :')
    bookcode = int(input('enter book code:'))
    issuedate = input('enter date:')
    print("WOULD YOU LIKE TO ISSUE ANOTHER BOOK ?")
    a = input('Enter y for yes and n for no:')
    if a == 'y':
        issuebook()
    elif a == 'n':
        mycursor = con.cursor()
        sql = 'insert into issue (bookname, bookcode, studentname, issuedate) values(%s, %s, %s, %s)'
        val = (bookname, bookcode, studentname, issuedate)
        mycursor.execute(sql, val)
        con.commit()
        print('book issued')
    else:
        print('invalid response')

def issuedbooks():
    mycursor = con.cursor()
    mycursor.execute('select * from issue')
    myrecords = mycursor.fetchall()
    no_rec = mycursor.rowcount
    print('total no. of entries found are:', no_rec)
    for x in myrecords:
        print(x)

def returnbook():
    bookname = input('enter name of the book:')
    studentname = input('enter name of the student :')
    bookcode = int(input('enter book code:'))
    returndate = input('enter date:')
    print("WOULD YOU LIKE TO RETURN ANOTHER BOOK?")
    a = input('Enter y for yes and n for no:')
    if a == 'y':
        returnbook()
    elif a == 'n':
        mycursor = con.cursor()
        sql = 'insert into `return` (bookname, bookcode, studentname, returndate) values(%s, %s, %s, %s)'
        val = (bookname, bookcode, studentname, returndate)
        mycursor.execute(sql, val)
        con.commit()
        print('BOOK RETURNED THANKYOU ')
    else:
        print('INVALID RESPONSE')

def returnedbooks():
    mycursor = con.cursor()
    mycursor.execute('select * from `return`')
    myrecords = mycursor.fetchall()
    no_rec = mycursor.rowcount
    print('total no. of entries found are:', no_rec)
    for x in myrecords:
        print(x)

def displaybooks():
    mycursor = con.cursor()
    mycursor.execute('select * from books')
    myrecords = mycursor.fetchall()
    no_rec = mycursor.rowcount
    print('total no. of books found are:', no_rec)
    for x in myrecords:
        print(x)

def exit():
    for i in range(1):
        break

def choice():
    user_choice = input('enter your choice (1-8):')
    if user_choice == '1':
        donatebook()
    elif user_choice == '2':
        deletebook()
    elif user_choice == '3':
        issuebook()
    elif user_choice == '4':
        issuedbooks()
    elif user_choice == '5':
        returnbook()
    elif user_choice == '6':
        returnedbooks()
    elif user_choice == '7':
        displaybooks()
    elif user_choice == '8':
        exit()
    else:
        print('invalid choice')
        choice()

def intro():
    print('HELLO USER welcome to our family')
    print('giving is not just about making a donation, it is must making difference')
    print('whatever the cost of our libraries the price is cheap compared to that of an ignorant nation')
    print('choose your choice wisely:')
    print("""
    1. DONATE BOOK
    2. DELETE BOOK
    3. ISSUE BOOK
    4. SHOW ISSUED BOOKS
    5. RETURN BOOK
    6. RETURNED BOOKS
    7. DISPLAY BOOKS
    LIBRARY MANAGER
    8. EXIT PROGRAM""")
    choice()

def password():
    pwd = input('enter password:')
    if pwd == 'nvps':
        intro()
    else:
        password()

# Program entry point
password()
