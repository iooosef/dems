import sys
import platform
import eel 
import json
from datetime import datetime
from database import demsDatabase

# Expected format of data fetched from DB to be passed to front-end
sampleDB = {
    'db_evacuees' : [
        (1,'Josence','C','Parayaoan','','09123456789',1),
        (2,'Joseph','C','Parayaoan','','09123456781',1),
        (3,'Clarence','C','Parayaoan','','09123456782',1),
        (4,'Primitivo','M','Parayaoan','Jr.','09123456783',1),
        (5,'Rosemarie','C','Parayaoan','','09123456784',1),
        (6,'Juan','DL','Dela Cruz','Sr.','09123456785',2),
        (7,'Maria','S','Dela Cruz','','09123456786',2),
        (8,'Mark','H','Sierra','III','09123456787',3),
        (9,'Anna','L','Sierra','','09123456788',3),
        (10,'Kyle','L','Sierra','','',3),
        (11,'Tina','L','Sierra','','09123456789',3),
        (12,'Derek','R','Martin','','09123456791',4),
        (13,'Shiela','Q','Martin','','09123456792',4),
        (14,'James','Q','Martin','','09123456793',4),
        (15,'Sheena','Q','Martin','','09123456794',4)
    ],
    'db_families' : [
        (1, 'Parayaoan', '16 7th St., Youngstown Vill., Cainta, Rizal', 4, '09123456783', 5),
        (2, 'Dela Cruz', 'Salakdwa Vill., Cainta, Rizal', 6, '09123456785', 2),
        (3, 'Sierra', '28 Kalawakan St., World, Moon', 8, '09123456787', 4),
        (4, 'Martin', 'Cavite, Laguna, Batangas, Rizal, Quezon', 12, '09123456787', 4)
    ],
    'db_medAssist' : [
        (0, 1, 1, 'Joseph Clarence', 'Parayaoan', 'Pneumonia'),
        (1, 3, 8, 'Mark', 'Sierra', 'Fever')
    ],
    'db_relief' : [
        (1, 'R0001', '2022-07-22', 3, 1),
        (2, 'R0001', '2022-07-22', 6, 1),
        (3, 'R0001', '2022-07-22', 8, 1),
        (4, 'R0001', '2022-07-22', 12, 1),
        (1, 'R0002', '2022-08-22', 3, 1),
        (2, 'R0002', '2022-08-22', 6, 1),
        (3, 'R0002', '2022-08-22', 8, 0),
        (4, 'R0002', '2022-08-22', 12, 1),
        (1, 'R0003', '2022-09-22', 3, 0),
        (2, 'R0003', '2022-09-22', 6, 0),
        (3, 'R0003', '2022-09-22', 8, 1),
        (4, 'R0003', '2022-09-22', 12, 0)
    ]
}
evacDBpy = 'San Juan Elementary School'

def sqliteTableToJSON(table):
    jsonTable = []
    jsonRow = {}
    for row in sampleDB[table]:
        fields = {
            'db_evacuees': ('evacID','fName','mi','lName','suffix','cNumber','famID'),
            'db_families': ('famID','famName','famAddrss','famCID','cNumber','famSize'),
            'db_medAssist': ('medreportID','famID','evacID','fName','lName','medCause'),
            'db_relief': ('famID','reliefName','reliefDate','reliefRep','reliefStatus')
        }
        for index, field in enumerate(fields[table]):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    return json.dumps(jsonTable)

def sqliteEvacToJSON():
    jsonTable = []
    jsonRow = {}
    for row in demsDatabase.fetchEvac():
        for index, field in enumerate(('evacID','fName','mi','lName','suffix','cNumber','famID')):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    return json.dumps(jsonTable)

def sqliteFamToJSON():
    jsonTable = []
    jsonRow = {}
    # print(demsDatabase.fetchFam())
    for row in demsDatabase.fetchFam():
        for index, field in enumerate(('famID','famName','famAddrss','evacID','famCID','cNumber','famSize')):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    return json.dumps(jsonTable)

def sqliteMedToJSON():
    jsonTable = []
    jsonRow = {}
    for row in demsDatabase.fetchMed():
        for index, field in enumerate(('medreportID','famID', 'evacID', 'evacueeName','medCause')):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    return json.dumps(jsonTable)

def sqliteReliefToJSON():
    jsonTable = []
    jsonRow = {}
    for row in demsDatabase.fetchRelief():
        for index, field in enumerate(('famID','reliefName','reliefDate','evacID','reliefRepName','reliefStatus')):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    # print("json.dumps(jsonTable): ", json.dumps(jsonTable))
    return json.dumps(jsonTable)

@eel.expose  # Expose function to JavaScript
def say_hello_py(x):
    """Print message from JavaScript on app initialization, then call a JS function."""
#    print("Hello from %s inside say_hello_py()" % x)
    eel.say_hello_js("Python through Eel, from within say_hello_py()!")

@eel.expose
def passDB_toJS(): # return a dict to JS
    databaseData = {
        'db_evacuees' : sqliteEvacToJSON(),
        'db_families' : sqliteFamToJSON(),
        'db_medAssist' : sqliteMedToJSON(),
        'db_relief' : sqliteReliefToJSON()
    }
    return databaseData

@eel.expose
def passEvacInfo_toJS():
    return demsDatabase.fetchEvacCenter()[0]

@eel.expose
def passStatsInfo_toJS():
    return [
        demsDatabase.countEvacueeTable()[0],
        demsDatabase.countFamilyTable()[0],
        demsDatabase.countMedTable()[0]
    ]

# ----- INSERT QUERIES ---------------------------------------------------------------------
@eel.expose
def sqlInsertFam(jsInput):
    # print(jsInput) #{'family_name': 'Familia', 'family_address': 'Mamamia'}
    demsDatabase.insertFam(jsInput['family_name'], jsInput['family_address'])
    # print("demsDatabase.idOfLastInsert()[0]: ", demsDatabase.idOfLastInsert()[0])
    demsDatabase.insertEContact(demsDatabase.idOfLastInsert()[0], '')

@eel.expose
def sqlInsertEvac(jsInput):
    # print(jsInput) #{'first_name': 'Pepito', 'middle_initial': 'SD', 'suffix': '', 'last_name': 'Manaloto', 'contact_number': '213', 'famID': 2, 'is_family_contact': True, 'is_relief_rep': True}
    demsDatabase.insertEvac(jsInput['first_name'], jsInput['middle_initial'], jsInput['last_name'], jsInput['suffix'], jsInput['contact_number'], jsInput['famID'])
    if(jsInput['is_family_contact']):
        demsDatabase.updateEContact(jsInput['famID'], demsDatabase.idOfLastInsert()[0])
    # print("demsDatabase.idOfLastInsert: ", demsDatabase.idOfLastInsert()[0], type(demsDatabase.idOfLastInsert())) # 1 <class 'tuple'>
    
@eel.expose
def sqlInsertMed(jsInput):
    # print(jsInput) #{'evacID': 6, 'famID': 2, 'medical_issue': 'ligma'}
    # print(demsDatabase.fetchFullName(jsInput['evacID'])[0])
    # print(demsDatabase.fetchFullName(jsInput['evacID'])[0])
    demsDatabase.insertMed(jsInput['famID'], jsInput['evacID'], jsInput['medical_issue'],)

@eel.expose
def sqlInsertRelief(jsInput):
    # print(jsInput) #{'relief_op_name': 'Tadaaaa'}
    # print(datetime.now().strftime('%Y-%m-%d'), " : ", demsDatabase.fetchFam())
    dateNow = datetime.now().strftime('%Y-%m-%d')
    for item in demsDatabase.fetchFam():
        demsDatabase.insertRelief(item[0], jsInput['relief_op_name'], dateNow, '', 0)

# ----- UPDATE QUERIES ---------------------------------------------------------------------
@eel.expose
def sqlUpdateEvacCenter(input):
    demsDatabase.updateEvacCenter(input)

@eel.expose
def sqlUpdateFam(jsInput):
    # print(jsInput) #{'famID': 3, 'famName': 'Bonifacio', 'famAddrss': 'Bonifacio Street', 'famCID': 11, 'cNumber': '192837142871', 'famSize': 2}
    demsDatabase.updateFamily(jsInput['famID'], jsInput['famName'], jsInput['famAddrss'])
    demsDatabase.updateEContact(jsInput['famID'], jsInput['evacID'])

@eel.expose
def sqlUpdateEvac(jsInput):
    # print(jsInput) #{'evacID': 5, 'fName': 'Primitivo', 'mi': 'M.', 'lName': 'Parayaoan', 'suffix': 'Jr.', 'cNumber': '12345', 'famID': 2}
    demsDatabase.updateEvac(jsInput['evacID'], jsInput['fName'], jsInput['mi'], jsInput['lName'], jsInput['suffix'], jsInput['cNumber'], jsInput['famID'], )

@eel.expose
def sqlUpdateMed(jsInput):
#    print("sqlUpdateMed: ", jsInput) #{'medreportID': 4, 'famID': 1, 'evacID': 1, 'fName': 'Pepito', 'lName': 'Manaloto', 'medCause': 'Sugma'}
    demsDatabase.updateMed(jsInput['medreportID'], jsInput['famID'], jsInput['evacID'], jsInput['medCause'])

@eel.expose
def sqlUpdateRelief(jsInput):
#    print("sqlUpdateRelief: ", jsInput) #{'famID': 2, 'reliefName': '3IB Operation', 'reliefDate': '2022-12-16', 'reliefRep': 7, 'reliefStatus': 1}
    demsDatabase.updateRelief(jsInput['famID'], jsInput['reliefName'], jsInput['reliefDate'], jsInput['evacID'], jsInput['reliefStatus'])

# ----- DELETE QUERIES ---------------------------------------------------------------------

@eel.expose
def sqlDeleteFam(jsInput):
    try:
        demsDatabase.removeEContact(jsInput['famID'])
        demsDatabase.removeFam(jsInput['famID'])
    except:
        return True

@eel.expose
def sqlDeleteEvac(jsInput):
    try:
        demsDatabase.removeEvac(jsInput['evacID'])
    except:
        return True

@eel.expose
def sqlDeleteMed(jsInput):
    try:
        demsDatabase.removeMed(jsInput['medreportID'])
    except:
        return True

@eel.expose
def sqlDeleteRelief(jsInput):
    try:
        demsDatabase.removeRelief(jsInput['reliefName'], jsInput['famID'])
    except:
        return True

@eel.expose
def sqlitecloseConnection():
    demsDatabase.closeConnection()

eel.init('web')
eel.browsers.set_path('electron', './node_modules/electron/dist/electron')


demsDatabase = demsDatabase('dems.db')


eel.start('index.html', mode='electron')

if __name__ == "__main__":
    print("Opening python...")
    # start_eel(False)
