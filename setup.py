import os
import json

os.system("python -m pip install pygame")

with open("log/log.json", "w") as log_file:
    json.dump({"turn" : 0,"maxScore" : 0}, log_file)