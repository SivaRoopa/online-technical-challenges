import json

#{"x":{"y":{"z":"a"}}}
# {"a":{"b":{"c":"d"}}}
object=json.loads(input("Enter dictionary"))

def keyvalue_items(object):
    key =""
    value=""
    for k, v in object.items():
        obj1 = k
        for k1, v1 in v.items():
            obj2 = k1
            for k2, v2, in v1.items():
                obj3 =k2
                val1 = v2
    key = '/'.join([obj1,obj2,obj3])
    value = val1
    print("Key= ",key)
    print("Value=", value)
    return  key, value

keyvalue_items(object)