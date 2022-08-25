import json

#save stats

def save_status(dict):
    with open("status.json", "w") as json_file:
        json.dump(dict, json_file, indent=4)

