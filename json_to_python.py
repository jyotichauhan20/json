import json
js =  '{ "name":"John", "age":30, "city":"New York"}'

py = json.loads(js)
print(type(py))
print(type(js))
print(py["age"])