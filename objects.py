import json

def setJson(info) -> None:
    obj = json.dumps(info, indent = 4)

    with open("data.json", "w") as file:
        file.write(obj)

def getJson() -> dict:
    with open("data.json", "r") as file:
        obj = json.load(file)
    
    return obj
