# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/67258
# 누적합 , 이진탐색
# 자료구조 set, dict

def solution(gems):
    gemset = set(gems)
    sresult = 0 # 최종 스타트 지점
    eresult = 0 # 최종 엔드 지점
    rlength = 987654321 # s와 e의 간격
    settable = set()
    dicttable = {}

    estart = 0 
    stopsignal = False
    for s in range(len(gems)):
        for e in range(estart, len(gems)):
            if s>e:
                stopsignal = True
                break
            # dictionary 와 set 을 사용해서 현재 보유 보석 관리
            if gems[e] in dicttable.keys():
                dicttable[gems[e]] += 1
            else:
                settable.add(gems[e])
                dicttable[gems[e]] = 1

            if len(settable) == len(gemset):

                if e-s < rlength:
                    #print(s, e)
                    sresult = s
                    eresult = e
                    rlength = e-s
                break

        # END 지점이 앞으로 올 수 는 없다.
        estart = e

        # start 지점이 end 지점 보다 더 크면 잘못된 수치 더이상 조회 할 필요 없다. 
        if stopsignal is True:
            break

        # s 지점 증가를 위해 현재 위치 s 지점 데이터 제거 
        if gems[s] in dicttable.keys():
            if dicttable[gems[s]] == 1:
                del dicttable[gems[s]]
                settable.remove(gems[s])
            else:
                dicttable[gems[s]] -= 1

        # s 지점 후 현재 e 부터 반복하기 떄문에, 현재 지점의 e제거 (미제거시 중복처리됨)
        if gems[estart] in dicttable.keys():
            if dicttable[gems[estart]] == 1:
                del dicttable[gems[estart]]
                settable.remove(gems[estart])
            else:
                dicttable[gems[estart]] -= 1
    answer = [sresult+1, eresult+1]
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["ZZZ"]))
print(solution(["ZZZ", "ZZZ"]))


"""
기본 로직 

( start 지점   
) end 지점


("DIA"), "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"
("DIA", "RUBY"), "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"
("DIA", "RUBY", "RUBY"), "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"
("DIA", "RUBY", "RUBY", "DIA",) "DIA", "EMERALD", "SAPPHIRE", "DIA"
("DIA", "RUBY", "RUBY", "DIA", "DIA",) "EMERALD", "SAPPHIRE", "DIA"
("DIA", "RUBY", "RUBY", "DIA", "DIA" "EMERALD,)", "SAPPHIRE", "DIA"
("DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE"), "DIA" <-- 모든 보석 전부 구매


* 다이아 제거 하면서 기존에 있는지 확인
"DIA", ("RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE"), "DIA"

* 루비 제거 하면서 기존에 있는지 확인
"DIA", "RUBY",( "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE"), "DIA"

*루비 제거 하면 기존에 있는지 확인 했는데 없다 ( 결과 3, 7) 도출


다른 케이스 있는지 확인해보자
* 마지막 다이아를 사보자
"DIA", "RUBY",( "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA")

*전부 구매한 상태니까 st 지점을 한칸 이동해보자 ?
근데 루비 제거 하면 불가능 이기 떄문에 더이상탐색할것없음
End 지점이 이미끝지점


"""