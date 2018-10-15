import random,string

passwd = ''.join([random.choice(string.digits) for i in range(6)])
print(passwd)


from collections import Counter

words = ['good', 'hello', 'world', 'python', 'dalian', 'china', 'great']

chk_words = ('god', 'hood', 'python', 'chine')

words_freq = {x:dict(Counter(x)) for x in words}

for i in chk_words:
    if i in words:
        print(i, i)
    else:
        i_freq = dict(Counter(i))
        d = {                                                      ## d is dict，单词为 key，字符次数差的list 为 value
            j:[i_freq[ch] - words_freq[j].get(ch,0) for ch in i] \
            + [words_freq[j].get(ch) - i_freq.get(ch, 0)  for ch in j] \
        for j in words_freq
        }
        ans = min(d.items(), key = lambda item:sum(map(lambda i : i**2,item[1]))) # 在 d.items（） 中找最小值，按照 key = sum的规则， sum = list 每项平方和
        print(i, ans[0])