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
      #print('The caller is ', user)
      #print(json.dumps(i['authorization']['action'], indent=4))
      action = i['authorization']['action']   
      counter[action] = counter.get(action, 0) +1
  return counter

def assigned_roles(user):
  with open('./role_assignments', 'r') as f:
    roles_file = json.load(f)
    roles = {}
  n=0  
  for i in roles_file:
    n += 1
    roles[n] = i['roleDefinitionName']
  return roles  
  
user = sys.argv[1]
counter = used_actions(user)
#print('counter result is:')
#print(counter)
roles = assigned_roles(user)
print(roles)