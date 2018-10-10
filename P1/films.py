import random

data = {'user' + str(i): 
            {'film' + str(random.randrange(1,10))
             for j in range(random.randrange(15))}
        for i in range(10)}

user = {'film1', 'film2', 'film3'}

maxn = 0
ans = set()

# 方案1 共同点最多
for i in data:
        print(i, data[i])
        if len(data[i] & user) > maxn:
                              maxn = len(data[i] & user)
for i in data:
        if len(data[i] & user) == maxn:
                print(i)
                ans = (data[i] - user) | ans;
print (ans)

# 方案2 有共同点的所有人
ans = set()
for i in data:
        print(i, data[i])
        if len(data[i] & user) != 0:
              ans = (data[i] - user) | ans 
print(ans)
