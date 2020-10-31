import requests
import json
import random
import pprint
from _collections import deque
url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users'
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]
temp = 0
# 숫자를 좌표로
num_to_pol = {}
pol_to_num = {}
for j in range(60):
    for i in range(59,-1,-1):
        num_to_pol[temp] = (i,j)
        pol_to_num[(i,j)] = temp
        temp += 1

def start(user, problem):
    uri = url + '/start'
    return requests.post(uri,headers={'X-Auth-Token':user},json={'problem':problem}).json()

def locations(token):
    uri = url + '/locations'
    return requests.get(uri, headers={'Authorization': token}).json()

def trucks(token):
    uri = url + '/trucks'
    return requests.get(uri, headers={'Authorization': token}).json()

def simulate(token, cmds):
    uri = url + '/simulate'
    return requests.put(uri, headers={'Authorization': token}, json={'commands': cmds}).json()

def score(token):
    uri = url + '/score'
    return requests.get(uri, headers={'Authorization': token}).json()

def move(a,b,flag,idx):
    pa,pb = num_to_pol[a],num_to_pol[b]
    # 밑으로 가야함
    if pa[0] < pb[0] :
        nx,ny = pa[0]+dx[3],pa[1]+dy[3]
        return 3,pol_to_num[(nx,ny)], flag
    # 위로 가야함
    elif pa[0] > pb[0] :
        nx, ny = pa[0] + dx[1], pa[1] + dy[1]
        return 1,pol_to_num[(nx,ny)], flag
    # 좌로 가야함
    elif pa[1] > pb[1] :
        nx, ny = pa[0] + dx[4], pa[1] + dy[4]
        return 4, pol_to_num[(nx,ny)],flag
    # 우로 가야함
    elif pa[1] < pb[1] :
        nx, ny = pa[0] + dx[2], pa[1] + dy[2]
        return 2, pol_to_num[(nx,ny)], flag
    # 목적지 도착
    else:
        # 담으러 왔음,담아야 함
        if not flag:
            return 5, a, not flag
        else:
            return 6, a, not flag


token = start('8cc582710da383d5df8c97d2dbbad477',2)['auth_key']
pprint.pprint(trucks(token), width=20, indent=4)
cmd = [
    {'truck_id': 0, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 1, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 2, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 3, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 4, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 5, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 6, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 7, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 8, 'command': [0, 0, 0, 0, 0]},
    {'truck_id': 9, 'command': [0, 0, 0, 0, 0]},

]
target = [deque() for _ in range(10)]
# 남은 자전거가 0인 애들
zero = []
# 남은 자전거가 4이상인 애들
over = []
# target 번호
index = 0
all_zero = [0 for _ in range(3600)]
all_over = [0 for _ in range(3600)]
for i in range(720):
    print(i)
    # 트럭의 명령
    loca = locations(token)
    # print(loca['locations'][3037]['located_bikes_count'])


    # 남은 자전거가 4이상 위치로 가서 0인 애들한테 가져다 줌

    truck = trucks(token)
    print(truck)
    for idx,tru in enumerate(truck['trucks']):
        # 현재 목표점이 있다면
        arr = []
        flag = tru['loaded_bikes_count']
        a = int(tru['location_id'])
        c = 0
        number = tru['id']
        for _ in range(6):
            if i<= 240:
                if number == 1 or number == 2 or number == 3:
                    if a != 3037:
                        c,a,flag = move(a, 3037,flag,idx)
                        arr.append(c)
                    else:
                        arr.append(5)
                elif number == 4 or number == 5 or number == 6:
                    if a != 2635:
                        c,a,flag = move(a, 2635,flag,idx)
                        arr.append(c)
                    else:
                        arr.append(0)
                else:
                    arr.append(0)
            elif 240 < i <= 480:
                if number == 1 or number == 2 or number == 3:
                    if a != 724:
                        c,a,flag = move(a, 724,flag,idx)
                        arr.append(c)
                    else:
                        arr.append(6)
                elif number == 4 or number == 5 or number == 6:
                    if a != 2635:
                        c,a,flag = move(a, 2635,flag,idx)
                        arr.append(c)
                    else:
                        arr.append(5)
                else:
                    arr.append(0)
                # 현재 자전거가 없다 -> 태울 위치로 감
            else:
                if number == 4 or number == 5 or number == 6:
                    if a != 2233:
                        c, a, flag = move(a, 2233, flag, idx)
                        arr.append(c)
                    else:
                        arr.append(6)
                else:
                    arr.append(0)

                # 없다면 그냥 대기8
        cmd[idx]['command'] = arr
    req = simulate(token, cmd)
    lo = locations(token)
    print(cmd)
k = score(token)
pprint.pprint(lo,width=20,indent=4)
print(target)
print(k)