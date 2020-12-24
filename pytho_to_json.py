import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
} 
with open("myfile.json","w") as a:
    json.dump(dict1, a, indent = 6)
    print(type(dict1))
    print(dict1)

