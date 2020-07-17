data = []
count = 0
length = 0
with open ('reviews.txt', 'r') as f:
    for line in f:  
 	    data.append(line)
 	    count += 1
 	    if count % 1000 == 0:
 	    	print(len(data))
print('档案读取完了， 共有', len(data), '个留言')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('每一个留言的平均长度是： ', sum_len / len(data))

#筛选概念
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[2])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '笔留言提到good')
# print(good[0])

#清单快写法 list comprehension
good = [d for d in data if 'good' in d]
print(good)

bad = ['bad' in d for d in data]
print(bad)

bad = []
for d in data:
	bad.append('bad' in d)

