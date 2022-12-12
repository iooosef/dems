import sqlite3

class Database:
#family Table 
    def __init__(self,db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Family(FamilyID INTEGER PRIMARY KEY ,FamilyName TEXT,EvacID_contact INTEGER,EvactContact_contact INTEGER,FamilySize INTEGER")
        self.connect.commit()

    def fetchFam(self):
        self.cursor.execute("SELECT * FROM Family")
        rows = self.cursor.fetchall()
        return rows
    
    def insertFam(self,FamilyName ,EvacID_contact,EvactContact_contact,Sex,FamilySize):
        self.cursor.execute("INSERT INTO Family VALUES (NULL, ?, ?, ?, ?)", (FamilyName, EvacID_contact, EvactContact_contact, Sex, FamilySize))
        self.connect.commit()

    def removeFam(self,FamilyID):
        self.cursor.execute("DELETE FROM Family WHERE FamilyID=?",(FamilyID,))   
        self.conn.commit()  

    def updateFamily(self,FamilyName ,EvacID_contact,EvactContact_contact,Sex,FamilySize):
        self.cursor.execute("UPDATE Family SET FamilyName=?, EvacID_contact=?, EvactContact_contact=?, FamilySize=?, WHERE FamilyID = ?",(FamilyName, EvacID_contact, EvactContact_contact, Sex, FamilySize))
        self.conn.commit()

    def deleteFamily(self):
        self.connect.close()  

#Evacuees Table 
    def __init__(self,db):
         self.connect = sqlite3.connect(db)
         self.cursor = self.connect.cursor()
         self.cursor.execute("CREATE TABLE IF NOT EXISTS Evacuee(EvacID INTEGER PRIMARY KEY ,EvactFName TEXT,EvactLName TEXT,EvacContact INTEGER,FamilyID INTEGER, FOREIGN KEY (FamilyID) REFERENCES Family(FamilyID)")
         self.connect.commit()

    def fetchEvac(self):
        self.cursor.execute("SELECT * FROM Evacuees")
        rows = self.cursor.fetchall()
        return rows
    
    def insertEvac(self,EvactFName ,EvactLName,EvacContact,FamilyID):
        self.cursor.execute("INSERT INTO Evacuees VALUES (NULL, ?, ?, ?, ? )", (EvactFName , EvactLName,EvacContact, FamilyID))
        self.connect.commit()

    def removeEvac(self,EvacID):
        self.cursor.execute("DELETE FROM Family WHERE EvacID=?",(EvacID,))   
        self.connect.commit()  

    def updateEvac(self,EvactFName ,EvactLName,EvacContact,FamilyID):
        self.cursor.execute("UPDATE Evacuees EvactFName=?, EvactLName=?, EvacContact_contact=?, FamilyID=?, WHERE EvacID = ?",(EvactFName , EvactLName,EvacContact, FamilyID),)
        self.connect.commit()

    def deleteEvac(self):
        self.connect.close()    

#Relief Table
    def __init__(self,db):
         self.connect = sqlite3.connect(db)
         self.cursor = self.connect.cursor()
         self.cursor.execute("CREATE TABLE IF NOT EXISTS Relief(FamilyID INTEGER PRIMARY KEY, FOREIGN KEY(FamilyID) REFERENCES Evacuee(FamilyID), ReliefOpName TEXT,ReliefOpDate TEXT CURRENT_TIMESTAMP, EvacFname TEXT, FOREIGN KEY (EvacFname) REFERENCES Evacuee(EvacFname), Status TEXT )")
         self.connect.commit()

    def fetchRelief(self):
         self.cursor.execute("SELECT * FROM Relief")
         rows = self.cursor.fetchall()
         return rows    

    def insertRelief(self,ReliefOpName ,ReliefOpDate ,  EvacFname , Status ):
        self.cursor.execute("INSERT INTO Evacuees VALUES (NULL, ?, ?, ?, ? )", (ReliefOpName ,ReliefOpDate,  EvacFname , Status))
        self.connect.commit() 

    def removeRelief(self,ReliefOpID):
        self.cursor.execute("DELETE FROM Family WHERE ReliefOpID=?",(ReliefOpID,))   
        self.connect.commit()  

    def deleteRelief(self):
        self.connect.close()    

#MedAssist Table
    def __init__(self,db):
         self.connect = sqlite3.connect(db)
         self.cursor = self.connect.cursor()
         self.cursor.execute("CREATE TABLE IF NOT EXISTS MedAssist(EvactID INTEGER,FOREIGN KEY (EvactID) REFERENCES Evacuee(EvactID),EvactFName TEXT,FOREIGN KEY (EvactFname) REFERENCES Evacuee(EvactFname),EvactLName TEXT,FOREIGN KEY (EvactLname) REFERENCES Evacuee(EvactLname),FamilyID INTEGER ,FOREIGN KEY (FamilyID) REFERENCES Family(FamilyID),MedAssistIssue TEXT ")
         self.connect.commit()
    
    def fetchMed(self):
         self.cursor.execute("SELECT * FROM MedAssist")
         rows = self.cursor.fetchall()
         return rows    

    def insertMed(self,EvactFName,EvactLName,FamilyID ,MedAssistIssue):
        self.cursor.execute("INSERT INTO Relief VALUES (NULL,?,?,?,?)",  (EvactFName,EvactLName,FamilyID ,MedAssistIssue ))
        self.connect.commit()  

    def removeMed(self,ReliefOpID):
        self.cursor.execute("DELETE FROM Family WHERE ReliefOpID=?",(ReliefOpID,))   
        self.connect.commit()  
    
    def updateMed(self,EvactFName,EvactLName,FamilyID ,MedAssistIssue):
        self.cursor.execute("UPDATE Relief FamilyID=?, EvactID_Rep=?, WHERE ReliefOpID = ?",(EvactFName,EvactLName,FamilyID ,MedAssistIssue ))
        self.connect.commit()

    def deleteRelief(self):
        self.connect.close()   

