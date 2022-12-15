import sqlite3

class demsDatabase:
    def __init__(self,db):
        self.connect = sqlite3.connect(db)
        self.connect.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.connect.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS family(
                famID INTEGER PRIMARY KEY AUTOINCREMENT,
                famName TEXT NOT NULL,
                famAddrss TEXT NOT NULL,
                famCID INTEGER,
                cNumber TEXT
                )""")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS evacuee(
                evacID INTEGER PRIMARY KEY AUTOINCREMENT,
                fName TEXT NOT NULL,
                mi TEXT,
                lName TEXT NOT NULL,
                suffix TEXT,
                cNumber TEXT,
                famID INTEGER NOT NULL,
                FOREIGN KEY (famID) REFERENCES family(famID) ON DELETE RESTRICT
            )
         """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS relief(
                famID INTEGER NOT NULL,
                reliefName TEXT NOT NULL,
                reliefDate TEXT NOT NULL,
                reliefRep INT NOT NULL,
                reliefStatus INTEGER NOT NULL,
                PRIMARY KEY (famID, reliefName),
                FOREIGN KEY (famID) REFERENCES family(famID) ON DELETE RESTRICT
            )         
         """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medassist(
                medreportID INTEGER PRIMARY KEY AUTOINCREMENT,
                famID INTEGER NOT NULL,
                evacID INTEGER NOT NULL,
                fName TEXT NOT NULL,
                lName TEXT NOT NULL,
                medCause TEXT NOT NULL,
                FOREIGN KEY (famID) REFERENCES family(famID) ON DELETE RESTRICT,
                FOREIGN KEY (evacID) REFERENCES evacuee(evacID) ON DELETE RESTRICT
            )         
         """)

        self.connect.commit()

    def idOfLastInsert(self):
        self.cursor.execute("SELECT last_insert_rowid()")
        return self.cursor.fetchone()

#family Table Methods
    def fetchFam(self):
        self.cursor.execute("""
        SELECT f.famID, f.famName, f.famAddrss, f.famCID, f.cNumber, ifnull(e.famSize, 0) as famSize
            FROM family f
            LEFT JOIN (
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
        self.connect.commit() 

    def updateFamily(self, famID, famName, famAddrss, famCID, cNumber):
        self.cursor.execute("""
            UPDATE family 
            SET famName = ?, 
                famAddrss = ?, 
                famCID = ?, 
                cNumber = ? 
            WHERE famID = ?
            """,
            (famName, famAddrss, famCID, cNumber, famID))
        self.connect.commit()
    
    def updateFamContact(self, famID, famCID, cNumber):
        self.cursor.execute("""
            UPDATE family 
            SET famCID = ?, 
                cNumber = ? 
            WHERE famID = ?
            """,
            (famCID, cNumber, famID))
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
        self.connect.commit()  

    def updateEvac(self, evacID, fName, mi, lName, suffix, cNumber, famID):
        self.cursor.execute("""
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
    
    def fetchFullName(self, evacID):
        self.cursor.execute("SELECT fName, lName FROM evacuee WHERE evacID = ?", (evacID,))
        return self.cursor.fetchall()
    
    def updateFamOnUpdateEvac(self, evacID, cNumber):
        #Updates the 
        self.cursor.execute("""
            UPDATE family 
            SET cNumber = ?
            WHERE famCID = ?
            """,
            (cNumber, evacID))
        self.connect.commit()


#Relief Table Methods
    def fetchRelief(self):
         self.cursor.execute("SELECT * FROM relief")
         return self.cursor.fetchall()

    def insertRelief(self, famID, reliefName, reliefDate, reliefRep, reliefStatus):
        self.cursor.execute("INSERT INTO relief (famID, reliefName, reliefDate, reliefRep, reliefStatus) VALUES (?, ?, ?, ?, ?)",
            (famID, reliefName, reliefDate, reliefRep, reliefStatus))
        self.connect.commit() 

    # special rule: if one relief operation row is deleted, all related relief operations will also be deleted
    def removeRelief(self, reliefName, famID):
        self.cursor.execute("DELETE FROM relief WHERE (reliefName = ? AND famID == ?)", (reliefName,famID))
        self.connect.commit()
    
    # let currentDate = new Date().toJSON().slice(0, 10);
    def updateRelief(self, famID, reliefName, reliefDate, reliefRep, reliefStatus):
        self.cursor.execute("""
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
        self.cursor.execute(f'DELETE FROM medassist WHERE medreportID = {medreportID}')
        self.connect.commit()
    
    def updateMed(self, medreportID, famID, evacID, fName, lName, medCause):
        self.cursor.execute("""
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
    
    def updateMedOnUpdateEvac(self, evacID, fName, lName):
        self.cursor.execute("""
            UPDATE medassist 
            SET fName = ?,
                lName = ?
            WHERE evacID = ?
            """,
            (fName, lName, evacID))
        self.connect.commit()
    
    def closeConnection(self):
        self.connect.close()  
