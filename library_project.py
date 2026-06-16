import mysql.connector
class Library:
    def __init__(self):
     self.mydb=mysql.connector.connect(host='localhost',user='root',password='manigoud',database="library")
     self.cursor=self.mydb.cursor()
    def menu(self):
     while True:
        print('\n===========LIBRARY Menu===========')
        print('1.add book')
        print('2.view books')
        print('3.search book')
        print('4.update book')
        print('5.delete book')
        print('6.exit')
        choice=input('enter option:').strip()
        if choice=='1':
            self.add_book()
        elif choice=='2':
            self.view_book()
        elif choice=="3":
            self.search_book()    
        elif choice=='4':
            self.update_book()
        elif choice=='5':
            self.delete_book()
        elif choice=='6':
            print('thank you') 
            break   
        else:
            print('invalid choice')   
    def add_book(self):
        book_name=input('enter book name:')
        author=input('enter author name:')
        price=float(input('enter price:'))
        status=input('enter status:')
        query="INSERT INTO books (book_name,author,price,status) values(%s,%s,%s,%s)"
        values=(book_name,author,price,status)
        self.cursor.execute(query,values)
        self.mydb.commit()
        print('added succesfully')
    def view_book(self):
        self.cursor.execute("select * from books")    
        result=self.cursor.fetchall()
        for i in result:
            print(i)
    def search_book(self):
        search_book=input('enter book name:')
        query="select * from books where book_name=%s"
        self.cursor.execute(query,(search_book,))
        result=self.cursor.fetchall()
        if result:
            for i in result:
                print(i)
        else:
                print('book not found')    
    def  update_book(self):
        oldname=input('enter old name:')
        newname=input('enter new name:')
        author = input('enter new author:')
        price = float(input('enter new price:'))
        status = input('enter new status:')
        query="update books set book_name=%s,author=%s,price=%s,status=%s where book_name=%s"
        values=(newname, author, price, status, oldname)
        self.cursor.execute(query,values)      
        self.mydb.commit()
        print('updated succesfully')    
    def delete_book(self):
        book_name=input('enter book name:')
        query="delete from books where book_name=%s"
        values=(book_name,)
        self.cursor.execute(query,values)
        if self.cursor.rowcount>0:
            print('book deleted succesfully')
        else:
            print('book not found')    
        self.mydb.commit()
if __name__ == "__main__":
 l=Library()
 l.menu()
