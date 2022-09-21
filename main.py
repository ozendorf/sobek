import json
import sys

def used_actions(user):
  with open('./activity_log_full', 'r') as f:
    logs = json.load(f)
  print(user)
  n = 0
  for i in logs:
    if i['caller'] == user:
      n = n + 1
      print('The caller is ', user)
      print(json.dumps(i['authorization']['action'], indent=4))
      action = i['authorization']['action']
      counter = action
      counter[action] += 1
      
counter = {}
user = sys.argv[1]
used_actions(user)
print(counter)