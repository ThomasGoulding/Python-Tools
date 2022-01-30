import json

#Python Dictionary
x = {
  "name": "Tom",
  "age": 22,
}

# convert into JSON:
y = json.dumps(x)

# Print out JSON File
print(y)
