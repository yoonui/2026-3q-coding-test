def solution(nums):
    selectNum = len(nums) // 2
    numsSet = set(nums)

    if selectNum > len(numsSet):
        return len(numsSet)
    else: return selectNum

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))