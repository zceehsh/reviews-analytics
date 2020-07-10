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


