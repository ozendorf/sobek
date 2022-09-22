import json
import sys
counter = {}

def used_actions(user):
  with open('./activity_log_full', 'r') as f:
    logs = json.load(f)
  print(user)
  counter = {}
  for i in logs:
    if i['caller'] == user:
      print('The caller is ', user)
      print(json.dumps(i['authorization']['action'], indent=4))
      action = i['authorization']['action']   
      counter[action] = counter.get(action, 0) +1
  print('counter result is:')
  print(counter)
  return counter
      
user = sys.argv[1]
used_actions(user)
print('counter result is:')
print(counter)