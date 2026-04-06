import pickle
import os
def addrecord():
    fh=open("library.dat","wb")
    rec=[]
    n=int(input("Enter no. of entries: "))
    for i in range(1,n+1):
        a=int(input("Enter the book no. : "))
        b=input("Enter the book name : ")
        c=input("Enter the author: ")
        d=input("Enter the publisher : ")
        e=input("Enter the quantity : ")
        f=input("Enter the price : ")
        print("----------------------")
        rec=[a,b,c,d,e,f]
        pickle.dump(rec,fh)
    fh.close()
def displayrecord():
    print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format("Book no.","Bookname","Author","Publisher","Quantity","Price"))
    fh=open("library.dat","rb")
    try:
        while True:
             rec=pickle.load(fh)
             print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]))
    except EOFError:
        print("Error")
    fh.close()
def bookno():
    b1 = int(input("Enter the required book no.: "))
    print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format("Book no.","Bookname","Author","Publisher","Quantity","Price"))
    fh=open("library.dat","rb")
    try:
        while True:
            rec=pickle.load(fh)
            if b1==rec[0]:
                print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]))
                break
    except EOFError:
        pass
    fh.close()
def bookname():
    b2 = input("Enter the required book name: ")
    print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format("Book no.","Bookname","Author","Publisher","Quantity","Price"))
    fh=open("library.dat","rb")
    try:
        while True:
            rec=pickle.load(fh)
            if rec[1]==b2:
                print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]))
    except EOFError:
        pass
    fh.close()
def author():
    b3 = input("Enter the required author name: ")
    print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format("Book no.","Bookname","Author","Publisher","Quantity","Price"))
    fh=open("library.dat","rb")
    try:
        while True:
            rec=pickle.load(fh)
            if rec[2]==b3:
                print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]))
    except EOFError:
        pass
    fh.close()
def nil():
    print("Books whose quantity is zero:")
    fh=open("library.dat","rb")
    try:
        while True:
            rec=pickle.load(fh)
            if rec[5]=="0":
                print(rec[1]+", ")
    except EOFError:
        pass
    fh.close()
def dlt():
    fh=open("library.dat","rb")
    fh1=open("temp.dat","wb")
    a=int(input("Enter book no.: "))
    f=0
    try:
        while True:
            rec=pickle.load(fh)
            if rec[0]==a:
                f=1
            else:
                pickle.dump(rec,fh1)
    except EOFError:
        pass
    fh.close()
    fh1.close()
    os.remove("library.dat")
    os.rename("temp.dat","library.dat")
    def d():
        fh=open("library.dat","rb")
        print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format("Book no.","Bookname","Author","Publisher","Quantity","Price"))
        try:
            while True:
                r=pickle.load(fh)
                print("{0:<17}{1:18}{2:16}{3:19}{4:8}{5:>15}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
        except EOFError:
            pass
    d()
def modify():
    def bookno():
        fh=open("library.dat","rb+")
        n=int(input("Enter the book number whose details need to be modified: "))
        f=0
        pos=0
        try:
            while True:
                data = pickle.load(fh)
                if n==int(data[0]):
                    fh.seek(pos)
                    print("** Before modifying ** :",data)
                    data[1]=input("Enter the new name: ")
                    data[2]=input("Enter the new authr: ")
                    data[3]=input("Enter the new pub: ")
                    data[4]=input("Enter the new qty: ")
                    data[5]=input("Enter the new price: ")
                    print(data[1])
                    pickle.dump(data,fh)
                    f=1
                    break
                else:
                    pos= fh.tell()
        except EOFError:
            pass
        fh.close()
        print("Modified !")
    def update():
        fh=open("library.dat","rb")
        try:
            while True:
                k=pickle.load(fh)
                a=int(k[5])
                a=a+a*0.05
                k[5]=a
        except EOFError:
            pass
        fh.close()
        f1=open("library.dat","ab")
        pickle.dump(k,f1)
        f1.close()
        f1=open("library.dat","rb")
        p1=pickle.load(f1)
        print(p1)
        f1.close()
    print("Press 1 for modifying")
    print("Press 2 for updating prices")
    choice=int(input("Enter choice: "))
    if choice==1:
            bookno()
    elif choice==2:
            update()
    else:
            print("Wrong choice")
while True:
    print("Press 1 for adding students")
    print("Press 2 for viewing students")
    print("Press 3 to display details of a book from book no.")
    print("Press 4 to display details of the book from the book name")
    print("Press 5 to display books written by a author")
    print("Press 6 to display books whose price is 0")
    print("Press 7 to delete details of a book")
    print("Press 8 to modify or update")
    a=int(input("Enter your choice: "))
    if a==1:
        addrecord()
    elif a==2:
        displayrecord()
    elif a==3:
        bookno()
    elif a==4:
        bookname()
    elif a==5:
        author()
    elif a==6:
        nil()
    elif a==7:
        dlt()
    elif a==8:
        modify()
