import requests
import json
from pprint import pprint
from _collections import deque

def start(user_key,problem_id,cnt):
    url = 'http://localhost:8000/start'
    req = requests.post(url+'/'+user_key+'/'+problem_id+'/'+cnt)
    temp = json.loads(req.text)
    return temp

def oncall(token):
    url = 'http://localhost:8000/oncalls'
    req = requests.get(url,headers={'X-Auth-Token': token})
    temp = json.loads(req.text)
    return temp['calls']

def action(token,cmd):
    url = 'http://localhost:8000/action'
    req = requests.post(url,headers={'X-Auth-Token': token}, json={'commands': cmd})
    temp = json.loads(req.text)
    return temp

st  = start('tester','2','4')
token = st['token']
target = [deque() for _ in range(4)]
passen = [[] for _ in range(4)]
cmd = [{'elevator_id': 0, 'command': 'STOP'},
        {'elevator_id': 1, 'command': 'STOP'},
        {'elevator_id': 2, 'command': 'STOP'},
        {'elevator_id': 3, 'command': 'STOP'}]
time = 0
index = 0
escape = 0
flag = False
while not flag:
    print('time',time)
    calls = oncall(token)
    print(calls)
    print(target)
    print(escape)
    for call in calls:
        if call['timestamp'] == time:
            target[index%4].append((call['id'],call['start'],call['end']))
            index += 1
    # elevator : (타는 위치, 내리는 위치)

    act = action(token,cmd)
    for dic in cmd:
        if 'call_ids' in dic:
            del dic['call_ids']

    for idx,elev in enumerate(act['elevators']):
        # target이 없다 -> 사람이 없다는 거니까 continue
        if not target[idx]:
            cmd[idx]['command'] = 'STOP'
            continue
        # 지금 엘베 위치
        floor = elev['floor']
        id,t_start,t_end = target[idx][0]
        # 엘베안에 목표가 탔음 -> 내려줘야지
        if id in passen[idx]:
            if floor == t_end:
                if cmd[idx]['command'] == 'EXIT':
                    cmd[idx]['command'] = 'CLOSE'
                    target[idx].popleft()
                    escape += 1
                elif cmd[idx]['command'] == 'OPEN':
                    cmd[idx]['command'] = 'EXIT'
                    # 'call_ids': [2, 3]
                    cmd[idx]['call_ids'] =  [id]
                elif cmd[idx]['command'] == 'UP' or cmd[idx]['command'] == 'DOWN':
                    cmd[idx]['command'] = 'STOP'
                elif cmd[idx]['command'] == 'STOP':
                    cmd[idx]['command'] = 'OPEN'
                elif cmd[idx]['command'] == 'CLOSE':
                    cmd[idx]['command'] = 'UP'
            elif cmd[idx]['command'] == 'OPEN':
                cmd[idx]['command'] = 'CLOSE'

            elif floor > t_end:
                if cmd[idx]['command'] == 'DOWN':
                    cmd[idx]['command'] = 'DOWN'
                elif cmd[idx]['command'] == 'UP':
                    cmd[idx]['command'] = 'STOP'
                elif cmd[idx]['command'] == 'STOP' or cmd[idx]['command'] == 'CLOSE':
                    cmd[idx]['command'] = 'DOWN'
            elif floor < t_end:
                if cmd[idx]['command'] == 'UP':
                    cmd[idx]['command'] = 'UP'
                elif cmd[idx]['command'] == 'DOWN':
                    cmd[idx]['command'] = 'STOP'
                elif cmd[idx]['command'] == 'STOP' or cmd[idx]['command'] == 'CLOSE':
                    cmd[idx]['command'] = 'UP'
        # 없다. -> 태워야지
        else:
            if floor == t_start:
                if cmd[idx]['command'] == 'ENTER':
                    passen[idx].append(id)
                    # elev['passengers'].append(elev['id'])
                    cmd[idx]['command'] = 'CLOSE'

                elif cmd[idx]['command'] == 'OPEN':
                    cmd[idx]['command'] = 'ENTER'
                    cmd[idx]['call_ids'] = [id]
                elif cmd[idx]['command'] == 'UP' or cmd[idx]['command'] == 'DOWN':
                    cmd[idx]['command'] = 'STOP'
                elif cmd[idx]['command'] == 'STOP':
                    cmd[idx]['command'] = 'OPEN'
                elif cmd[idx]['command'] == 'CLOSE':
                    cmd[idx]['command'] = 'UP'

            elif cmd[idx]['command'] == 'OPEN':
                cmd[idx]['command'] = 'CLOSE'
            elif floor > t_start:
                if cmd[idx]['command'] == 'DOWN':
                    cmd[idx]['command'] = 'DOWN'
                elif cmd[idx]['command'] == 'UP':
                    cmd[idx]['command'] = 'STOP'
                elif cmd[idx]['command'] == 'STOP' or cmd[idx]['command'] == 'CLOSE':
                    cmd[idx]['command'] = 'DOWN'

            elif floor < t_start:
                if cmd[idx]['command'] == 'UP':
                    cmd[idx]['command'] = 'UP'
                elif cmd[idx]['command'] == 'DOWN':
                    cmd[idx]['command'] = 'STOP'
                elif cmd[idx]['command'] == 'STOP' or cmd[idx]['command'] == 'CLOSE':
                    cmd[idx]['command'] = 'UP'

    time += 1
    flag = act['is_end']
print(act)



# call = oncall('kqBeE')
# pprint(call)

# cmd = [{'elevator_id': 0, 'command': 'CLOSE'},{'elevator_id': 1, 'command': 'CLOSE'}]
# act = action('kqBeE',cmd)
# pprint(act)

# cmd = [{'elevator_id': 0, 'command': 'UP'},{'elevator_id': 1, 'command': 'UP'}]
# act = action('kqBeE',cmd)
# pprint(act)