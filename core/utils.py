import json

def save_result(data):
    with open("output/results.json", "w") as f:
        json.dump(data, f, indent=4)
