# https://www.acmicpc.net/problem/21315
import sys
import math

N = int(input())
card = [i for i in range(1, N+1)]
shuffleCard = []
normalCard = []
result = list(map(int, input().split()))

def shuffle(cardCnt):
    global card
    global shuffleCard
    global normalCard
    tmp = []    
    for i in range(cardCnt):
        tmp.append(shuffleCard.pop())
    tmp.reverse()
    normalCard = shuffleCard+normalCard
    shuffleCard = tmp
    card = shuffleCard+normalCard
    #print(shuffleCard, normalCard)


def process(K):
    global card
    global shuffleCard
    global normalCard
    cnt = 2 ** (K-1+1)    # 2^2 = 4 
    normalCard = card[0:N-cnt] # 1
    shuffleCard = card[N-cnt:N]  # 2 3 4 5 
    card = shuffleCard+normalCard
    #print("st", shuffleCard, normalCard)
    for i in range(2, K+2): # i는 1~3        
        cnt = 2 ** (K-i+1)        
        shuffle(cnt)


#process(2)
#process(1)

# k 값을 구하는 dfs 두가지 케이스 1<=k<10   11 가능 12 21 별도 취급, permutation 순열
dfsresult = []
def dfs(depth):
    global dfsresult
    global card
    if depth == 2:
        #print(dfsresult)
        process(dfsresult[0])
        process(dfsresult[1])
        allcheck = 1
        for i in range(len(result)):
            if result[i] != card[i]:
                allcheck = 0
                break
        if allcheck == 1:
            print(*dfsresult)
            sys.exit()
        card = [i for i in range(1, N+1)]
        return
    
    for i in range(1, 10):
        if 2**i >= N:
            continue
        dfsresult.append(i)
        dfs(depth+1)
        dfsresult.pop()

dfs(0)
