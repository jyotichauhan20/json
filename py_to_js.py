import json
# a={'a':'1','b':'2'}
# b=json.dumps(a)
# print(b)
ini_string = {"nikhil": 1, 'akash' : 5,  
              'manjeet' : 10, 'akshat' : 15} 
final_dictionary = json.loads(ini_string)
print(final_dictionary) 
