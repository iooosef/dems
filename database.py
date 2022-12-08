import sqlite3


class Database:
#family Table 
    def Family(self,db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Family(FamilyID INTEGER PRIMARY KEY ,FamilyName TEXT,EvacID_contact INTEGER,EvactContact_contact INTEGER,FamilySize INTEGER")
        self.connect.commit()

    def fetchFam(self):
        self.cursor.execute("SELECT * FROM Family")
        rows = self.cursor.fetchall()
        return rows
    
    def insertFam(self,FamilyName ,EvacID_contact,EvactContact_contact,Sex,FamilySize):
        self.cursor.execute("INSERT INTO Family VALUES (NULL, ?, ?, ?, ?, ?, ?)", 
                            (FamilyName, EvacID_contact, EvactContact_contact, Sex, FamilySize))
        self.conn.commit()

    def removeFam(self,FamilyID):
        self.cursor.execute("DELETE FROM Family WHERE FamilyID=?",(FamilyID,))   
        self.conn.commit()  

    def updateFamily(self,FamilyName ,EvacID_contact,EvactContact_contact,Sex,FamilySize):
        self.cursor.execute("UPDATE Family SET FamilyName=?, EvacID_contact=?, EvactContact_contact=?, FamilySize=?, WHERE FamilyID = ?",
                            (FamilyName, EvacID_contact, EvactContact_contact, Sex, FamilySize))
        self.conn.commit()

    def deleteFamily(self):
        self.conn.close()  

#Evacuees Table 
    def Evacuees(self,db):
         self.connect = sqlite3.connect(db)
         self.cursor = self.connect.cursor()
         self.cursor.execute("CREATE TABLE IF NOT EXISTS Evacuee(EvacID INTEGER PRIMARY KEY ,EvactFName TEXT,EvactLName TEXT,EvacContact INTEGER,FamilyID INTEGER, FOREIGN KEY (FamilyID) REFERENCES Family(FamilyID)")
         self.connect.commit()

    def fetchEvac(self):
        self.cursor.execute("SELECT * FROM Evacuees")
        rows = self.cursor.fetchall()
        return rows
    
    def insertEvac(self,EvactFName ,EvactLName,EvacContact,FamilyID):
        self.cursor.execute("INSERT INTO Evacuees VALUES (NULL, ?, ?, ?, ?, )", 
                            (EvactFName , EvactLName,EvacContact, FamilyID))
        self.connect.commit()

    def removeEvac(self,EvacID):
        self.cursor.execute("DELETE FROM Family WHERE EvacID=?",(EvacID,))   
        self.connect.commit()  

    def updateEvac(self,EvactFName ,EvactLName,EvacContact,FamilyID):
        self.cursor.execute("UPDATE Evacuees EvactFName=?, EvactLName=?, EvacContact_contact=?, FamilyID=?, WHERE EvacID = ?",
                            (EvactFName , EvactLName,EvacContact, FamilyID))
        self.connect.commit()

    def deleteEvac(self):
        self.connect.close()    

#Relief Table
    def Relief(self,db):
         self.connect = sqlite3.connect(db)
         self.cursor = self.connect.cursor()
         self.cursor.execute("CREATE TABLE IF NOT EXISTS Relief(ReliefOpID INTEGER PRIMARY KEY ,FamilyID INTEGER,EvactID_Rep INTEGER,FOREIGN KEY (FamilyID) REFERENCES Evacuee(FamilyID)FOREIGN KEY (EvactID_Rep) REFERENCES Family (FamilyID)")
         self.connect.commit()

    def fetchRelief(self):
         self.cursor.execute("SELECT * FROM Relief")
         rows = self.cursor.fetchall()
         return rows    

    def insertRelief(self,FamilyID ,EvactID_Rep):
        self.cursor.execute("INSERT INTO Relief VALUES (NULL, ?, ?)", 
                            (FamilyID , EvactID_Rep))
        self.connect.commit()  

    def removeRelief(self,ReliefOpID):
        self.cursor.execute("DELETE FROM Family WHERE EvacID=?",(ReliefOpID,))   
        self.connect.commit()  
    
    def updateRelief(self,FamilyID ,EvactID_Rep):
        self.cursor.execute("UPDATE Relief FamilyID=?, EvactID_Rep=?, WHERE ReliefOpID = ?",
                            (FamilyID , EvactID_Rep))
        self.connect.commit()

    def deleteRelief(self):
        self.connect.close()    

#MedAssist Table
    def MedAssist(self,db):
         self.connect = sqlite3.connect(db)
         self.cursor = self.connect.cursor()
         self.cursor.execute("CREATE TABLE IF NOT EXISTS MedAssist(FamilyID INTEGER,EvactID INTEGER,EvactFName TEXT,EvactLName TEXT,MedAssistIssue TEXT FOREIGN KEY (FamilyID) REFERENCES Family(FamilyID)FOREIGN KEY (EvactID) REFERENCES Evacuee(EvactID)")
         self.connect.commit()
    
    def fetchRelief(self):
         self.cursor.execute("SELECT * FROM MedAssist")
         rows = self.cursor.fetchall()
         return rows    

    def insertRelief(self,FamilyID ,EvactID,EvactFName,EvactLName,MedAssistIssue):
        self.cursor.execute("INSERT INTO Relief VALUES (NULL, ?, ?,?,?,?)", 
                            (FamilyID ,EvactID,EvactFName,EvactLName,MedAssistIssue ))
        self.connect.commit()  

    def removeRelief(self,ReliefOpID):
        self.cursor.execute("DELETE FROM Family WHERE ReliefOpID=?",(ReliefOpID,))   
        self.connect.commit()  
    
    def updateRelief(self,FamilyID ,EvactID,EvactFName,EvactLName,MedAssistIssue):
        self.cursor.execute("UPDATE Relief FamilyID=?, EvactID_Rep=?, WHERE ReliefOpID = ?",
                            (FamilyID ,EvactID,EvactFName,EvactLName,MedAssistIssue ))
        self.connect.commit()

    def deleteRelief(self):
        self.connect.close()   
