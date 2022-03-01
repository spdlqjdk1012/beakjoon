# 문제 링크 https://www.acmicpc.net/problem/1759

# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
# 1<=모음<= L-2

L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
#print(alphabet)

result = []
def dfs(depth, start, vcnt):
    global result
    vowel = ['a', 'e', 'i', 'o', 'u']
    if depth == L:
        if 1<=vcnt<=L-2: 
            print(*result, sep="")
        #print(*result, vcnt)
        return
    
    for i in range(start, C):
        tmpv = 0
        for v in vowel:
            if alphabet[i] == v:
                tmpv = 1
                break
        tmpv += vcnt
        result.append(alphabet[i])
        dfs(depth+1, i+1, tmpv)
        result.pop()
dfs(0, 0, 0)


"""
<dfs 조합 문제>

조건1. abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
=> for i in range(start, C) start부터 돌리면서 순서 보장
[a,b,c,d] 일 떄 c를 보고 있으면 d부터 본다는 뜻


조건2. 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
=>dfs 파라미터로 vcnt 넘겨줌, vcnt는 모음의 갯수이다!
해당 조회하는 문자열이 모음일 경우 모음 카운팅 갯수 증가

"""