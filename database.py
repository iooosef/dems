import sqlite3

class Database:
    def __init__(self,db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS family(
                famID INTEGER PRIMARY KEY AUTOINCREMENT,
                famName TEXT NOT NULL,
                famAddrss TEXT NOT NULL,
                famCID INTEGER,
                cNumber TEXT
                FOREIGN KEY (famCID) REFERENCES evacuee(evacID),
                FOREIGN KEY (cNumber) REFERENCES evacuee(cNumber)
                )
        """)
        self.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS evacuee(
                evacID INTEGER PRIMARY KEY AUTOINCREMENT,
                fName TEXT NOT NULL,
                mi TEXT,
                lName TEXT NOT NULL,
                suffix TEXT,
                cNumber TEXT,
                famID INTEGER NOT NULL,
                FOREIGN KEY (famID) REFERENCES family(famID)
            )
         """)
        self.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS relief(
                famID INTEGER NOT NULL,
                reliefName TEXT NOT NULL,
                reliefDate TEXT NOT NULL,
                reliefRep INT NOT NULL,
                reliefStatus INTEGER NOT NULL,
                FOREIGN KEY (famID) REFERENCES family(famID),
                FOREIGN KEY (reliefRep) REFERENCES evacuee(evacID),
                PRIMARY KEY (famID, reliefName)
            )         
         """)
        self.cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS medassist(
                medreportID INTEGER PRIMARY KEY AUTOINCREMENT,
                famID INTEGER NOT NULL,
                evacID INTEGER NOT NULL,
                fName TEXT NOT NULL,
                lName TEXT NOT NULL,
                medCause TEXT NOT NULL,
                FOREIGN KEY (famID) REFERENCES family(famID),
                FOREIGN KEY (evacID) REFERENCES evacuee(evacID),
                FOREIGN KEY (fName) REFERENCES evacuee(fName),
                FOREIGN KEY (lName) REFERENCES evacuee(lName)
            )         
         """)

        self.connect.commit()

#family Table Methods
    def fetchFam(self):
        self.cursor.execute("""--sql
        SELECT f.famID, f.famName, f.famAddrss, f.famCID, f.cNumber, e.famSize
            FROM family f
            INNER JOIN (
                SELECT famID, COUNT(famID) AS famSize
                FROM evacuee
                GROUP BY famid
            ) e USING(famid)        
        """)
        return self.cursor.fetchall()
    
    def insertFam(self, famName, famAddrss, famCID, cNumber):
        self.cursor.execute("INSERT INTO family (famName, famAddrss, famCID, cNumber) VALUES (?, ?, ?, ?)", 
            (famName, famAddrss, famCID, cNumber))
        self.connect.commit()

    def removeFam(self, famID):
        self.cursor.execute(f'DELETE FROM family WHERE famID = {famID}')
        self.connect.close()  

    def updateFamily(self, famID, famName, famAddrss, famCID, cNumber):
        self.cursor.execute("""--sql
            UPDATE family 
            SET famName = ?, 
                famAddrss = ?, 
                famCID = ?, 
                cNumber = ? 
            WHERE famID = ?
            """,
            (famName, famAddrss, famCID, cNumber, famID))
        self.connect.commit()

#Evacuees Table Methods
    def fetchEvac(self):
        self.cursor.execute("SELECT * FROM evacuee")
        return self.cursor.fetchall()
    
    def insertEvac(self, fName, mi, lName, suffix, cNumber, famID):
        self.cursor.execute("INSERT INTO evacuee (fName, mi, lName, suffix, cNumber, famID) VALUES (?, ?, ?, ?, ?, ?)",
            (fName, mi, lName, suffix, cNumber, famID))
        self.connect.commit()

    def removeEvac(self, evacID):
        self.cursor.execute(f'DELETE FROM evacuee WHERE evacID = {evacID}')
        self.connect.close()  

    def updateEvac(self, evacID, fName, mi, lName, suffix, cNumber, famID):
        self.cursor.execute("""--sql
            UPDATE evacuee 
            SET fName = ?, 
                mi = ?, 
                lName = ?, 
                suffix = ?, 
                cNumber = ?, 
                famID = ?
            WHERE evacID = ?
            """,
            (fName, mi, lName, suffix, cNumber, famID, evacID))
        self.connect.commit()

#Relief Table Methods
    def fetchRelief(self):
         self.cursor.execute("SELECT * FROM relief")
         return self.cursor.fetchall()

    def insertRelief(self, reliefName, reliefDate, reliefRep, reliefStatus):
        self.cursor.execute("INSERT INTO relief (reliefName, reliefDate, reliefRep, reliefStatus) VALUES (?, ?, ?, ?)",
            (reliefName, reliefDate, reliefRep, reliefStatus))
        self.connect.commit() 

    # special rule: if one relief operation row is deleted, all related relief operations will also be deleted
    def removeRelief(self, reliefName):
        self.cursor.execute(f'DELETE FROM relief WHERE reliefName = {reliefName}')
        self.connect.close()
    
    # let currentDate = new Date().toJSON().slice(0, 10);
    def updateEvac(self, famID, reliefName, reliefDate, reliefRep, reliefStatus):
        self.cursor.execute("""--sql
            UPDATE relief 
            SET reliefName = ?, 
                reliefDate = ?, 
                reliefRep = ?, 
                reliefStatus = ?
            WHERE famID = ? AND reliefName = ?
            """,
            (reliefName, reliefDate, reliefRep, reliefStatus, famID, reliefName))
        self.connect.commit()

#MedAssist Table Methods
    def fetchMed(self):
         self.cursor.execute("SELECT * FROM medassist")
         return self.cursor.fetchall()

    def insertMed(self, famID, evacID, fName, lName, medCause):
        self.cursor.execute("INSERT INTO medassist (famID, evacID, fName, lName, medCause) VALUES (?, ?, ?, ?, ?)",
            (famID, evacID, fName, lName, medCause))
        self.connect.commit()

    def removeMed(self, medreportID):
        self.cursor.execute(f'DELETE FROM medassist WHERE reliefName = {medreportID}')
        self.connect.close()
    
    def updateMed(self,EvactFName,EvactLName,FamilyID ,MedAssistIssue):
        self.cursor.execute("UPDATE medassist FamilyID=?, EvactID_Rep=?, WHERE ReliefOpID = ?",(EvactFName,EvactLName,FamilyID ,MedAssistIssue ))
        self.connect.commit()
    
    def updateMed(self, medreportID, famID, evacID, fName, lName, medCause):
        self.cursor.execute("""--sql
            UPDATE medassist 
            SET famID = ?, 
                evacID = ?, 
                fName = ?, 
                lName = ?,
                medCause = ?
            WHERE medreportID = ?
            """,
            (famID, evacID, fName, lName, medCause, medreportID))
        self.connect.commit()