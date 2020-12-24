import json

py= {
  "name": "John",
  "age": 30,
  "city": "New York"
}

js_str = json.dumps(py)
print(js_str)
print(type(js_str))
print(type(py))
