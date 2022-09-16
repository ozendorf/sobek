import json
import sys

with open('./activity_log_full', 'r') as f:
  logs = json.load(f)

user = sys.argv[1]
print(user)
for i in logs:
    if i['caller'] == user:
        print('The caller is ', user)
        print(json.dumps(i['authorization']['action'], indent=4))

	
