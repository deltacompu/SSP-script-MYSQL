import mysql.connector
class database():

    def InsertPrinter(self):
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Cra48n70a54",
          database="test"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO printers (printer_id , printer_location , printer_status , ticket ) VALUES (%s, %s, %s, %s)"
        val = [('10.243.240.109','1Q04', 'online','no'),
                ('10.243.240.114','1Q16', 'online','no'),
                ('10.243.240.111','1Q15', 'online','no'),
                ('10.243.240.150','1H04', 'online','no'),
                ('10.243.240.167','1N04', 'online','no'),
                ('10.243.240.164','1Q02', 'online','no'),
                ('10.243.240.23','1P02', 'online','no'),
                ('10.243.240.192','1F02', 'online','no'),
                ('10.243.240.101','1Q12', 'online','no'),
                ('10.243.240.24','100', 'online','no'),
                ('10.243.240.18','1J06', 'online','no'),
                ('10.243.240.130','1L06', 'online','no'),
                ('10.243.240.159','1M06', 'online','no'),
                ('10.243.240.15','1T06', 'online','no'),
                ('10.243.240.128','1T07', 'online','no'),
                ('10.243.240.126','1T09', 'online','no'),
                ('10.243.240.42','1T10', 'online','no'),
                ('10.243.240.182','1T11', 'online','no'),
                ('10.243.240.97','1T16', 'online','no'),
                ('10.243.240.102','1Q11', 'online','no'),
                ('10.243.240.149','1T14', 'online','no'),
                ('10.243.240.10','1T13', 'online','no'),
                ('10.243.240.187','1S02', 'online','no'),
                ('10.243.240.168','1R02', 'online','no'),
                ('10.243.240.55','1N02', 'online','no'),
                ('10.243.240.86','1J20', 'online','no'),
                ('10.243.240.209','1J19', 'online','no'),
                ('10.243.240.118','1E09', 'online','no'),
                ('10.243.240.184','1F19', 'online','no'),
                ('10.243.240.138','1D19', 'online','no'),
                ('10.243.240.103','1Q10', 'online','no'),
                ('10.243.240.175','1G19', 'online','no'),
                ('10.243.240.157','1G20', 'online','no'),
                ('10.243.240.47','1N14', 'online','no'),
                ('10.243.240.104','1Q9', 'online','no'),
                ('10.243.240.105','1Q8', 'online','no'),
                ('10.243.240.106','1Q7', 'online','no'),
                ('10.243.240.107','1Q6', 'online','no'),
                ('10.243.240.108','1Q5', 'online','no'),
                ('10.243.244.7','1S4', 'online','no')

               ]
        mycursor.executemany(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


    def findallIPprinter(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cra48n70a54",
            database="test"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select printer_id from printers")
        myresult = mycursor.fetchall()

        return myresult

    def findaprinterlocation(self, ip):
        self.ip=ip
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cra48n70a54",
            database="test"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select printer_location from printers where printer_id='"+self.ip+"';")
        myresult = mycursor.fetchall()
        for x in myresult:
            return x[0]

    def findprinterstatus(self, ip):
        self.ip=ip
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cra48n70a54",
            database="test"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select printer_status from printers where printer_id='"+self.ip+"';")
        myresult = mycursor.fetchall()
        for x in myresult:
            return x[0]

    def updateprinterstatus(self, ip,status):
        self.ip = ip
        self.status = status
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cra48n70a54",
            database="test"
        )
        mycursor = mydb.cursor()
        mycursor.execute("update printers set printer_status='"+self.status+"' where printer_id='" + self.ip + "';")
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

    def findallprinteroffline(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cra48n70a54",
            database="test"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select printer_id  from printers where printer_status = 'offline' ;")
        myresult = mycursor.fetchall()
        return myresult




