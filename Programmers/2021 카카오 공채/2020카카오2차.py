import requests
import json
import random
url = "https://wqwfrkh5k1.execute-api.ap-northeast-2.amazonaws.com/kakao-2020"

def start(user, problem):
    uri = url + '/start'
    return requests.post(uri,headers={'X-Auth-Token':user},json={'problem':problem}).json()

def users(token):
    uri = url + '/users'
    return requests.get(uri, headers={'Authorization': token}).json()

def new_users(token):
    uri=url + '/new_users'
    return requests.get(uri,headers={'Authorization':token}).json()

def recommend(token, cmds):
    uri = url + '/recommend'
    return requests.post(uri, headers={'Authorization': token}, json={'recommendations': cmds}).json()

def run_simulation(token):
    uri = url + '/run_simulation'
    return requests.put(uri,headers={'Authorization':token}).json()

def status(token):
    uri = url + '/status'
    return requests.get(uri,headers={'Authorization':token}).json()

def score(token):
    uri=url + '/score'
    return requests.get(uri,headers={'Authorization':token}).json()

def simulator():
    user = 'b8e662824d8a80c8efa5d7a28eaf3a03'
    problem = 1
    ret=start(user,problem)
    print(ret)
    token = ret['token']
    mp = dict()
    idx=0
    rev = [""]*200
    while(1):
        rec=[]
        p = [[0] * 200 for i in range(200)]  # phone
        f = [[0] * 200 for i in range(200)]  # follow
        check=[0]*100
        temp=users(token)
        jstr=json.dumps(temp)
        str=json.loads(jstr)
        print(str)
        temp2=new_users(token)
        for us in str["users"]:
            if(not us["user"] in mp):
                mp[us["user"]]=idx
                rev[idx]=us["user"]
                idx+=1
        for us in str["users"]:
            for i in us["phone"]:
                if(not i in mp):
                    mp[i]=idx
                    rev[idx]=i
                    idx+=1
                p[mp[us["user"]]][mp[i]]=1
            ct=0
            for i in us["following"]:
                ct+=1
                if(not i in mp):
                    mp[i]=idx
                    rev[idx]=i
                    idx+=1
                f[mp[us["user"]]][mp[i]]=1
            check[mp[us["user"]]]=ct
        cnt=0
        for i in range(100):
            rect = {"user": "", "recommendation": []}
            rect["user"]=rev[i]
            if(check[i]>=20 or cnt==100):
                rec.append(rect)
                continue
            flag= False
            count=0
            for j in range(100):
                if(p[i][j]==1 and f[i][j]==0):
                    rect["recommendation"].append(rev[j])
                    count+=1
                    cnt+=1
                    if(cnt==100 or count==10):
                        break
                if(cnt==100):
                    break
            if(count<10):
                for j in range(idx):
                    if(f[i][j]==1):
                        continue
                    if(p[i][j]==0):
                        rect["recommendation"].append(rev[j])
                        count+=1
                        cnt+=1
                        if(cnt==100 or count==10):
                            break
                    if(cnt==100):
                        break
            rec.append(rect)
        print(rec)
        ttt=recommend(token,rec)
        #print(ttt)
        tt=run_simulation(token)
        #print(tt)
        finish=False
        while(1):
            state = status(token)
            print(state)
            if(state["status"]=="working"):
                continue
            elif(state["status"]=="done"):
                break
            elif(state["status"]=="finish"):
                finish=True
                break
        print(check)
        if(finish):
            break

if __name__ == '__main__':
    simulator()


