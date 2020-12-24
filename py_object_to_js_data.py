import json
dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
js_data = json.dumps(dic)
print(js_data)
print(type(js_data))
print(type(dic))
