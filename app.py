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
var_to_js_incr = 0

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
    for row in demsDatabase.fetchFam():
        for index, field in enumerate(('famID','famName','famAddrss','famCID','cNumber','famSize')):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    return json.dumps(jsonTable)

def sqliteMedToJSON():
    jsonTable = []
    jsonRow = {}
    for row in demsDatabase.fetchMed():
        for index, field in enumerate(('medreportID','famID','evacID','fName','lName','medCause')):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    print(json.dumps(jsonTable))
    return json.dumps(jsonTable)

def sqliteReliefToJSON():
    jsonTable = []
    jsonRow = {}
    for row in demsDatabase.fetchRelief():
        for index, field in enumerate(('famID','reliefName','reliefDate','reliefRep','reliefStatus')):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    return json.dumps(jsonTable)
        

@eel.expose
def test_f(x):
    print("Hello World! Called from NewEntry.vue", x)


@eel.expose  # Expose function to JavaScript
def say_hello_py(x):
    """Print message from JavaScript on app initialization, then call a JS function."""
    print("Hello from %s inside say_hello_py()" % x)
    eel.say_hello_js("Python through Eel, from within say_hello_py()!")

@eel.expose
def passDB_toJS(): # return a dict to JS
    databaseData = {
        'db_evacuees' : sqliteEvacToJSON(),
        'db_families' : sqliteFamToJSON(),
        'db_medAssist' : sqliteMedToJSON(),
        'db_relief' : sqliteReliefToJSON()
    }
    # databaseData = {
    #     'db_evacuees' : sqliteTableToJSON('db_evacuees'),
    #     'db_families' : sqliteTableToJSON('db_families'),
    #     'db_medAssist' : sqliteTableToJSON('db_medAssist'),
    #     'db_relief' : sqliteTableToJSON('db_relief')
    # }
    return databaseData

@eel.expose
def sqlInsertFam(jsonInput):
    print(jsonInput) #{'family_name': 'Familia', 'family_address': 'Mamamia'}
    demsDatabase.insertFam(jsonInput['family_name'], jsonInput['family_address'], '', '')

@eel.expose
def sqlInsertEvac(jsonInput):
    print(jsonInput) #{'first_name': 'Pepito', 'middle_initial': 'SD', 'suffix': '', 'last_name': 'Manaloto', 'contact_number': '213', 'famID': 2, 'is_family_contact': True, 'is_relief_rep': True}
    print(type(jsonInput)) #<class 'dict'>
    demsDatabase.insertEvac(jsonInput['first_name'], jsonInput['middle_initial'], jsonInput['last_name'], jsonInput['suffix'], jsonInput['contact_number'], jsonInput['famID'])
    print("demsDatabase.idOfLastInsert: ", demsDatabase.idOfLastInsert()[0], type(demsDatabase.idOfLastInsert())) # 1 <class 'tuple'>
    if jsonInput['is_family_contact']: # If selected to be family contact, will update the corresponding family's contact details
        demsDatabase.updateFamContact(jsonInput['famID'], demsDatabase.idOfLastInsert()[0], jsonInput['contact_number'])
    
@eel.expose
def sqlInsertMed(jsonInput):
    # print(jsonInput) #{'evacID': 6, 'famID': 2, 'medical_issue': 'ligma'}
    # print(demsDatabase.fetchFullName(jsonInput['evacID'])[0])
    demsDatabase.insertMed(jsonInput['famID'], jsonInput['evacID'], 
        demsDatabase.fetchFullName(jsonInput['evacID'])[0][0], 
        demsDatabase.fetchFullName(jsonInput['evacID'])[0][1], 
        jsonInput['medical_issue'],)

@eel.expose
def sqlInsertRelief(jsonInput):
    print(jsonInput) #{'relief_op_name': 'Tadaaaa'}
    print(datetime.now().strftime('%Y-%m-%d'), " : ", demsDatabase.fetchFam())
    dateNow = datetime.now().strftime('%Y-%m-%d')
    for item in demsDatabase.fetchFam():
        demsDatabase.insertRelief(item[0], jsonInput['relief_op_name'], dateNow, '', 0)


@eel.expose
def passEvacInfo_toJS():
    return evacDBpy

eel.init('web')
eel.browsers.set_path('electron', './node_modules/electron/dist/electron')


demsDatabase = demsDatabase('dems.db')


eel.start('index.html', mode='electron')

if __name__ == "__main__":
    print("Opening python...")
    # start_eel(False)
