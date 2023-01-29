import json

def setJson(info) -> None:
    obj = json.dumps(info, indent = 4)

    with open("data.json", "w") as file:
        file.write(obj)

def getJson():
    try:
        file = open("data.json", "r")
        data = json.loads(file.read())
        file.close()
        return data
    except:
        return {"hand":False}
     