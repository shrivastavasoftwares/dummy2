import pymysql as sql
db=sql.connect(host="localhost",port=3310,user='root',password='',database='demodb')
c=db.cursor()
 

print("hello")


def data_show():
    cmd = "select * from tb1"
    c.execute(cmd)

    data = c.fetchall()

    print(*data)

def show():
    cmd = "select * from tb1"
    c.execute(cmd)
    xy = c.fetchall()
    print(*xy)
def dataenter():
    cmd ="desc tb1"
    x=c.execute(cmd)
    print(x)
def datae():
    x=input("enter name ")
    y=int(input("enter age "))
    cmd = "insert into tb1 values('{}','{}')".format(x,y)
    c.execute(cmd)
    db.commit()




data_show()
print("\n\n\n\n\n\n\n")
show()
print("\n\n\n\n\n\n\n")
datae()

"""def data_entry():
    print("Welcome to data entry ")
    
    name = input("Enter Name : ")
    age = int (input("Enter age : "))
    p_no = int(input("Enter p_no : "))

    cmd = "insert into xyz(name,age,p_no) values('{}','{}','{}')".format(name,age,p_no)
    c.execute(cmd)
    db.commit()"""

