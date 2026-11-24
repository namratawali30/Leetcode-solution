class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix += num
            count += freq[prefix - k]
            freq[prefix] += 1

        return count




        