import json
import os

DB_FILE = "output/db.json"

def save_entry(entry):
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

    with open(DB_FILE, "r") as f:
        data = json.load(f)

    data.append(entry)

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_entries():
    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as f:
        return json.load(f)
