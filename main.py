# Importing modules
from ast import main
import sys
# Importing local modules
from research import main as rec
from sort import main as tri

# Configuration api keys
isitarealemailapi = "api key here"
leakcheckapi = "api key here"

if len(sys.argv) == 1:
    print("Invalid arguments")
    print("Use : python main.py -r [email...] | -t [file...]")
elif sys.argv[1] == "-r":
    rec.research(sys.argv[2],isitarealemailapi,leakcheckapi)
elif sys.argv[1] == "-t":
    tri.sort(sys.argv[2])
else:
    print("Invalid arguments")
    print("Use : python main.py -r [email...] | -t [file...]")

# https://github.com/SoikRs/PythInt