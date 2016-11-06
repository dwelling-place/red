import red
from werkzeug.serving import run_simple


app = red.create_app()
app.debug = True

run_simple('localhost', 5000, app,
           use_reloader=True, use_debugger=True, use_evalex=True)