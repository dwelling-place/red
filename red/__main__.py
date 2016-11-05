import red
from werkzeug.serving import run_simple

red.application.debug = True

run_simple('localhost', 5000, red.application,
           use_reloader=True, use_debugger=True, use_evalex=True)