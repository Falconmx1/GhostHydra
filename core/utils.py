import json
from datetime import datetime

def save_result(target, service, username, password):
    data = {
        "target": target,
        "service": service,
        "username": username,
        "password": password,
        "timestamp": str(datetime.now())
    }

    with open("output/results.json", "w") as f:
        json.dump(data, f, indent=4)
