import json

complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}')

simple_object =json.loads('{"real": 4, "img": 3}')

print("Complex_object: ",complex_object)
print("Without complex object",complex_object)