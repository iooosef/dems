import sys
import platform
import eel 
import json

# Expected format of data fetched from DB to be passed to front-end
sampleDB = {
    'db_evacuees' : [
        (1,'Joseph Clarence','C','Parayaoan','','09123456789',1),
        (2,'Joseph','C','Parayaoan','','09123456781',1),
        (3,'Clarence','C','Parayaoan','','09123456782',1),
        (4,'Primitivo','M','Parayaoan','Jr.','09123456783',1),
        (5,'Rosemarie','C','Parayaoan','','09123456784',1),
        (6,'Juan','DL','Dela Cruz','Sr.','09123456785',2),
        (7,'Maria','S','Dela Cruz','','09123456786',2),
        (8,'Mark','H','Sierra','III','09123456787',3)
    ],
    'db_families' : [
        (1, 'Parayaoan', '16 7th St., Youngstown Vill., Cainta, Rizal', 4, '09123456783', 5),
        (2, 'Dela Cruz', 'Salakdwa Vill., Cainta, Rizal', 6, '09123456785', 2),
        (3, 'Sierra', 'World, Moon', 8, '09123456787', 1)
    ],
    'db_medAssist' : [
        (1, 1, 'Joseph Clarence', 'Parayaoan', 'Pneumonia'),
        (8, 3, 'Mark', 'Sierra', 'Fever')
    ],
    'db_relief' : [
        (1, 'R0001', '2022-07-22', 'Clarence', 1),
        (2, 'R0001', '2022-07-22', 'Juan', 1),
        (3, 'R0001', '2022-07-22', 'Mark', 1),
        (1, 'R0002', '2022-09-22', 'Clarence', 1),
        (2, 'R0002', '2022-09-22', 'Juan', 1),
        (3, 'R0002', '2022-09-22', 'Mark', 1),
        (1, 'R0003', '2022-10-22', 'Clarence', 0),
        (2, 'R0003', '2022-10-22', 'Juan', 1),
        (3, 'R0003', '2022-10-22', 'Mark', 0)
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
            'db_families': ('famID','famName','famAddrss','famCName','cNumber','famSize'),
            'db_medAssist': ('famID','evacID','fName','lName','medCause'),
            'db_relief': ('famID','reliefName','reliefDate','reliefRep','reliefStatus')
        }
        for index, field in enumerate(fields[table]):
            jsonRow[field] = row[index]
        jsonTable.append(jsonRow)
        jsonRow = {}
    return json.dumps(jsonTable)


@eel.expose  # Expose function to JavaScript
def say_hello_py(x):
    """Print message from JavaScript on app initialization, then call a JS function."""
    print("Hello from %s inside say_hello_py()" % x)
    eel.say_hello_js("Python through Eel, from within say_hello_py()!")

@eel.expose
def passDB_toJS(): # return a dict to JS
    databaseData = {
        'db_evacuees' : sqliteTableToJSON('db_evacuees'),
        'db_families' : sqliteTableToJSON('db_families'),
        'db_medAssist' : sqliteTableToJSON('db_medAssist'),
        'db_relief' : sqliteTableToJSON('db_relief')
    }
    return databaseData

@eel.expose
def passEvacInfo_toJS():
    return evacDBpy

eel.init('web')
eel.browsers.set_path('electron', './node_modules/electron/dist/electron')
eel.start('index.html', mode='electron')

if __name__ == "__main__":
    print("Opening python...")
    # start_eel(False)
