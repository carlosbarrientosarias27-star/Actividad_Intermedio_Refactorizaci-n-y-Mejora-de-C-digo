def p(d, t, dc=0):
r = 0
for i in d:
if t == 'A':
if i['s'] == 1:
r += i['p'] * i['q']
elif t == 'B':
if i['s'] == 1:
r += i['p'] * i['q'] * 0.9
elif i['s'] == 2:
r += i['p'] * i['q'] * 0.8
else:
r += i['p'] * i['q']
if dc > 0:
r = r - (