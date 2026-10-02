import json

print("This is python json operation")


# JSON data is written as a string here.
# Triple quotes """ allow us to write multi-line strings.
jsonUser = """
{
    "name": "Ashwin",
    "age": 20,
    "isStudent": false,
    
    "address": {
        "Street": "1/23",
        "city": "Pune",
        "pincode": 222001
    },
    
    "skill": ["java", "python", "html"],
    
    "user": [
        {"name": "A", "age": 25},
        {"name": "B", "age": 30}
    ]
}
"""


# json.loads()
# ----------------
# loads = Load String
# Converts JSON string → Python object (usually dictionary)

# JSON:  
# "false" → Python False
# JSON object {} → Python dictionary
# JSON array [] → Python list

userDict = json.loads(jsonUser)

print(userDict)

# Check the Python data type after conversion
print(type(userDict))       # <class 'dict'>

# Access a value from the Python dictionary
print(userDict['age'])      # 20


# -------------------------------
# Python Dictionary → JSON String
# -------------------------------

todo = {
    'title': "learn python core for ai",
    'isComp': False
}


# json.dumps()
# ----------------
# dumps = Dump String
# Converts Python object → JSON string
#
# Python:
# False
#
# becomes JSON:
# false

jsonTodo = json.dumps(todo)

# After dumps(), the result is a STRING
print(type(jsonTodo))       # <class 'str'>
