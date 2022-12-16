import sqlite3

class demsDatabase:
    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.connect.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.connect.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS family(
                famID INTEGER PRIMARY KEY AUTOINCREMENT,
                famName TEXT NOT NULL,
                famAddrss TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS evacuee(
                evacID INTEGER PRIMARY KEY AUTOINCREMENT,
                fName TEXT NOT NULL,
                mi TEXT,
                lName TEXT NOT NULL,
                suffix TEXT,
                cNumber TEXT,
                famID INTEGER NOT NULL,
                FOREIGN KEY (famID) REFERENCES family(famID) ON UPDATE CASCADE ON DELETE RESTRICT
            )
         """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS emergencycontact(
				famID INTEGER PRIMARY KEY,
  				evacID INTEGER DEFAULT '',
  				FOREIGN KEY (famID) REFERENCES family(famID) ON UPDATE CASCADE ON DELETE CASCADE
            )
         """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS relief(
                famID INTEGER NOT NULL,
                reliefName TEXT NOT NULL,
                reliefDate TEXT NOT NULL,
                evacID INT,
                reliefStatus INTEGER DEFAULT 0 NOT NULL,
                PRIMARY KEY (famID, reliefName),
                FOREIGN KEY (famID) REFERENCES family(famID) ON UPDATE CASCADE ON DELETE RESTRICT
            )         
         """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medassist(
                medreportID INTEGER PRIMARY KEY AUTOINCREMENT,
                famID INTEGER NOT NULL,
                evacID INTEGER NOT NULL,
                medCause TEXT NOT NULL,
                FOREIGN KEY (famID) REFERENCES family(famID) ON UPDATE CASCADE ON DELETE RESTRICT,
                FOREIGN KEY (evacID) REFERENCES evacuee(evacID) ON UPDATE CASCADE ON DELETE RESTRICT
            )         
         """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS evaccenter(
                indexkey INTEGER PRIMARY KEY AUTOINCREMENT,
                evaccentername TEXT DEFAULT "Evacuation Center" NOT NULL
            )         
         """)
        try:
            self.cursor.execute("INSERT INTO evaccenter (evaccentername) VALUES ('Evacuation Center')")
            self.connect.commit()
            self.cursor.execute("SELECT count(*) FROM evaccenter")
            ecenterCount = self.cursor.fetchone()
            if(ecenterCount[0] > 1):
                self.cursor.execute("DELETE FROM evaccenter WHERE indexkey > 1")
                self.connect.commit() 
        except:
            pass
    
    def closeConnection(self):
        self.connect.close()  

    def idOfLastInsert(self):
        self.cursor.execute("SELECT last_insert_rowid()")
        return self.cursor.fetchone()

#Evacuation Center Info Table Methods ----------------------------------------------------------------------
    def fetchEvacCenter(self):
        self.cursor.execute("SELECT evaccentername FROM evaccenter WHERE indexkey = 1")
        return self.cursor.fetchone()

    def updateEvacCenter(self, nameUpdate):
        self.cursor.execute("UPDATE evaccenter SET evaccentername = ?  WHERE indexkey = 1", (nameUpdate,))
        self.connect.commit()
        self.cursor.execute("SELECT count(*) FROM evaccenter")
        ecenterCount = self.cursor.fetchone()
        if(ecenterCount[0] > 1):
            self.cursor.execute("DELETE FROM evaccenter WHERE indexkey > 1")
            self.connect.commit() 
        

#family Table Methods ----------------------------------------------------------------------
    def fetchFam(self):
        self.cursor.execute("""
        SELECT fam.famid, fam.famname, fam.famaddrss, emc.evacid, emc.fname || ' ' || emc.lname "contactName", emc.cnumber, fam.famsize
        FROM (
            SELECT f.famID, f.famName, f.famAddrss, ifnull(e.famSize, 0) as famSize
            FROM family f
            LEFT JOIN (
                SELECT famID, COUNT(famID) AS famSize
                FROM evacuee
                GROUP BY famid
                ) e USING(famid)
        ) fam
        LEFT JOIN (            
            SELECT ec.famid, ec.evacid, ev.fname, ev.lname, ev.cnumber
            FROM emergencycontact ec
            INNER JOIN evacuee ev
            USING (evacid)
        ) emc 
        USING (famID)
        """)
        return self.cursor.fetchall()
    
    def insertFam(self, famName, famAddrss):
        self.cursor.execute("INSERT INTO family (famName, famAddrss) VALUES (?, ?)", 
            (famName, famAddrss))
        self.connect.commit()

    def removeFam(self, famID):
        self.cursor.execute("DELETE FROM family WHERE [famID] = ?", (famID,))
        self.connect.commit() 

    def updateFamily(self, famID, famName, famAddrss):
        self.cursor.execute("""
            UPDATE family 
            SET famName = ?, 
                famAddrss = ?
            WHERE famID = ?
            """,
            (famName, famAddrss, famID))
        self.connect.commit()

#Evacuees Table Methods ----------------------------------------------------------------------
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
        self.cursor.execute("SELECT fName || ' ' || lName AS 'fullName' FROM evacuee WHERE evacID = ?", (evacID,))
        return self.cursor.fetchall()

#Relief Table Methods ----------------------------------------------------------------------
    def fetchRelief(self):
         self.cursor.execute("""
         SELECT r.famID, r.reliefName, r.reliefDate, ev.evacID, ev.fName || ' ' || ev.lName AS 'reliefRepName', r.reliefStatus
            FROM relief r
            LEFT JOIN evacuee ev
            USING (evacID)
         """)
         return self.cursor.fetchall()

    def insertRelief(self, famID, reliefName, reliefDate, evacID, reliefStatus):
        self.cursor.execute("INSERT INTO relief (famID, reliefName, reliefDate, evacID, reliefStatus) VALUES (?, ?, ?, ?, ?)",
            (famID, reliefName, reliefDate, evacID, reliefStatus))
        self.connect.commit() 

    def removeRelief(self, reliefName, famID):
        self.cursor.execute("DELETE FROM relief WHERE (reliefName = ? AND famID == ?)", (reliefName,famID))
        self.connect.commit()
    
    # let currentDate = new Date().toJSON().slice(0, 10);
    def updateRelief(self, famID, reliefName, reliefDate, evacID, reliefStatus):
        self.cursor.execute("""
            UPDATE relief 
            SET reliefName = ?, 
                reliefDate = ?, 
                evacID = ?, 
                reliefStatus = ?
            WHERE famID = ? AND reliefName = ?
            """,
            (reliefName, reliefDate, evacID, reliefStatus, famID, reliefName))
        self.connect.commit()

#MedAssist Table Methods ----------------------------------------------------------------------
    def fetchMed(self):
         self.cursor.execute("""
            SELECT med.medreportID, med.famID, ev.evacID, ev.fName || ' ' || ev.lName AS 'evacueeName', med.medCause
                FROM medassist med
                INNER JOIN evacuee ev
                USING (evacID)
        """)
         return self.cursor.fetchall()

    def insertMed(self, famID, evacID, medCause):
        self.cursor.execute("INSERT INTO medassist (famID, evacID, medCause) VALUES (?, ?, ?)",
            (famID, evacID, medCause))
        self.connect.commit()

    def removeMed(self, medreportID):
        self.cursor.execute(f'DELETE FROM medassist WHERE medreportID = {medreportID}')
        self.connect.commit()
    
    def updateMed(self, medreportID, famID, evacID, medCause):
        self.cursor.execute("""
            UPDATE medassist 
            SET famID = ?, 
                evacID = ?, 
                medCause = ?
            WHERE medreportID = ?
            """,
            (famID, evacID, medCause, medreportID))
        self.connect.commit()

#EmergencyContact Table Methods ----------------------------------------------------------------------
    def insertEContact(self, famID, evacID):
        self.cursor.execute("INSERT INTO emergencycontact (famID, evacID) VALUES (?, ?)",
            (famID, evacID))
        self.connect.commit()

    def removeEContact(self, famID):
        self.cursor.execute(f'DELETE FROM emergencycontact WHERE famID = {famID}')
        self.connect.commit()
    
    def updateEContact(self, famID, evacID):
        self.cursor.execute("""
            UPDATE emergencycontact 
                SET evacID = ?
                WHERE famID = ?
            """,
            (evacID, famID))
        self.connect.commit()
    
