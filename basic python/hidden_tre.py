def solve(n, nums):
    pairs = []
    for i in nums:
        for j in nums[i:]:
            pairs.append(i + j)
    print(pairs)


n = int(input())
nums = list(map(int, input().split()))

print(nums)

out_ = solve(n, nums)
print(out_)
