
a=[0,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,0]
l = len(a)
c = 0; cost = [1 for i in range(l)]; k = 13; j = 0
while l > 1:
    j += 1
#    print('')
#    print('ITER #',j)
    l //= 2
#    print('l = ', l)
    T = 0
    L = [a[i] for i in range(l)]
    R = [a[i+l] for i in range(l)]
    b = [(L[i] + R[i]) % 2 for i in range(l)]
    for i in range(l):
        T = T + b[i] * min(cost[i],cost[i+l])
    a = [0 for i in range(l)]
    if T <= k:
        k = k - T
        for i in range(l):
            if b[i] == 1:
                if cost[i] <= cost[i+l]:
                    L[i] = R[i]
                    cost[i] = cost[i+l] - cost[i]
                else:
                    cost[i] = cost[i] - cost[i+l]
            else:
                cost[i] = cost[i] + cost[i+l]
        a = [L[i] for i in range(l)]
    else:
        c = c + l
        a = [b[i] for i in range(l)]
        cost = [min(cost[i],cost[i+l]) for i in range(l)]

if (a[0] == 1) & (cost[0] > k):
    c += 1
    print('final c = ', c)
if c==0:
    print('zero')


                    
        
    