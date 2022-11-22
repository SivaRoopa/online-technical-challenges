import json

json_object = "metadata.json"
data = json.loads(open(json_object).read())

#print(data)

my_var = input("type a keyword : ")

for key, value in data.items():
    for k1, v1 in value.items():
        if my_var is not None:
            if k1 == my_var:
                print(v1)