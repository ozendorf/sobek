import json

with open('./roledefinition', 'r') as f:
  roledefinition = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(json.dumps(roledefinition, indent=4))