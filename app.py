import sys
import platform
import eel

# Expected format of data fetched from DB to be passed to front-end
tableDBpy = {
    'db_evacuees' : [
        ['000001', 'Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
        ['000002', 'Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
        ['000003', 'Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
        ['000004', 'Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
        ['000005', 'Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
        ['000006', 'Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001']
    ],
    'db_families' : [
        ['001', 'Parayaoan', '16 7th St., Youngstown Vill., Cainta, Rizal', '000001', '09123456789', '5'],
        ['002', 'Parayaoan', '16 7th St., Salakdwa Vill., Cainta, Rizal', '000001', '09123456789', '5'],
        ['003', 'asdawokdaskdlaksd', 'dakwdnlkjflemadla., Cainta, Rizal', '000001', '09123456789', '5'],
        ['004', 'Parayaoan', 'skfdslklskflsdkf, Cainta, Rizal', '000001', '09123456789', '5'],
        ['005', 'Parayaoan', '16 7th St., Youngstown Vill., Cainta, Rizal', '000001', '09123456789', '5']
    ],
    'db_medAssist' : [
        ['000001', '001', 'Joseph Clarence', 'Parayaoan', 'Injury'],
        ['000002', '001', 'Joseph Clarence', 'Parayaoan', 'Injury'],
        ['000003', '001', 'Joseph Clarence', 'Parayaoan', 'Fever'],
        ['000004', '001', 'Joseph Clarence', 'Parayaoan', 'Injury'],
        ['000005', '001', 'Joseph Clarence', 'Parayaoan', 'Injury']
    ]
}
var_to_js_incr = 0

@eel.expose  # Expose function to JavaScript
def say_hello_py(x):
    """Print message from JavaScript on app initialization, then call a JS function."""
    print("Hello from %s inside say_hello_py()" % x)
    eel.say_hello_js("Python through Eel, from within say_hello_py()!")

@eel.expose
def passDB_toJS(): # return a dict to JS
    return tableDBpy

eel.init('web')
eel.browsers.set_path('electron', './node_modules/electron/dist/electron')
eel.start('index.html', mode='electron')

if __name__ == "__main__":
    print("Opening python...")
    # start_eel(False)
