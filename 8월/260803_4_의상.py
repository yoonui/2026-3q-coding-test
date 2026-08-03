def solution(clothes):
    dictList = {}

    for i, id in clothes:
        if id not in dictList:
            dictList[id] = [i]
        else:
            dictList[id].append(i)

    answer = 1
    for i in dictList:
        answer *= len(dictList[i])+1

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))