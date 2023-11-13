class Book:

    def __init__(self,id,name,quantity) -> None:
        self.book_id=id
        self.book_name=name
        self.quantity=quantity

class User:

    def __init__(self,id,name,password) -> None:
        self.user_id=id
        self.name=name
        self.password=password

class Library:

    def __init__(self,name) -> None:
        self.library_name=name
        self.Users=[]
        self.Books=[]

    def add_user(self,user_obj):
        # user_obj=User(id,name,password)
        self.Users.append(user_obj)
    def add_book(self,book_obj):
        # book_obj=Book(id,name,quantity)
        self.Books.append(book_obj)

def make_user_obj():

    id=int(input("Enter user id : "))
    name=input("Enter user name : ")
    password=input("Enter user password : ")
    print (f"added user : {name} is sucessfully!!")
    return User(id,name,password)

def make_book_obj():
    id=int(input("Enter the book id : "))
    name=input("Enter the name of  newly adding book : ")
    quantity=int(input("Enter the quantity of books : "))
    print (f"added book : {name} is sucessfully!!")
    return Book(id,name,quantity)

BSK=Library('Bishwo Shahitto Kendro')
book_obj=make_book_obj()
BSK.add_book(book_obj)
user_obj=make_user_obj()
BSK.add_user(user_obj)

currentUser=None

while True:

    if currentUser is None:
        print("No user Loging yet!!")
        option=input("Enter your option, login(L) /Register(R) :  ")

        if option=='L':
            id=int(input("Enter your Library Id : "))
            password=input("Enter your library password ")

            flag=False
            for user in BSK.Users:
                if id==user.user_id and password==user.password:
                    currentUser=user
                    flag=True
                    break
            if flag==False :
                print("Either password or Id is wrong, Try again,Please!!")
        elif option=='R':
            # id=int(input("Enter your Library Id : "))
            # password=input("Enter your library password ") 
            new_user_obj=make_user_obj()
            BSK.add_user(new_user_obj)
    else :
        
        if currentUser.name =='admin':
            print("welcome to admin page")
            print("Select your option please\n")
            print("1. for Add Book")
            print("2. for Add User")
            print("3. show all user")
            print("4. Log Out")
            choice=int(input("Enter your choice : "))
            if choice==1:
                new_book_obj=make_book_obj()
                BSK.add_book(new_book_obj)
            elif choice==2:
                new_user_obj=make_user_obj()
                BSK.add_user(new_user_obj)
            elif choice==3:

                for name in BSK.Users:
                    print(name.user_id ,name.name )
            elif choice==4:
                break
        else :
            print("Normal is underprivliliged")
            break


