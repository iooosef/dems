import sys
import platform
import eel

db_evacuees = {
    '000001': ['Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
    '000002': ['Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
    '000003': ['Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
    '000004': ['Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
    '000005': ['Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001'],
    '000006': ['Primitivo', 'M.', 'Parayaoan', 'Jr.', '09123456789', '001']
}

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

# """
# 原理是：
# 测试环境：
# 1、测试环境设置启动页面为vue的测试服务端口，然后将app设为None，
# 2、将端口和vue的public/index.html 中的eel.js绑定/
# 生产环境：
# 和正常的一样使用
# """
# def start_eel(develop):
#     """Start Eel with either production or development configuration."""
#     directory = 'web'
#     app = 'edge'
#     page = 'index.html'
#     eel_kwargs = dict(
#         mode=app,
#         port=0,
#         size=(1280, 800))
#     eel.init(directory)
#     say_hello_py("Python World!")
#     eel.say_hello_js(
#         "Python World!"
#     )  # Call a JavaScript function (must be after `eel.init()`)
#     try:
#         eel.start(page, **eel_kwargs)
#     except EnvironmentError:
#         # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
#         if sys.platform in ["win32", "win64"] and int(platform.release()) >= 10:
#             eel.start(page, mode="edge", **eel_kwargs)
#         else:
#             raise


if __name__ == "__main__":
    print("Opening python...")
    # start_eel(False)
