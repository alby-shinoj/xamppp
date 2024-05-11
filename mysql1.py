import pymysql
dbcon=pymysql.connect(host='localhost',user='root',password='',db='collage')
cursor=dbcon.cursor()

name=input('enter name:')
regno=int(input('enter reg no:'))
email=input('enter email:')

sqlquery='insert into student values(%s,%s,%s)'
data=(name,regno,email)
cursor.executable(sqlquery,data)
dbcon.commit()
print('data is saved')









