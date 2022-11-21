import eel

eel.init("webapp")
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')

eel.start("index.html", mode='electron')