import os
import json
def load_history():
    if os.path.isfile("history.json") == True:
        with open("history.json", "r") as f:
            history =json.load(f)
            return history

