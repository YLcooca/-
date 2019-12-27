# 随机给一组非负整数，计算能收集多少水在下雨后，1代表1个高度
# 从最底层开始逐级往上找 
l = [1, 0, 0, 0, 1]
sums = 0
while l.count(0) < len(l) - 1:
    indexs = []
    for i, j in enumerate(l.copy()):
        if j > 0:
            indexs.append(i)
            l[i] -= 1
    for k in range(len(indexs)-1):
        sums += indexs[k+1] - indexs[k] - 1
    indexs.clear()
print(sums)
