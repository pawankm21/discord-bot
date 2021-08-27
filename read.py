import json

def write_json(data,filename="information.json"):
    with open(filename,"w") as f:
        json.dump(data,f, indent=4)


def append_json( key, value, filename="information.json"):
    with open(filename) as json_file:
        data=json.load(json_file)
        temp=data[key]
        if value not in temp:
            temp.append(value)
        
    write_json(data)

def read_json(key,filename="information.json"):
    with open(filename) as json_file:
        data=json.load(json_file)
        temp=data[key]
    return temp


append_json("DIALOGUES","chup ho ja surya","information.json")
print(read_json("DIALOGUES","information.json"))